from django.views.generic import TemplateView

from devisio.common.pjax import PJAXResponseMixin


class AboutView(PJAXResponseMixin, TemplateView):
    template_name='devisio/about.html'


class ContactView(PJAXResponseMixin, TemplateView):
    template_name='devisio/contact.html'


class ImprintView(PJAXResponseMixin, TemplateView):
    template_name='devisio/imprint.html'
