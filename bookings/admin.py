from django.contrib import admin
from .models import Table, Reservation

# Register your models here.
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats')
    search_fields = ('number',)


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('user', 'table', 'date', 'time', 'number_of_guests', 'created_at')
    list_filter = ('date', 'time')
    search_fields = ('user__username', 'table__number')
    ordering = ('date', 'time')


admin.site.register(Table, TableAdmin)
admin.site.register(Reservation, ReservationAdmin)
