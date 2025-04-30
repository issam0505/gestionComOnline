from django.urls import path
from.views import signview,loginview
urlpatterns=[
    path('sign',signview.as_view(),name='hhkb'),
    path("login/",loginview.as_view(),name="login_page")
]