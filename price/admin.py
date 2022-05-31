from django.contrib import admin

from price.models import Price, Symbol


class PriceAdmin(admin.ModelAdmin):
    list_filter = ("symbol", "created_at")
    list_display = ("symbol", "price", "created_at")
    search_fields = ("symbol__name", "price", "created_at")


class SymbolAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Price, PriceAdmin)
admin.site.register(Symbol, SymbolAdmin)
