
from django.contrib import admin

from .models import Recipe, Step, Ingredient
from users.models import Profile

class IngredientInLine(admin.TabularInline):
    model = Ingredient
    extra = 1
class StepInLine(admin.StackedInline):
    model = Step
    extra = 1
class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{"fields":["recipe_name"]}),
        ("Food Image", {"fields":["author"]}),
        ("Food Image", {"fields":["image"]}),
        ("Date Information", {"fields":["pub_date"]}),
        ("Recipe Description", {"fields":["recipe_description"]})
    ]
    inlines = [IngredientInLine, StepInLine]
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
admin.site.register(Profile)