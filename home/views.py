from django.shortcuts import render,redirect

from django.http import JsonResponse

from .models import Recipe

# Create your views here.

def index(request):
    return render(request, "index.html") # you can also give variables ,


def recipe_search(request):
    if request.method == 'POST':
        query = request.POST.get('message', '')
        recipes = Recipe.objects.filter(title__icontains=query)

        print(recipes);
  
        params = {"recipes": recipes}

        return render(request, 'recipe_search.html', params)

    else:
        return render(request, 'recipe_search.html' )
 



def recipe(request):
    greeting = "What would you prefer to eat?"


    return render(request, "recipe.html", {"greeting": greeting}, ) 
    


 
def about(request):
    return render(request, "about.html") 



def services(request):
    return render(request, "services.html") 


def contact(request):
    return render(request, "contact.html") 





