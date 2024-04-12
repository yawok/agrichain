from django.contrib import admin
from . import models

admin.site.register(models.Cattle)
admin.site.register(models.Organisation)
admin.site.register(models.Product)
admin.site.register(models.Location)
admin.site.register(models.Cattle_process)
admin.site.register(models.Product_process)
admin.site.register(models.Process_type)
admin.site.register(models.Breed)
admin.site.register(models.Transportation_mode)
admin.site.register(models.Organisation_type)
