from django.conf.urls import url
from loginpage import views

urlpatterns = [
    url(r'^main/', views.loginpage_view),
    url(r'^login/', views.login_view, name='login_view_board'),
    url(r'^signup/', views.signup_view, name='signup_view_board'),
    url(r'signup_result/', views.signup, name='signup'),
    url(r'login_result/', views.login, name='login')
]