from djangular.views.crud import NgCRUDView

from devisio.journals.models import Journal


class JournalCRUDView(NgCRUDView):
    model_class = Journal
