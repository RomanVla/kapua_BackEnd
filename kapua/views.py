from django.conf import settings
from django.db import utils
from django.views.generic import TemplateView
from django.http import HttpResponse, JsonResponse

from tenant_schemas.utils import remove_www

from testApp.models import Client, Category

def category_list(request):
    data = Category.dump_bulk()
    
    # json.dumps(data)
    return JsonResponse(data, safe=False)

def category_entity(request):
    id = request.GET.get('id', '')

    get = lambda node_id: Category.objects.get(pk=node_id)    
    node = get(id)

    return JsonResponse(node.to_json(), safe=False)

def category_addEntity(request):
    parentId = request.GET.get('parentId', '')
    name = request.GET.get('name', '')

    new_node = Category(name = name)
    get = lambda node_id: Category.objects.get(pk=node_id)
    node = get(parentId)
    node.add_child(instance=new_node)

    return JsonResponse(new_node.to_json(), safe=False)

def category_moveEntity(request):
    parentId = request.GET.get('parentId', '')
    id = request.GET.get('id', '')

    get = lambda node_id: Category.objects.get(pk=node_id)

    parentId = get(parentId)
    node = get(id)

    node.move(parentId, 'sorted-child')

    return JsonResponse('ok', safe=False)

def category_deleteEntity(request):
    id = request.GET.get('id', '')

    get = lambda node_id: Category.objects.get(pk=node_id)

    node = get(id)

    node.delete()

    return JsonResponse('ok', safe=False)


