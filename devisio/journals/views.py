from django.views.generic import ListView, DetailView, TemplateView

from devisio.photos.utils import serialize_photos_json
from devisio.common.pjax import PJAXResponseMixin
from devisio.journals.models import Journal, JournalEntry


class JournalsTeaserView(PJAXResponseMixin, TemplateView):
    template_name = 'journals/journal_teaser.html'


class JournalsMapView(PJAXResponseMixin, ListView):
    model = Journal
    template_name = 'journals/journal_map.html'


class JournalsListView(PJAXResponseMixin, ListView):
    def get_queryset(self):
        return Journal.objects.get_valid()


class JournalsDetailView(PJAXResponseMixin, DetailView):
    model = Journal


class JournalEntryDetailView(PJAXResponseMixin, DetailView):
    model = JournalEntry
    template_name = 'photos/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(JournalEntryDetailView, self).get_context_data(**kwargs)
        context['json'] = serialize_photos_json(context['object'].photos.all())
        return context
