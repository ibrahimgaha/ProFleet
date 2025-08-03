from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    # Landing page
    path('', views.landing_page, name='landing'),
    
    # Authentication URLs
    path('auth/', views.auth_page, name='auth'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
    # Dashboard URLs
    path('dashboard/', views.dashboard_view, name='dashboard'),
    
    # Role-specific dashboard URLs
    path('dashboard/client/', views.client_dashboard, name='client_dashboard'),
    path('dashboard/driver/', views.driver_dashboard, name='driver_dashboard'),
    path('dashboard/clearance-agent/', views.clearance_agent_dashboard, name='clearance_agent_dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
]
