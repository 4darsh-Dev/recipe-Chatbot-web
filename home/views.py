from django.shortcuts import render,redirect

from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, "index.html") # you can also give variables ,


def process_message(request):
    if request.method == 'GET':
        message = request.GET.get('message')
    elif request.method == 'POST':
        message = request.POST.get('message')

    # process and manage response

    
    if message is not None:
        if message == 'Yes':

            response = {
                'title': "Recipe",
                'desc':"This is your recipe\nEnjoy",

            }
    else:
        response = {
            'message': 'Invalid message received',
        }

    return JsonResponse(response)
    # return responser
 

def recipe(request):
    greeting = "Are you Hungry?"
    


    return render(request, "recipe.html", {"greeting": greeting}, ) 
    


 
def about(request):
    return render(request, "about.html") 



def services(request):
    return render(request, "services.html") 


def contact(request):
    return render(request, "contact.html") 





