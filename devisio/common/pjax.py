class PJAXResponseMixin(object):
    def get_context_data(self, **kwargs):
        context = super(PJAXResponseMixin, self).get_context_data(**kwargs)
        if self.request.META.get('HTTP_X_PJAX', False):
            context['parent'] = 'pjax.html'
        else:
            context['parent'] = 'base.html'
        return context

