from wagtail_modeladmin.options import ModelAdmin, modeladmin_register
from .models import Contact

class ContactAdmin(ModelAdmin):
    model = Contact
    menu_label = "Contacts"  # A more descriptive name for the menu item
    menu_icon = "mail"  # Choose an appropriate icon
    list_display = ("name", "email")
    search_fields = ("name", "email")

modeladmin_register(ContactAdmin)
