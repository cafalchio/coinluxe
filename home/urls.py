from django.urls import path
from .views import IndexListView

urlpatterns = [
    path('', IndexListView.as_view(), name='home'),
]
