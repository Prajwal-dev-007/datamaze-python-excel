"""
URL configuration for datamaze project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from home.views import *




urlpatterns = [
   
   

    path('admin/', admin.site.urls),
    path('api/', include('home.urls')),
    #path('importexcel/',importexcel, name='import-excel'),
    #path('get_processed_data/', get_processed_data, name='get_processed_data'),
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
