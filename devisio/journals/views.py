from django.views.generic import ListView, TemplateView

from devisio.journals.models import Journal


class JournalsTeaserView(TemplateView):
    template_name = 'journals/journal_teaser.html'


class JournalsListView(ListView):
    model = Journal
