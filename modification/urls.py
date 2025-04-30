from django.urls import path
from.views import modificationview

urlpatterns = [
path('modification',modificationview.as_view(),name='modi'),
]