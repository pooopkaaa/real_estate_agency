from django.contrib import admin

from .models import Flat
from .models import Complaint
from .models import Owner


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ['owners_phonenumber', 'owner_pure_phone', 'address', 'price', 'new_building', 'construction_year', 'town']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']


class ComplaintAdmin(admin.ModelAdmin):
    raw_id_fields = ['flat', 'user']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['property_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)