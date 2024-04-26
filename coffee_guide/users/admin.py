from django.contrib import admin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
    )
    search_fields = ("username",)
    list_filter = ("username",)
    empty_value_display = "-пусто-"
