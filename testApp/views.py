import copy
from django.http import JsonResponse
from rest_framework import status

from testApp.models import Category

def category_controller(request):

    get = lambda node_id: Category.objects.get(pk=node_id)

    if (request.method == 'GET'):        
        data = Category.getCategoryList()

        return JsonResponse(data, safe=False)
    elif (request.method == 'PATCH'):
        parentId = request.GET.get('parentId', 0)
        id = request.GET.get('id', '') 

        if (Category.moveCategory(id, parentId)):
            return JsonResponse(status.HTTP_201_CREATED, safe=False)
        else:
            return JsonResponse(status.HTTP_404_NOT_FOUND, safe=False)
    elif (request.method == 'DELETE'):        
        id = request.GET.get('id', 0)

        if(Category.deleteCategory(id)):
            return JsonResponse(status.HTTP_204_NO_CONTENT, safe=False)
        else:
            return JsonResponse(status.HTTP_404_NOT_FOUND, safe=False)
    else:

        return JsonResponse(status.HTTP_400_BAD_REQUEST, safe=False)
    


