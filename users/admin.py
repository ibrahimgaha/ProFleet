from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Custom admin interface for CustomUser model.
    """

    # Fields to display in the user list
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'is_staff', 'is_active', 'date_joined')

    # Fields to filter by in the admin sidebar
    list_filter = ('user_type', 'is_staff', 'is_active', 'date_joined', 'last_login')

    # Fields to search by
    search_fields = ('username', 'email', 'first_name', 'last_name', 'phone_number')

    # Fields to order by
    ordering = ('-date_joined',)

    # Add the custom fields to the user creation and editing forms
    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'phone_number')
        }),
    )

    # Fields to show when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Additional Info', {
            'fields': ('user_type', 'phone_number', 'email', 'first_name', 'last_name')
        }),
    )

    # Enable actions for bulk operations
    actions = ['make_active', 'make_inactive', 'make_client', 'make_driver', 'make_clearance_agent']

    def make_active(self, request, queryset):
        """Bulk action to activate users."""
        queryset.update(is_active=True)
        self.message_user(request, f"{queryset.count()} users have been activated.")
    make_active.short_description = "Mark selected users as active"

    def make_inactive(self, request, queryset):
        """Bulk action to deactivate users."""
        queryset.update(is_active=False)
        self.message_user(request, f"{queryset.count()} users have been deactivated.")
    make_inactive.short_description = "Mark selected users as inactive"

    def make_client(self, request, queryset):
        """Bulk action to set users as clients."""
        queryset.update(user_type=CustomUser.CLIENT)
        self.message_user(request, f"{queryset.count()} users have been set as clients.")
    make_client.short_description = "Set selected users as clients"

    def make_driver(self, request, queryset):
        """Bulk action to set users as drivers."""
        queryset.update(user_type=CustomUser.DRIVER)
        self.message_user(request, f"{queryset.count()} users have been set as drivers.")
    make_driver.short_description = "Set selected users as drivers"

    def make_clearance_agent(self, request, queryset):
        """Bulk action to set users as clearance agents."""
        queryset.update(user_type=CustomUser.CLEARANCE_AGENT)
        self.message_user(request, f"{queryset.count()} users have been set as clearance agents.")
    make_clearance_agent.short_description = "Set selected users as clearance agents"
