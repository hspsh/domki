from django.contrib import admin
from app.models.apartment import Apartment


class ApartmentAdmin(admin.ModelAdmin):

    readonly_fields = ('uuid',)


admin.site.register(Apartment, ApartmentAdmin)
