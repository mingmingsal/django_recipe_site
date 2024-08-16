from django.db import models

# Create your models here.
MEASURE_UNIT_CHOICES={
        "mg":"milligram",
        "g":"gram",
        "kg":"kilogram",
        "mL":"milliliter",
        "L":"liter",
        "cup":"cup",
        "tbsp":"tablespoon",
        "tsp":"teaspoon",
        "pc": "piece"
    }

#One-to-Many relationship
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=200)
    recipe_description = models.CharField(max_length=128)
    pub_date = models.DateTimeField("date published")
    image = models.ImageField(blank=True,upload_to='post_pics')
    def __str__(self):
        return self.recipe_name
    def isVegan(self):
        for ingredient in self.ingredient_set.all():
            if ingredient.is_meat():
                return False
        return True
class Step(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    step_description = models.CharField(max_length=1024)

class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=100)
    measure_unit = models.CharField(max_length=4, choices=MEASURE_UNIT_CHOICES, default=MEASURE_UNIT_CHOICES["g"])
    amount = models.IntegerField(default=1)
    
    def __str__(self):
        return self.ingredient_name
    def is_meat(self): 
        meat_strings = ['pork','beef','sausage','chicken','hotdog','sausage','fish'] 
        #test if ingredient has a meat name in it
        if self.ingredient_name.lower() in meat_strings:
            return True
        else:
            return False

