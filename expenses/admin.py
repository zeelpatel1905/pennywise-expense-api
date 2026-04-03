from django.contrib import admin
from .models import Category, Expense

# Option 1: Simple registration
admin.site.register(Category)

# Option 2: Advanced registration (shows more info in the table)
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'date', 'category', 'user')
    list_filter = ('date', 'category')
    search_fields = ('title', 'description')