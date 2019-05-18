from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^login',views.LoginView.as_view()),  # /user/login
    url(r'^register',views.RegisterView.as_view()),  #user/register
]