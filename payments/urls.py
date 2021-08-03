from django.urls import path

from .views import (HomePageView,  SuccessView, CancelledView,
            stripe_config, create_checkout_session)

app_name="payments"

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('config/', stripe_config, name='config'),
    path('create-checkout-session/', create_checkout_session, name='create_checkout_session'),
    path('success/', SuccessView.as_view(), name="success"), # new
    path('cancelled/', CancelledView.as_view(), name="cancel"), # new
]