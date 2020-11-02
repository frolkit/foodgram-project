from django.contrib import admin

from .models import Recipe, Ingredient, Tag, IngredientInRecipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "author")
    list_filter = ("author", 'title', 'tags')


class IngredientAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "dimension")
    list_filter = ("title",)


class IngredientInRecipeAdmin(admin.ModelAdmin):
    list_display = ("ingredient", 'number')


class TagAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "value")


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(IngredientInRecipe, IngredientInRecipeAdmin)
admin.site.register(Tag, TagAdmin)
