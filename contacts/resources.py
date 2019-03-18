from tastypie.resources import ModelResource
from contacts.models import Person
from tastypie.authorization import Authorization


class PersonResource(ModelResource):
    class Meta:
        queryset = Person.objects.all()
        resource_name = 'person'
        authorization = Authorization()
