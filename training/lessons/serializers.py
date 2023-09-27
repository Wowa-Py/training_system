from rest_framework import serializers
from.models import Course, Product

class CourseSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    accesses = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'video_link', 'duration', 'owner', 'accesses']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name']
