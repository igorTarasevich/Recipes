from django.contrib import admin

from main.models import UnitsModel, ProductsModel, UnitsRatio, RecipesModel, IngredientsModel, StoreModel, \
    StoreProductModel

admin.site.register(UnitsModel)
admin.site.register(ProductsModel)
admin.site.register(UnitsRatio)
admin.site.register(RecipesModel)
admin.site.register(IngredientsModel)
admin.site.register(StoreModel)
admin.site.register(StoreProductModel)



