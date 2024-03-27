from django.shortcuts import render
from django.http import HttpResponse
from .models import departments,doctors
# Create your views here.


def index(request):

    # person = {
    #     'name' : 'Aje',
    #     'age' : 20,
    #     'profession':'programmer'
    # }

    numbers = {
        'num1':-10,
        
    }
    return render(request,'index.html',numbers)

def about(request):
    return render(request,'about.html')

def booking(request):
    return render(request,'booking.html')

def contact(request):
    return render(request,'contact.html')

def doctor(request):
    dict_docs = {
        'docs':doctors.objects.all()
    }
    return render(request,'doctor.html',dict_docs)

def department(request):
    dict_dept = {
        'dept':departments.objects.all()
    }
    return render(request,'department.html', dict_dept)