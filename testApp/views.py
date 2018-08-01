import copy
from rest_framework.response import Response
from rest_framework import status, serializers

from django.conf import settings
from django.db import utils
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import ObjectDoesNotExist

from tenant_schemas.utils import remove_www

from testApp.models import Category

# def category_list(request):
#     data = Category.dump_bulk()
#     return JsonResponse(data, safe=False)

# def category_entity(request):
#     id = request.GET.get('id', 0)

#     get = lambda node_id: Category.objects.get(pk=node_id)    
#     node = get(id)

#     return JsonResponse(node.to_json(), safe=False)

# def category_add(request):
#     parentId = request.GET.get('parentId', 0)
#     name = request.GET.get('name', '')

#     new_node = Category(name = name)
#     try:
#         get = lambda node_id: Category.objects.get(pk=node_id)   
#         node = get(parentId)
#         node.add_child(instance=new_node)
#     except DoesNotExist as e:        
#         new_node = Category.add_root(instance=new_node)

#     return JsonResponse(new_node.to_json(), safe=False)

# def category_move(request):
#     response = Response()

#     if (request.method != 'PATCH'):
#         return

#     parentId = request.GET.get('parentId', 0)
#     id = request.GET.get('id', '')

#     get = lambda node_id: Category.objects.get(pk=node_id)

#     parentId = get(parentId)
#     node = get(id)

#     node.move(parentId, 'sorted-child')

#     return JsonResponse('ok', safe=False)

# def category_delete(request):

#     print(request.method)
#     if (request.method == 'DELETE'):
#         id = request.GET.get('id', 0)
#         get = lambda node_id: Category.objects.get(pk=node_id)
#         node = get(id)
#         node.delete()
#     else:
#         return JsonResponse(status.HTTP_400_BAD_REQUEST, safe=False)
    


def category_controller(request):

    get = lambda node_id: Category.objects.get(pk=node_id)
    print(request.method)

    if (request.method == 'GET'):
        data = Category.dump_bulk()

        return JsonResponse(data, safe=False)        
    elif (request.method == 'PATCH'):
        parentId = request.GET.get('parentId', 0)
        id = request.GET.get('id', '') 

        node = get(id)        
        try:
            parentId = get(parentId)
            node.move(parentId, 'sorted-child')
        except ObjectDoesNotExist as e: 
            new_node = copy.copy(node)
            print(new_node)
            print(node)
            root_node = Category.get_last_root_node()            
            root_node.add_sibling('sorted-sibling', instance=new_node)
            node.delete()

        return JsonResponse(status.HTTP_201_CREATED, safe=False)
    elif (request.method == 'DELETE'):
        id = request.GET.get('id', 0)

        node = get(id)
        node.delete()

        return JsonResponse(status.HTTP_204_NO_CONTENT, safe=False)
    else:

        return JsonResponse(status.HTTP_400_BAD_REQUEST, safe=False)
    


