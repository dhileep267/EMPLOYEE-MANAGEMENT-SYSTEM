
from django.contrib import admin
from .models import Department, Employee


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'designation',
        'salary',
        'joinin_date',
        'manager',
        'is_active',
    )

    list_filter = ('manager', 'is_active')
    search_fields = ('first_name', 'last_name', 'email')
    list_editable = ('is_active', 'salary')
    ordering = ('id',)

    @admin.display(description='Full name')
    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
