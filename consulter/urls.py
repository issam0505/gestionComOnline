from django.urls import path
from.views import consulterview

urlpatterns = [
path('',consulterview.as_view(),name='consulter'),
]