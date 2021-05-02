from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request,*args, **kwargs):
    print(args,kwargs)
    print(request)
    print(request.user)
    #return HttpResponse("<h1>Hello World</h1>")
    return render(request,'home.html',{})
def contact_view(request,*args,**kwargs):
    
    #return HttpResponse("contact Page")
    return render(request,'contact.html',{})

def about_view(request,*args,**kwargs):
    my_context = {
        "my_text" : " This is about Us",
        "my_number" : 123973127,
        "my_list" : [12,213,1331,213,]
    }
    #return HttpResponse("contact Page")
    return render(request,'about.html',my_context)