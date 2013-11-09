from django.views.generic import TemplateView

from devisio.common.pjax import PJAXResponseMixin


class GoogleVerification(TemplateView):
    template_name='common/google_verification.html'


class AboutView(PJAXResponseMixin, TemplateView):
    template_name='common/about.html'


class ContactView(PJAXResponseMixin, TemplateView):
    template_name='common/contact.html'


class ImprintView(PJAXResponseMixin, TemplateView):
    template_name='common/imprint.html'
