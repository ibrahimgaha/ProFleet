from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView
from .forms import CustomUserCreationForm, CustomLoginForm
from .models import CustomUser


def landing_page(request):
    """
    Landing page view - accessible to all users.
    """
    return render(request, 'users/landing.html')


def auth_page(request):
    """
    Modern authentication page with tab switching between login and register.
    """
    return render(request, 'users/auth.html')


class CustomLoginView(LoginView):
    """
    Custom login view using our custom form.
    """
    form_class = CustomLoginForm
    template_name = 'users/login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        user = self.request.user
        if user.is_client():
            return '/dashboard/client/'
        elif user.is_driver():
            return '/dashboard/driver/'
        elif user.is_clearance_agent():
            return '/dashboard/clearance-agent/'
        elif user.is_admin_user():
            return '/dashboard/admin/'
        else:
            return '/dashboard/'


def register_view(request):
    """
    User registration view with role selection.
    """
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            user_type = form.cleaned_data.get('user_type')
            messages.success(request, f'Account created for {username} as {user.get_user_type_display()}!')

            # Automatically log in the user after registration
            login(request, user)

            # Redirect based on user role
            if user.is_client():
                return redirect('client_dashboard')
            elif user.is_driver():
                return redirect('driver_dashboard')
            elif user.is_clearance_agent():
                return redirect('clearance_agent_dashboard')
            elif user.is_admin_user():
                return redirect('admin_dashboard')
            else:
                return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard_view(request):
    """
    Main dashboard view that redirects users based on their role.
    """
    user = request.user

    if user.is_client():
        return render(request, 'users/client_dashboard.html', {'user': user})
    elif user.is_driver():
        return render(request, 'users/driver_dashboard.html', {'user': user})
    elif user.is_clearance_agent():
        return render(request, 'users/clearance_agent_dashboard.html', {'user': user})
    elif user.is_admin_user():
        return render(request, 'users/admin_dashboard.html', {'user': user})
    else:
        # Fallback for any undefined user types
        return render(request, 'users/default_dashboard.html', {'user': user})


@login_required
def client_dashboard(request):
    """
    Client-specific dashboard view.
    """
    if not request.user.is_client():
        messages.error(request, 'Access denied. You do not have permission to view this page.')
        return redirect('dashboard')

    return render(request, 'users/client_dashboard.html', {'user': request.user})


@login_required
def driver_dashboard(request):
    """
    Driver-specific dashboard view.
    """
    if not request.user.is_driver():
        messages.error(request, 'Access denied. You do not have permission to view this page.')
        return redirect('dashboard')

    return render(request, 'users/driver_dashboard.html', {'user': request.user})


@login_required
def clearance_agent_dashboard(request):
    """
    Clearance Agent-specific dashboard view.
    """
    if not request.user.is_clearance_agent():
        messages.error(request, 'Access denied. You do not have permission to view this page.')
        return redirect('dashboard')

    return render(request, 'users/clearance_agent_dashboard.html', {'user': request.user})


@login_required
def admin_dashboard(request):
    """
    Admin-specific dashboard view.
    """
    if not request.user.is_admin_user():
        messages.error(request, 'Access denied. You do not have permission to view this page.')
        return redirect('dashboard')

    # Get some basic statistics for admin
    total_users = CustomUser.objects.count()
    clients = CustomUser.objects.filter(user_type=CustomUser.CLIENT).count()
    drivers = CustomUser.objects.filter(user_type=CustomUser.DRIVER).count()
    clearance_agents = CustomUser.objects.filter(user_type=CustomUser.CLEARANCE_AGENT).count()
    admins = CustomUser.objects.filter(user_type=CustomUser.ADMIN).count()

    context = {
        'user': request.user,
        'total_users': total_users,
        'clients': clients,
        'drivers': drivers,
        'clearance_agents': clearance_agents,
        'admins': admins,
    }

    return render(request, 'users/admin_dashboard.html', context)
