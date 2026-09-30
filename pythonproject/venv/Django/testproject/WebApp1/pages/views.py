from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    #return HttpResponse("<h1>Hello, word!</h1> ")# обычный HTML-код
    return render(request, "home.html",{}) # в фигурных скобках указан контекст

def contact_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Contacts page!</h1> ")
    context={
        "my_text":"здесь пропишем любой текст",
        "my_number":1860681,
        "my_list":[1,2,3],
    }
    return render(request, "contact.html",context)

def about_view(request,*args, **kwargs):
    #return HttpResponse("<h1>About page!</h1> ")
    return render(request, "about.html",{})

def social_view(request,*args, **kwargs):
    #return HttpResponse("<h1>Social page!</h1> ")
    return render(request, "social.html",{})
