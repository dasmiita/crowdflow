from django.urls import path
from .views import SlotListView

urlpatterns = [
    path('', SlotListView.as_view(), name='slot-list'),
]