from django.db import models
from django.db.models import Func, F, Q
from django.db.models.functions import Cast
from django_cte import With, CTEManager

from django_pg_rrule.fields import RruleField
from datetime import datetime


class RecurrenceManager(CTEManager):
    date_start_field = "date_start"
    date_end_field = "date_end"
    datetime_start_field = "datetime_start"
    datetime_end_field = "datetime_end"
    until_field = "rrule_until"

    def with_occurrences(self, start: datetime | None, end: datetime | None):
        """Evaluate rrules and annotate all occurrences."""

        # Annotate occurrences of datetimes
        with_qs_datetimes = self.filter(
            **{f"{self.datetime_start_field}__isnull": False}
        )
        if start and end:
            with_qs_datetimes = with_qs_datetimes.filter(
                Q(**{f"{self.datetime_start_field}__lte": end})
                & (
                    Q(**{f"{self.until_field}__isnull": True})
                    | Q(**{f"{self.until_field}__gte": start})
                )
            )

        cte_datetimes = With(
            with_qs_datetimes.only("id")
            # Get occurrences
            .annotate(
                odatetime=Func(
                    Func(
                        Cast("rrule", output_field=RruleField()),
                        F(self.datetime_start_field),
                        function="get_occurrences",
                        output_field=models.DateTimeField(),
                    ),
                    function="UNNEST",
                )
            )
            # Combine with rdatetimes
            .union(
                self.filter(
                    **{
                        f"{self.datetime_start_field}__isnull": False,
                        "rdatetimes__isnull": False,
                    }
                )
                .only("id")
                .annotate(odatetime=Func(F("rdatetimes"), function="UNNEST"))
            ),
            name="qodatetimes",
        )

        # Annotate occurrences of dates
        with_qs_dates = self.filter(
            **{f"{self.date_start_field}__isnull": False, "rrule__isnull": False}
        )
        if start and end:
            with_qs_dates = with_qs_dates.filter(
                Q(**{f"{self.date_start_field}__lte": end.date()})
                & (
                    Q(**{f"{self.until_field}__isnull": True})
                    | Q(**{f"{self.until_field}__gte": start})
                )
            )

        cte_dates = With(
            with_qs_dates.only("id")
            # Get occurrences
            .annotate(
                odate=Func(
                    Func(
                        Cast("rrule", output_field=RruleField()),
                        F(self.date_start_field),
                        function="get_occurrences",
                        output_field=models.DateField(),
                    ),
                    function="UNNEST",
                )
            )
            # Combine with rdates
            .union(
                self.filter(
                    **{
                        f"{self.date_start_field}__isnull": False,
                        "rdates__isnull": False,
                    }
                )
                .only("id")
                .annotate(odate=Func(F("rdates"), function="UNNEST"))
            ),
            name="qodates",
        )
        qs = (
            # Join WITH clauses with actual data
            cte_datetimes.join(
                cte_dates.join(self.model, id=cte_dates.col.id, _join_type="FULL JOIN"),
                id=cte_datetimes.col.id,
                _join_type="FULL JOIN",
            )
            # Annotate WITH clauses
            .with_cte(cte_datetimes)
            .with_cte(cte_dates)
            .annotate(
                odatetime=cte_datetimes.col.odatetime,
                odate=Cast(cte_dates.col.odate, output_field=models.DateField()),
            )
            # Exclude exdatetimes and exdates
            .filter(
                ~(
                    Q(odatetime__isnull=False)
                    & Q(exdatetimes__contains=[F("odatetime")])
                )
                & ~(Q(odate__isnull=False) & Q(exdates__contains=[F("odate")]))
            )
        )
        return qs
