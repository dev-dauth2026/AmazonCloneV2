from django.urls import path
from .views import SignUpView,LoginView,LogoutView,PasswordForgotView,PasswordResetView
from accounts.views import ProfileAccountView



app_name='accounts'
urlpatterns = [
  
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('passwordforgot/', PasswordForgotView.as_view(), name='passwordforgot'),
    path("password-reset/<email>/<token>/",PasswordResetView.as_view(), name="passwordreset"),
    path("profile-account",ProfileAccountView.as_view(), name="profile-account"),

]
