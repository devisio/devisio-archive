from tastypie import fields
from tastypie.resources import ModelResource, ALL_WITH_RELATIONS

from devisio.journals.models import Journal, JournalSection


class JournalSectionResource(ModelResource):
    class Meta:
        queryset = JournalSection.objects.all()
        include_resource_uri = False
        resource_name = 'journal/section'


class JournalResource(ModelResource):
    sections = fields.ToManyField(JournalSectionResource, attribute=lambda bundle: JournalSection.objects.filter(journal=bundle.obj), full=True)

    def dehydrate(self, bundle):
        bundle.data['author'] = bundle.obj.author

        return bundle

    class Meta:
        queryset = Journal.objects.all()
        filtering = {'sections': ALL_WITH_RELATIONS}
