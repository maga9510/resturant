from django.contrib import admin
from organization.models import *



@admin.register(user)
class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "role")
    fields = ("name", "email", "role")

@admin.register(partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("first_name", "phone")

@admin.register(organizatsion)
class OrganizatsionAdmin(admin.ModelAdmin):
    list_display = ("name", "partner")

@admin.register(platform_user)
class PlatformUserAdmin(admin.ModelAdmin):
    list_display = ("organization", "full_name", "role")
    fields = ("organization", "full_name", "phone", "email", "role")

@admin.register(room)
class RoomUserAdmin(admin.ModelAdmin):
    list_display = ("name", "oraganizatsion_id")

@admin.register(organization_table)
class OrganizationTableUserAdmin(admin.ModelAdmin):
    list_display = ("number", "room_id")



