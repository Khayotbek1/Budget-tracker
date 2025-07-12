from django.contrib import admin
from .models import *

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'source', 'date')

class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'source', 'date')

admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
