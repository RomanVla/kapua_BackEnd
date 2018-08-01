from django.db import models
from django.utils import timezone
from treebeard.mp_tree import MP_Node

from django_tenants.models import TenantMixin, DomainMixin

class Category(MP_Node):
    name = models.CharField(max_length=30)

    node_order_by = ['name']

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
