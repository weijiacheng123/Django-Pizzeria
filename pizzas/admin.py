from django.contrib import admin

# Register your models here.
from pizzas.models import Image, Pizza, Topping, Comment

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Comment)
admin.site.register(Image)