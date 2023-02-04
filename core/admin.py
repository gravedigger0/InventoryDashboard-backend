from .models import *
# import pandas as pd
# from django.http import HttpResponseRedirect
# from django.urls import reverse, path
from django.contrib import admin


#     # Save the processed data to the database
    

# class PartAdmin(admin.ModelAdmin):

#     def process_csv_data(self, request, queryset):
#         if request.POST.get('post'):
#             csv_file = request.FILES['csv_file']
#             df = pd.read_csv(csv_file)
#             for i, row in df.iterrows():
#                 part_no = row['part_no']
#                 vehicle_name = row['vehicle_name']
#                 bike_model = row['bike_model']
#                 description = row['description']
#                 mrp = row['mrp']
#                 group = row['group']
#                 common_name = row['common_name']
#                 rack_location = row['rack_location']
#                 rack_city = row['rack_city']

#                 # check if vehicle exists
#                 try:
#                     vehicle = Vehicle.objects.get(name=vehicle_name)
#                 except Vehicle.DoesNotExist:
#                     vehicle = Vehicle.objects.create(name=vehicle_name)

#                 # check if bike exists
#                 try:
#                     bike = Bike.objects.get(model=bike_model)
#                 except Bike.DoesNotExist:
#                     bike = Bike.objects.create(model=bike_model)

#                 # check if rack exists
#                 try:
#                     city = City.objects.get(name=rack_city)
#                 except City.DoesNotExist:
#                     city = City.objects.create(name=rack_city)

#                 try:
#                     rack = Rack.objects.get(location=rack_location, city=city)
#                 except Rack.DoesNotExist:
#                     rack = Rack.objects.create(location=rack_location, city=city)

#                 # check if part exists, update it if it does, create it if it doesn't
#                 try:
#                     part = Part.objects.get(part_no=part_no)
#                     part.vehicle = vehicle
#                     part.bike = bike
#                     part.description = description
#                     part.mrp = mrp
#                     part.group = group
#                     part.common_name = common_name
#                     part.rack = rack
#                     part.save()
#                 except Part.DoesNotExist:
#                     part = Part.objects.create(part_no=part_no, vehicle=vehicle, bike=bike, description=description, mrp=mrp, group=group, common_name=common_name, rack=rack)


#     actions = [process_csv_data,]
#     process_csv_data.short_description = "Process CSV data from Excel and save to database"

#     def get_urls(self):
#         urls = super().get_urls()
#         custom_urls = [
#             path('process_csv/', self.admin_site.admin_view(self.process_csv_data), name='process_csv'),
#         ]
#         return custom_urls + urls


admin.site.register(Part)
admin.site.register(City)
admin.site.register(Rack)
admin.site.register(Vehicle)