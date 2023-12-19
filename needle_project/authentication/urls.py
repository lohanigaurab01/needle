from django.urls import path
from authentication import views
from django.contrib.auth import views as auth_Views
from authentication.forms import CustomPasswordResetForm

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('setting/', views.setting_change, name='setting'),
    path('change-password/', auth_Views.PasswordChangeView.as_view(template_name='change-password.html'), name='change_password'),
    path('change-password-done/', auth_Views.PasswordChangeDoneView.as_view(template_name='change-password-done.html'), name='change_password_done'),

    path('password-reset/', auth_Views.PasswordResetView.as_view(template_name='password-reset.html', form_class=CustomPasswordResetForm), name='password_reset'),

    path('password-reset-send/', auth_Views.PasswordResetDoneView.as_view(template_name='password-reset-send.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', auth_Views.PasswordResetConfirmView.as_view(template_name='password-reset-set.html'),name='password_reset_confirm'),

    path('password-reset-done/', auth_Views.PasswordResetCompleteView.as_view(template_name='password-reset-done.html'), name='password_reset_complete'),

]
