from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),

    #homepageview.as_view()
    path('home/',views.HomePageView.as_view(),name='home'),

    #eventpageview
    #path('event/', views.EventPageView.as_view(), name='event'),
    # change password urls
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),

    #edit profile
    path('edit/', views.edit, name='edit'),
    #display list of all Events
    path('event/', views.EventListView.as_view(), name='event'),

    #display ProfileEditForm
    path('profile/', views.profile_display, name='profile'),

    #add event
    path('add_event/', views.add_event, name='add_event')

    #view profile
]
