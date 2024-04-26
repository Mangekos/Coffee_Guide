from django.contrib import admin
# from django.forms import CheckboxSelectMultiple

from .models import (
    Address,
    # Additional,
    Cafe,
    Schedule,
    ScheduleInCafe,
    Roaster,
    Additionals,
    Drink,
    DrinkInCafe,
)


class ScheduleInCafeInline(admin.TabularInline):
    model = ScheduleInCafe
    extra = 1


class DrinkInCafeInline(admin.TabularInline):
    model = DrinkInCafe
    extra = 1


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'address', 'organization',)
    search_fields = ('name', 'organization__username')
    inlines = [ScheduleInCafeInline, DrinkInCafeInline]
        # (
        #     "Контакты и адреса",
        #     {"fields": (
        #         "address")},
        # ),
    # list_filter = ("name",)
    # empty_value_display = "-пусто-"
    # autocomplete_fields = ["cities"]

    # def preview(self, obj):
    #     """Отображение превью заведения"""
    #     if obj.poster:
    #         return mark_safe(
    #             f'<img src="{obj.poster.url}" style="max-height: 50px;">'
    #         )
    #     else:
    #         return "No preview"

    # preview.short_description = "Превью"


# @admin.register(ImageCafe)
# class ImageCafeAdmin(admin.ModelAdmin):
#     list_display = ("image_file", "image_url")


@admin.register(Roaster)
class RoasterAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Additionals)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")


@admin.register(Address)
class Address(admin.ModelAdmin):
    list_display = ("id", "name", "lat", "lon")


# @admin.register(Additional)
# class Additional(admin.ModelAdmin):
#     list_display = ("name", "slug")


@admin.register(ScheduleInCafe)
class ScheduleInCafeAdmin(admin.ModelAdmin):
    list_display = ("cafe", "schedules", "start", "end")


@admin.register(DrinkInCafe)
class DrinkInCafeAdmin(admin.ModelAdmin):
    list_display = ("id", "cafe", "drink", "cost")


# @admin.register(ImageCafe)
# class ImageAdmin(admin.ModelAdmin):
#     list_display = ("id", "image_file", "image_url")
