
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')

def show(request):
    return render(request,'show.html')

def edit(request):
    return render(request,'edit.html')

def delete(request):
    return render(request,'delete.html')

# def edit(request):
#     sample_text = "زر موقعي على https://example.com وشوف التفاصيل"
#     return render(request, 'students/edit.html', {'my_text': sample_text})

    
# Create your views here.from django.shortcuts import render

# def home(request):
#     sample_text = "زر موقعي على https://example.com وشوف التفاصيل"
#     return render(request, 'students/home.html', {'my_text': sample_text})
