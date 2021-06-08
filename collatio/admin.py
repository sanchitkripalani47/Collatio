from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from .models import *
# Register your models here.

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    exclude = ['id']

admin.site.register(Tag)
