from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom user model that extends AbstractUser with role-based access control.
    """

    # User role choices
    CLIENT = 'client'
    DRIVER = 'driver'
    CLEARANCE_AGENT = 'clearance_agent'
    ADMIN = 'admin'

    USER_TYPE_CHOICES = [
        (CLIENT, 'Client'),
        (DRIVER, 'Driver'),
        (CLEARANCE_AGENT, 'Clearance Agent'),
        (ADMIN, 'Admin'),
    ]

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default=CLIENT,
        help_text='Select the user role/type'
    )

    # Additional fields can be added here in the future
    phone_number = models.CharField(
        max_length=15,
        blank=True,
        null=True,
        help_text='Contact phone number'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"

    def is_client(self):
        return self.user_type == self.CLIENT

    def is_driver(self):
        return self.user_type == self.DRIVER

    def is_clearance_agent(self):
        return self.user_type == self.CLEARANCE_AGENT

    def is_admin_user(self):
        return self.user_type == self.ADMIN

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
