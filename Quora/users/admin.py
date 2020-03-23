from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser

# Use custom class avoid using modding Django Direct
class CustomUserAdmin(UserAdmin):
    """ Here we want to add our custom
    fields to the model here direct
    see inline comments below:
    """
    # Example Fields
    # add_form = 
    # form = 
    model = CustomUser
    list_display = ["username", "email", "is_staff"]

# Register The New Custom Class
admin.site.register(CustomUser, CustomUserAdmin)