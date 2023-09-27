#from django.shortcuts import render
from rest_framework import generics
from.models import Course, UserAccess, Product
from.serializers import CourseSerializer, ProductSerializer

class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        user = self.request.user
        user_accesses = UserAccess.objects.filter(user=user)
        course_ids = [ua.course_id for ua in user_accesses]
        courses = Course.objects.filter(id__in=course_ids)
        return courses

class CourseListByProduct(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        product_id = self.kwargs['pk']
        user = self.request.user
        user_accesses = UserAccess.objects.filter(user=user, course__product_id=product_id)
        course_ids = [ua.course_id for ua in user_accesses]
        courses = Course.objects.filter(id__in=course_ids)
        return courses

class ProductStats(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        products = Product.objects.all()
        for product in products:
            product.viewers_count = UserAccess.objects.filter(course__product=product, is_viewed=True).count()
            product.total_duration = UserAccess.objects.filter(course__product=product).aggregate(Sum('course__duration'))['course__duration__sum']
            product.students_count = UserAccess.objects.filter(course__product=product).count()
            product.percent = round(product.viewers_count / product.students_count * 100, 2)
        return products