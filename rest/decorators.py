from django.http import HttpResponse
from django.shortcuts import redirect

def unauthorized(view_func):
    def wrapperfunc(request,*args,*kwargs):
        return view_func(request,*args,*kwargs)
    return wrapperfunc
