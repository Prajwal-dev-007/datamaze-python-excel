
from django.http import JsonResponse
from .models import Person
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Count, Q
import json




@csrf_exempt
def add_row(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the JSON data from the request
            # Create a new object in the database
            new_row = Person.objects.create(**data)
            return JsonResponse({'status': 'success', 'id': new_row.id})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request'}, status=400)


def get_total_cv_count(request):
    if request.method == 'GET':
        total_cvs = Person.objects.values('contact').distinct().count()  # Count unique contacts
        return JsonResponse({'total_cvs': total_cvs})

def get_full_data(request):
    if request.method == 'GET':
        data = list(Person.objects.values())  # Fetch all columns for all rows
        return JsonResponse(data, safe=False)


def get_all_data(request):
    if request.method == 'GET':
        data = list(Person.objects.values('source', 'client', 'SPOC', 'skill', 'name', 'contact', 'Remarks'))
        return JsonResponse(data, safe=False)


def get_remarks(request):
    if request.method == 'GET':
        remarks = Person.objects.values_list('Remarks', flat=True).distinct()
        return JsonResponse(list(remarks), safe=False)

def get_skill(request):
    if request.method == 'GET':
        skill = Person.objects.values_list('skill', flat=True).distinct()
        return JsonResponse(list(skill), safe=False)

def get_data_by_client(request):
    if request.method == 'GET':
        client_name = request.GET.get('client')
        remarks = request.GET.get('remarks')
        
        if client_name:
            filters = {'client__icontains': client_name}
            if remarks:
                filters['Remarks'] = remarks

            data = list(Person.objects.filter(**filters).values('source','client', 'SPOC', 'skill', 'name', 'contact', 'Remarks'))
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse({'error': 'Enter the client name'}, status=400)




def get_filtered_data(request):
    client = request.GET.get('client', '')
    remarks = request.GET.get('remarks', '')
    skill = request.GET.get('skill', '')

    # Start with all records
    queryset = Person.objects.all()

    # Apply filters only if the respective value is provided
    if client:
        queryset = queryset.filter(client__icontains=client)  # Case-insensitive partial match
    if remarks:
        queryset = queryset.filter(Remarks__icontains=remarks)  # Case-insensitive partial match for remarks
    if skill:
        queryset = queryset.filter(skill__icontains=skill)  # Case-insensitive partial match for skill

    # Check if queryset is empty
    if not queryset.exists():
        return JsonResponse({'message': 'No data found'}, status=200)

    # Return the filtered data as JSON
    data = list(queryset.values('source', 'client', 'SPOC', 'skill', 'name', 'contact', 'Remarks'))
    return JsonResponse(data, safe=False)

"""
def get_unique_contacts_count(request):
    if request.method == 'GET':
        column = request.GET.get('column')
        value = request.GET.get('value')
        
        # Ensure both column and value are provided
        if column and value:
            # Map of allowed columns and their exact model field names
            allowed_columns = {
                 'Remarks': 'Remarks', 
                 'source': 'source', 
                 'client': 'client', 
                 'skill': 'skill',
                 'SPOC' : 'SPOC'
            }
            
            # Make sure the column exists in allowed_columns
            if column in allowed_columns:
                # Filter based on the correct field name in the model
                filter_kwargs = {allowed_columns[column]: value}
                
                # Count unique contacts associated with the filtered rows
                unique_contacts_count = Person.objects.filter(**filter_kwargs).values('contact').distinct().count()
                return JsonResponse({'unique_contacts_count': unique_contacts_count})
            else:
                return JsonResponse({'error': 'Invalid column'}, status=400)
        return JsonResponse({'error': 'Missing column or value parameter'}, status=400)



"""
from django.http import JsonResponse
from urllib.parse import unquote

def get_unique_contacts_count(request):
    if request.method == 'GET':
        # Get multiple filter values from the request
        client = request.GET.get('client')
        skill = request.GET.get('skill')
        spoc = request.GET.get('SPOC')
        remarks = request.GET.get('Remarks')
        source = request.GET.get('source')

        # Prepare filter kwargs dynamically
        filter_kwargs = {}
        if client:
            filter_kwargs['client'] = unquote(client)
        if skill:
            filter_kwargs['skill'] = unquote(skill)
        if spoc:
            filter_kwargs['SPOC'] = unquote(spoc)
        if remarks:
            filter_kwargs['Remarks'] = unquote(remarks)
        if source:
            filter_kwargs['source'] = unquote(source)

        # Filter by the provided criteria and count unique contacts
        if filter_kwargs:
            unique_contacts_count = Person.objects.filter(**filter_kwargs).values('contact').distinct().count()
            return JsonResponse({'unique_contacts_count': unique_contacts_count})
        else:
            return JsonResponse({'error': 'No valid filters provided'}, status=400)
