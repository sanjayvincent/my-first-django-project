from django.shortcuts import render

# Create your views here.
def patient_list(request):
    return render(request, 'ehospital/patient_list.html', {})