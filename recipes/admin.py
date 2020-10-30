from django.contrib import admin

from .models import Recipe, Ingredient, Tag, IngredientInRecipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "author")
    list_filter = ("author", 'name', 'tags')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "dimension")
    list_filter = ("name",)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ("ingredient", 'number')


class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "value")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
admin.site.register(Tag, TagAdmin)
