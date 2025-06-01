from django.shortcuts import render
from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.
'''
class StudentList(APIView):
    def get(self, request):
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.get_object(pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        '''
 #Mixins classes
    # ListModelMixin -> list() -> get()
    # CreateModelMixin -> create() -> post()
    # RetrieveModelMixin -> retrieve() -> get()
    # UpdateModelMixin -> update() -> put()
    # DestroyModelMixin -> destroy() -> delete()
'''
from rest_framework import mixins, generics
class StudentList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)

class StudentDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get(self, request, pk):
        return self.retrieve(request, pk=pk)

    def put(self, request, pk):
        return self.update(request, pk=pk)

    def delete(self, request, pk):
        return self.destroy(request, pk=pk)
'''
#Generics class based views
#CreateAPIView -> create() -> post()
# ListAPIView -> list() -> get()
# RetrieveAPIView -> retrieve() -> get()
# UpdateAPIView -> update() -> put()
# DestroyAPIView -> destroy() -> delete()
#ListCreateAPIView -> list() -> get(), create() -> post()
# RetrieveUpdateAPIView -> retrieve() -> get(), update() -> put()
# RetrieveDestroyAPIView -> retrieve() -> get(), destroy() -> delete()
# RetrieveUpdateDestroyAPIView -> retrieve() -> get(), update() -> put(), destroy() -> delete()
'''
from rest_framework import generics
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
'''
#viewsets
#ViewSet -> list(),create(),retrieve(),update(),delete()
#ModelViewSet -> list(),create(),retrieve(),update(),delete()

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination ,LimitOffsetPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class StuentPagination(PageNumberPagination):
    page_size = 2

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = LimitOffsetPagination # StuentPagination #pageNumberPagination
    #filter_backends = [DjangoFilterBackend]  # Use DjangoFilterBackend for filtering
    #filter_backends = [filters.SearchFilter]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name', 'score']  # Specify fields to filter by 
    ordering = ['name']  #Default ordering field
    #search_fields = ['^id', '^name']  # Specify fields to filter by 

# to filter 
# > pip install django-filter
#classes > django_filters.rest_framework.DjangoFilterBackend
#for configure Saerchfilter
    #>'^' : starts with
    #>'$' : Regex serch
    #>'@' : Full text search (currently only supported by PostgreSQL)
    #>'=' : Exact match