from django.shortcuts import render,redirect



# Create your views here.

def index(request):
    return render(request, "index.html") # you can also give variables ,


 

def recipe(request):
    greeting = "Are you Hungry?"
    return render(request, "recipe.html", {"greeting": greeting}) 
    


 
def about(request):
    return render(request, "about.html") 



def services(request):
    return render(request, "services.html") 


def contact(request):
    return render(request, "contact.html") 





