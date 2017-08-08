from django.shortcuts import render,HttpResponse,redirect,HttpResponseRedirect
try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin=object

class SimpleMiddleware(MiddlewareMixin):
    def process_request(self,request):
        if 'user' not in request.session and request.path != '/login/' and request.path !='/admin/':
            HttpResponseRedirect('/login/')
        return None

    def process_response(self,request,response):
        return response
