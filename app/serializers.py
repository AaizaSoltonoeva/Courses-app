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

    def create(self, validated_data):
        contacts_data = {}
        branches_data = {}

        if 'contacts' in validated_data:
            contacts_data = validated_data.pop('contacts')
        if 'branches' in validated_data:
            branches_data = validated_data.pop('branches')

        course = Course.objects.create(**validated_data)

        for branch_data in branches_data:
            branch = Branch.objects.create(course=course, **branch_data)
        for contact_data in contacts_data:
            contact = Contact.objects.create(course=course, **contact_data)
        return course
