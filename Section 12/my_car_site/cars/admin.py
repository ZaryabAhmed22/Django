from django.contrib import admin
from cars.models import Car

# Register your models here.

# admin.site.register(Car)

#ModelNameAdmin
class CarAdmin(admin.ModelAdmin):
  #fields = ['year', 'brand'] #order of fields

  #field sets/ field segmenting
  fieldsets= [('TIME INFORMATION', {'fields': ['year']}), ('CAR INFORMATION', {'fields': ['brand']})]

admin.site.register(Car, CarAdmin)