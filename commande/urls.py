from django.urls import path
from.views import homeview

urlpatterns = [
path('commande',homeview.as_view(),name='home'),
]