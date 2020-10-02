from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request, 'index.html')

@csrf_exempt
def add(request):
    response_data = {}

    val1 = float(request.POST.get('number1', 0.0))
    val2 = float(request.POST.get('number2', 0.0))
    result = val1 + val2
    response_data['Number 1'] = val1
    response_data['Number 2'] = val2
    response_data['Operation'] = "Add"
    response_data['Result'] = result

    return JsonResponse(response_data)

