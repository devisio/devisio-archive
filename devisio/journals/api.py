from tastypie.resources import ModelResource

from devisio.journals.models import Journal


class JournalResource(ModelResource):
    def dehydrate(self, bundle):
        bundle.data['author'] = bundle.obj.author

        return bundle

    class Meta:
        queryset = Journal.objects.all()
        #resource_name = 'journal'
