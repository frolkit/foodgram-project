from django.contrib import admin

from .models import Favorite, Purchase, Subscribe


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "recipe")
    list_filter = ("user", "recipe")


class PurchareAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "recipe")
    list_filter = ("user", "recipe")


class SubscribeAdmin(admin.ModelAdmin):
    list_display = ("pk", "user", "following")
    list_filter = ("user", "following")


admin.site.register(Favorite, FavoriteAdmin)
admin.site.register(Purchase, PurchareAdmin)
admin.site.register(Subscribe, SubscribeAdmin)
