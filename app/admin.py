from django.contrib import admin
from .models import Flavor, Ingredient, CustomerSuggestion

# Register your models here.
admin.site.register(Flavor)
admin.site.register(Ingredient)
admin.site.register(CustomerSuggestion)
