from django.views.generic import ListView

from devisio.boxes.models import Box


class BoxListView(ListView):
    model = Box
