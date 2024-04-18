from django.contrib import admin
from django.utils.html import format_html
from . import models

admin.site.register(models.Location)


class TypeAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


admin.site.register(models.Breed, TypeAdmin)
admin.site.register(models.Process_type, TypeAdmin)
admin.site.register(models.Transportation_mode, TypeAdmin)
admin.site.register(models.Organisation_type, TypeAdmin)


class ProcessAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "organisation",
        "date",
        "type",
        "transportation_mode",
        "entity",
    )
    list_filter = (
        "organisation",
        "date",
        "type",
        "transportation_mode",
        "entity",
    )
    search_fields = ("name", "organisation")


class CattleProcessAdmin(ProcessAdmin):
    list_display = (
        "name",
        "description",
        "location",
        "organisation",
        "date",
        "type",
        "transportation_mode",
        "entity",
        "organic",
    )
    list_filter = (
        "organisation",
        "date",
        "type",
        "transportation_mode",
        "entity",
        "organic",
    )


admin.site.register(models.Cattle_process, CattleProcessAdmin)
admin.site.register(models.Product_process, ProcessAdmin)


class CattleAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
        "location",
        "organisation",
        "birth_date",
        "breed",
    )
    list_filter = ("organisation", "breed")
    search_fields = ("name",)
    fieldsets = (
		("Boi Data", {"fields": ("name", "description", "breed", "birth_date")}),
		("Localisation", {"fields": ("location", "organisation")})
	)


admin.site.register(models.Cattle, CattleAdmin)


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "location", "type", "registration_date")
    list_filter = ("type",)
    search_fields = ("name",)


admin.site.register(models.Organisation)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "cattle", "location", "date_added", "QRcode")
    list_filter = ( "cattle",)
    search_fields = ("name", )
    fieldsets = (
		("Boi Data", {"fields": ("name", "description", "cattle")}),
		("Localisation", {"fields": ("location",)})
	) 
    
    def QRcode(self, obj):
        return format_html(
            f'<button><a href="http://127.0.0.1:8000/qrcode/{obj.pk}">View</a></button>'
        )
    
    
admin.site.register(models.Product, ProductAdmin)