from django.urls import path
from . import views

urlpatterns=[
    path('',views.review,name="REVIEW"),
    path('thankyou',views.thankyou,name="THANK_YOU")
]