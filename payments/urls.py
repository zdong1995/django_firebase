from django.urls import path

from . import views

urlpatterns = [
    path('customer', views.customers),
    path('customer/add', views.add_customer),
    path('charge', views.charge),
    path('charge/add', views.add_charge),
    path('transaction', views.transaction),
    path('card', views.card),
    path('card/add', views.add_card),
    path('card/default', views.default_card),
    path('card/list', views.list_cards),
    path('refund', views.refund),
    path('refund/add', views.add_refund)
]