from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from treebeard.mp_tree import MP_Node
from django_tenants.models import TenantMixin, DomainMixin

class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

    def getCategoryList():
        data = Category.dump_bulk()
        return data

    def getCategory(id):
        get = lambda node_id: Category.objects.get(pk=node_id)
        return get(id)

    def deleteCategory(id):
        try:
            node = Category.getCategory(id)
            node.delete()
            return True
        except:
            return False

    def moveCategory(id, parentId):
        try:
            node = Category.getCategory(id)
            try:
                parentId = Category.getCategory(parentId)
                node.move(parentId, 'sorted-child')
            except ObjectDoesNotExist as e: 
                root_node = Category.get_last_root_node()
                node.move(root_node, 'sorted-sibling')
        except:
            return False

    def to_json(self):
        return {'name': self.name}

    def __str__(self):
        return self.name

    def __unicode__(self):
        return 'Category: %s' % self.name


class Client(TenantMixin):
    name = models.CharField(max_length=100)
    paid_until =  models.DateField()
    on_trial = models.BooleanField()
    created_on = models.DateField(auto_now_add=True)

    # default true, schema will be automatically created and synced when it is saved
    auto_create_schema = True

class Domain(DomainMixin):
    pass        
