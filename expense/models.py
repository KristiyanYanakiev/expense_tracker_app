from django.db import models
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.utils import timezone

from expense.choices import ExpenseCategoryChoices
from expense.validators import positive_float_validators


class ExpenseQuerySet(models.QuerySet):

    def monthly_breakdown(self):

        return (
            self.annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(total=Sum('amount'))
            .order_by('-month')
        )

    def total_spent(self):
        return self.aggregate(total=Sum('amount'))['total'] or 0.0

    def total_expenses_for_the_current_year(self):
        current_year = timezone.now().year
        return self.filter(created_at__year=current_year).total_spent()

    def total_expenses_for_the_current_month(self):
        current_month = timezone.now().month
        return self.filter(created_at__month=current_month).total_spent()


class Expense(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[positive_float_validators])
    created_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE)

    objects = ExpenseQuerySet.as_manager()

    def __str__(self):
        return f"${self.amount} - {self.category}"



class Category(models.Model):
    name = models.CharField(choices=ExpenseCategoryChoices.choices, default=ExpenseCategoryChoices.OTHER)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'





