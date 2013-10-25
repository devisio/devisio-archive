from django.views.generic import ListView, DetailView, TemplateView

from devisio.common.pjax import PJAXResponseMixin
from devisio.journals.models import Journal


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
    pass
