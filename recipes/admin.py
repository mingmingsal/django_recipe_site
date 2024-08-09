
from django.contrib import admin

from .models import Recipe, Step, Ingredient

class IngredientInLine(admin.TabularInline):
    model = Ingredient
    extra = 1
class StepInLine(admin.StackedInline):
    model = Step
    extra = 1
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["recipe_name"]}),
        ("Date Information", {"fields":["pub_date"]}),
        ("Recipe Description", {"fields":["recipe_description"]})
    ]
    inlines = [IngredientInLine, StepInLine]
admin.site.register(Recipe, RecipeAdmin)