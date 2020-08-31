from django.contrib import admin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

from .models import Employees, DeptManager
 

# Register your models here.

class DisplayEmployee(admin.ModelAdmin):
    list_display = ('emp_no', 'first_name', 'last_name', 'birth_date', 'gender', 'hire_date')
    search_fields = ['first_name'] # first_name으로 검색
    list_filter = ('gender', ('birth_date', DateRangeFilter))
    ordering = ('last_name', 'hire_date')


admin.site.register(Employees, DisplayEmployee)

admin.site.register(DeptManager)