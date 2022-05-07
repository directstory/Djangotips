from django.forms import model_to_dict
from django.http.response import JsonResponse
from userRole.models import *

# Create your views here.


def mtom(request):
    rf = RolesFearutes.objects.filter()
    return JsonResponse(model_to_dict(role))
