from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

'''
def hello(request) :
    html = "<h1>Hello, Django</h1>"
    return HttpResponse(html)
'''

def hello(request) :
    people = {'name' : 'dk', 'age' : 20}
    return render(request, 'simple/hello.html', {'data' : people})
