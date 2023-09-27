from django.contrib import admin
from lessons.models import Product
from lessons.models import Course
from lessons.models import UserAccess


admin.site.register(Product)

admin.site.register(Course)

admin.site.register(UserAccess)
