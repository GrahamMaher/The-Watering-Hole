from django.urls import path
from .views import register, reservation_list, make_reservation, modify_reservation, cancel_reservation


urlpatterns = [
    path('register/', register, name='register'),
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations_make/', make_reservation, name='make_reservation'),
    path('reservations/modify/<int:reservation_id>', modify_reservation, name='modify_reservation'),
    path('register/cancel/<int:reservation_id>', cancel_reservation, name='cancel_reservation'),
]