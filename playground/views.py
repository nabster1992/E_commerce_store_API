
from django.core.cache import cache
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging
from .tasks import notify_customers
import requests

logger = logging.getLogger(__name__) #playground.views

class HelloView(APIView):
    @method_decorator(cache_page(5 * 60))
    def get(self, request):
        try:
            logger.info('Calling httpbin')
            response = requests.get('https://httpbin.org/delay/2')
            data = response.json()
        except requests.ConnectionError:
            logger.critical('httpbin is offline')
        return render(request, 'emails/hello.html',{'name': 'Nab'})
    








 













# def say_hello(request):
#     try:  
#       message = BaseEmailMessage(
#          template_name='emails/hello.html',
#          context={'name': 'Nab'}
#       )
#       message.send(['john@nabbuy.com'])
#     except BadHeaderError:
#         pass
#     return render(request, 'hello.html', {'name': 'Nab'})



