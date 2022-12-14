from django.shortcuts import render
from .models import sites,Person
# Create your views here.
def dynamicfunc(request):
    obj=sites.objects.all()
    obj2 = Person.objects.all()
    return render(request,'index.html',{'res' : obj,'res2':obj2})