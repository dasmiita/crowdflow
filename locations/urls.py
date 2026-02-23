from django.urls import path
from .views import TempleListView

urlpatterns = [
    path('', TempleListView.as_view(), name='temple-list'),
]