from django.contrib import admin

# Customizing Django Admin
class CustomAdminSite(admin.AdminSite):
    site_header = "🌸 Munira's Custom Admin"
    site_title = "Munira Admin Portal"
    index_title = "Welcome to Custom Dashboard"

    class Media:
        css = {
            "all": ("admin/css/custom_admin.css",)  # ✅ points to static file
        }

admin.site = CustomAdminSite()
