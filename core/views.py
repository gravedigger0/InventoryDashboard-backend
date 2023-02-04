from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
import pandas as pd
from django.shortcuts import render, redirect
import csv

def import_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        df = pd.read_csv(csv_file)
        #get city_name from request
        city_name = request.POST['city_name']
        #get city object
        city = City.objects.get(name=city_name)
        # Loop through each row of the dataframe and create a new Rack object



        # Loop through each row of the dataframe and create a new Part object
        for index, row in df.iterrows():
            rack = Rack.objects.get_or_create(city=city, location=row['Rack Location'], part_no=row['Part No'])
            rack.save()

            part_no = row['Part No']

            existing_part = Part.objects.filter(part_no=part_no).first()

            if existing_part:
                existing_part.rack.add(row['vehicle'])
                existing_part.save()
            part = Part.objects.get_or_create(
                part_no=row['Part No'],
                description=row['Part Description'],
                mrp=row['MRP'],
                category=row['Part Group (G1)'],
                sub_category=row['Common Name (G2)'],
                rack=rack,
                vehicle=row['vehicle'],
                barcode=row['barcode']
            )
            part.save()
        return render(request, 'import_success.html')
            
        return redirect('/success/')
    return render(request, 'import_csv.html')


class PartViewSet(ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['vehicle__name', 'vehicle__variant']


class PartView(APIView):
    def get(self, request):
        queryset = Part.objects.all()
        serializer = PartSerializer(queryset, many=True)
        return Response(serializer.data)
    

class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubCategoryList(generics.ListAPIView):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer

class SubCategoryByCategory(generics.ListAPIView):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return SubCategory.objects.filter(category=category_id)
