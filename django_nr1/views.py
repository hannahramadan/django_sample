from django.http import HttpResponse
from django.shortcuts import render
import time, random

answer = 3 * 5

# Create your views here.
def index(request):
    return render(request, 'index.html')

def normal(request):
    return render(request, 'multiplication.html', {"answer": answer})

def slow(request):
    time.sleep(3)
    return render(request, 'multiplication.html', {"answer": answer})

def rand_error(request):
    error = random.randint(1,3)
    if error == 1:
            response = render(request, '404.html',)
            response.status_code = 404
            return response
    return render(request, 'multiplication.html', {"answer": answer})