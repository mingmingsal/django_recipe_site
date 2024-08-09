import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Recipe,Ingredient,Step

#Helpers
def create_recipe(recipe_name, daysOffset, steps, ):

    time = timezone.now() + datetime.timedelta(days=daysOffset)
    return Recipe.objects.create(recipe_name=recipe_name, pub_date=time)

def create_step(step, recipe_name):
    return Step.objects.create(step_description=step, recipe=recipe_name)
def create_ingredient(ingredient, amount, measure_unit, recipe_name):
    return Step.objects.create(ingredient_name=ingredient, amount = amount, measure_unit = measure_unit, recipe=recipe_name)
#Model Tests
class RecipeModelTests(TestCase):
    def test_make_blank_recipe(self):
        time = timezone.now()
        recipe = Recipe(recipe_name="hotdog",pub_date=time)
        self.assertIs(recipe.recipe_name=="hotdog", True)
    def test_add_step(self):
        time = timezone.now()
        new_recipe = Recipe(recipe_name="hotdog",pub_date=time)
        new_step = Step(step_description="Steam bun",recipe=new_recipe)
        self.assertIs(new_step.recipe==new_recipe, True)
    def test_is_ingredient_meat(self):
        time = timezone.now()
        new_recipe = Recipe(recipe_name="hotdog",pub_date=time)
        new_ingredient = Ingredient(ingredient_name="Beef", measure_unit="g",amount=400,recipe=new_recipe)
        self.assertIs(new_ingredient.is_meat(), True)

# View Tests
"""
class IndexViewTests(TestCase):
    def test_step_add(self):
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No recipes are available.")
        self.assertQuerySetEqual(response.context["recipe)_list"], [])

class DetailsViewTests(TestCase):
    def test_step_add(self):
        recipe = create_recipe(question_text="Ice Cream Sundae.", days=0)
        step = create_step("Scoop Ice Cream",recipe)
        url = reverse("recipes:detail", args=(recipe.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

"""