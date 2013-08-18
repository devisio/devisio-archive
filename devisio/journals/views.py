from django.views.generic import ListView

from devisio.journals.models import Journal


class JournalsListView(ListView):
    model = Journal
