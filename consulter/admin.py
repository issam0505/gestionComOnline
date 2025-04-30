from django.contrib import admin
from .models import category,produit
@admin.register(category)
class categoryadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(produit)
class produitAdmin(admin.ModelAdmin):
    list_display=('name','category','price','stock')
    list_filter=('category',)
    search_fields=('name','description')