from tastypie.resources import ModelResource

from devisio.journals.models import Journal


class JournalResource(ModelResource):
    class Meta:
        queryset = Journal.objects.all()
        #resource_name = 'journal'
