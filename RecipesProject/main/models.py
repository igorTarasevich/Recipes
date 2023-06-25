from django.db import models


class UnitsModel(models.Model):
    name = models.CharField(max_length=150)
    short_name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class ProductsModel(models.Model):
    name = models.CharField(max_length=150)
    unit = models.ForeignKey(UnitsModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.name


class UnitsRatio(models.Model):
    unit_one = models.ForeignKey(UnitsModel, on_delete=models.PROTECT, related_name='unit_one')
    unit_two = models.ForeignKey(UnitsModel, on_delete=models.PROTECT, related_name='unit_two')
    ratio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.unit_one.name} = {self.ratio} {self.unit_two.name}'


class RecipesModel(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name


class IngredientsModel(models.Model):
    recipe = models.ForeignKey(RecipesModel, on_delete=models.PROTECT, default=None, null=True)
    product = models.ForeignKey(ProductsModel, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.ForeignKey(UnitsModel, on_delete=models.PROTECT)
    description = models.TextField(max_length=1000)

    def __str__(self):
        return f'{self.product.name} ({self.recipe.name})'


class StoreModel(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class StoreProductModel(models.Model):
    product = models.ForeignKey(ProductsModel, on_delete=models.PROTECT, default=None, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    actual_date = models.DateField(auto_now=True)
    is_available = models.BooleanField()
    store = models.ForeignKey(StoreModel, on_delete=models.PROTECT, default=None, null=True)
    unit = models.ForeignKey(UnitsModel, on_delete=models.PROTECT)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.product.name} {self.price}/{self.amount} {self.unit} {self.store.name}'


