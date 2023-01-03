from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordResetForm, MySetPassword

urlpatterns = [
    #path('', views.home),
    path('', views.ProductView.as_view(), name='home'),

    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),


    #--Add-TO-Cart----------------------------------------------------------
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path("pluscart/", views.plus_cart),
    path("minuscart/", views.minus_cart),
    path("removecart/", views.remove_cart),
    #--CART DONE------------------------------------------------------------


    #CHECKOUT--------------------------------------------------------------
    path('checkout/', views.checkout, name='checkout'),

    path('paymentdone/', views.payment_done, name="paymentdone"),

    path('buy/', views.buy_now, name='buy-now'),

    #--profile Url----------------------------------
    path('profile/', views.ProfileView.as_view(), name='profile'),

    #--address Url--------------------------------------------------------------------------------------------------------
    path('address/', views.address, name='address'),

    path('orders/', views.orders, name='orders'),
    path('regular/', views.regular, name='regular'),
    path('regular/<slug:data>', views.regular, name='regulardata'),#for filter specific ittar and perfumes
    
    #path('login/', views.login, name='login'),<---FOR LOGIN--->
    path('accounts/login/', auth_views.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    #<---FOR LOGOUT--->
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
   
    #password change---------------------------------------------------------------------
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html', form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'), name='passwordchange'),
    path('passwordchangedone/', auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'), name='passwordchangedone'),
    #password change complete---------------------------------------------------------------------
    
    #password reset (forgot)----------------------------------------------------------------------
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='app/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='app/password_reset_confirm.html', form_class=MySetPassword), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='app/password_reset_complete.html'), name='password_reset_complete'),
    #password reset (forgot) complete ----------------------------------------------------------------------
    
    
    #--old registration-   path('registration/', views.customerregistration, name='customerregistration'),
   
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
