from django.shortcuts import render,redirect
from .models import destination
from .forms import destinationform,searchform
from django.http import JsonResponse

# Create your views here.

def td(request):
    err = ''
    message = ''
    message_class = ''
    if request.method == 'POST':
        form = destinationform(request.POST,request.FILES)
        if form.is_valid():
            Name = form.cleaned_data['name']
            Desc = form.cleaned_data['desc']
            if destination.objects.filter(name=Name).exists() : 
                err = 'Destination already added'
            elif destination.objects.filter(desc=Desc).exists() :
                err = 'Same description already given to a destination'
            else:
                instance = form.save(commit=False)
                instance.author = request.user
                instance.save()
        else:
            
            err = 'Invalid Submission,Try again'
            
        if err:
            message = err
            message_class = 'alert-danger'
        else:
            message = 'Destination added successfully'
            message_class = 'alert-success'
    else:
        form = destinationform()
    return render(request,'td.html',{'form':form,'message':message,'message_class':message_class})





def index(request):
    dests=destination.objects.all() 
    if request.method == 'POST':
        f = searchform(request.POST)
        if f.is_valid():
            search = f.cleaned_data['search']
            return redirect("https://www.tripadvisor.com/Search?q={}&searchSessionId=6DD58777B8F9F3EDEE92B346514F4E081590312503285ssid&searchNearby=false&sid=A9E123DF5AEF498DAE96FCDCECAC2AD61590312519030&blockRedirect=true".format(search))
    
    else:
        f = searchform()
        return render(request,'index.html',{'dests':dests,'f':f})

def about(request):
    return render(request,'about.html')

def news(request):
    return render(request,'news.html')

def check(request):
    sh = request.GET.get('sh',None)
    value = destination.objects.filter(name__iexact=sh).exists() 
    data = {
        'value': value 
    }
    return JsonResponse(data)





