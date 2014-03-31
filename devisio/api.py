from tastypie.api import Api

from devisio.journals.api import JournalResource


api1 = Api(api_name='v1')
api1.register(JournalResource)
