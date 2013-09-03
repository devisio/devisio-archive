from django.views.generic import ListView, TemplateView

from devisio.common.pjax import PJAXResponseMixin
from devisio.journals.models import Journal


class JournalsTeaserView(PJAXResponseMixin, TemplateView):
    template_name = 'journals/journal_teaser.html'


class JournalsListView(PJAXResponseMixin, ListView):
    model = Journal
