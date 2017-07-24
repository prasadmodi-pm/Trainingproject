from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^sign-up/',views.signup,name='signup')

]