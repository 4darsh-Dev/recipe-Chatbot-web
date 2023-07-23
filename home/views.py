from django.shortcuts import render,redirect

from django.http import JsonResponse

from .models import Recipe
# Create your views here.

def index(request):
    return render(request, "index.html") # you can also give variables ,


def recipe_results(request):
    if request.method == 'POST':
        query = request.POST.get('message', '')
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()
    
    context = {
        'recipes': recipes,
        'query': query if request.method == 'POST' else '',
    }
    


    return render(request, 'recipe_search.html', context)
 

def recipe(request):
    greeting = "Are you Hungry?"

    

    return render(request, "recipe.html", {"greeting": greeting}, ) 
    


 
def about(request):
    return render(request, "about.html") 



def services(request):
    return render(request, "services.html") 


def contact(request):
    return render(request, "contact.html") 





