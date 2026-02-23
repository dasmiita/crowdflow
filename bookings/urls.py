from django.urls import path
from .views import BookingView, TokenVerificationView

urlpatterns = [
    path('', BookingView.as_view(), name='booking'),
    path('verify/', TokenVerificationView.as_view(), name='verify-token'),
]