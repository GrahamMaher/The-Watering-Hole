from django.contrib import admin
from .models import Table, Reservation, AdminUser , RestaurantSettings

# Register your models here.


admin.site.register(Table)

admin.site.register(Reservation)

admin.site.register(AdminUser )

admin.site.register(RestaurantSettings)