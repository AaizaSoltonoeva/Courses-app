from rest_framework import generics
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView
from app.permissions import IsOwnerOrReadOnly


class CourseList(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CourseDetail(RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializers


class CategoryList(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class CategoryDetail(RetrieveDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class BranchList(ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


class BranchDetail(RetrieveDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializers


class ContactsList(ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers


class ContactsDetail(RetrieveDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializers

