from django.contrib import admin

# expense/admin.py
from django.contrib import admin
from .models import Expense, Category


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    # 1. Columns to show in the list view table
    list_display = ('id', 'category', 'amount', 'created_at')

    # 2. Filters on the right sidebar (super helpful for expenses!)
    list_filter = ('category', 'created_at')

    # 3. Quick date navigation hierarchy at the top
    date_hierarchy = 'created_at'

    # 4. Sorting defaults (newest expenses first)
    ordering = ('-created_at',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)