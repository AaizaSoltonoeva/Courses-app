from rest_framework import serializers
from .models import *


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'imgpath',)


class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ('latitude', 'longitude', 'address',)


class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('type', 'value',)


class CourseSerializers(serializers.ModelSerializer):
    branches = BranchSerializers(many=True, required=False)
    contacts = ContactSerializers(many=True, required=False)

    class Meta:
        model = Course
        fields = ('id', 'category', 'name', 'description', 'logo', 'branches', 'contacts')

    def create(self, validate_data):
        contacts = validate_data.pop('contacts')
        branches = validate_data.pop('branches')
        course = Course.objects.create(**validate_data)

        for contact in contacts:
            Contact.objects.create(course=course, **contact)
        for branch in branches:
            Branch.objects.create(course=course, **branch)

        return course