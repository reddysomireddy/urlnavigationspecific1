from django.shortcuts import render

# Create your views here.
def a1_first(request):
    return render(request,'hai.html')

def a1_second(request):
    return render(request,'hello.html')   