# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()


urlpatterns = [
     # path('importexcel/', importexcel, name='import-excel'),
     # path('get_processed_data/', get_processed_data, name='get_processed_data'),
      path('get-data-by-client/', get_data_by_client, name='get_data_by_client'),
      path('get-remarks/', get_remarks, name='get_remarks'),
      path('get-skill/', get_skill, name='get_skill'),
      path('get-all-data/', get_all_data, name='get_all_data'),
      path('get-full-data/', get_full_data, name='get_full_data'),
      path('get-total-cv-count/', get_total_cv_count, name='get_total_cv_count'),
      path('add-row/', add_row,name='add_row'),
      path('get-filtered-data/', get_filtered_data, name='get_filtered_data'),
     path('get-unique-contacts-count/', get_unique_contacts_count, name='get_unique_contacts_count'),

    
]

