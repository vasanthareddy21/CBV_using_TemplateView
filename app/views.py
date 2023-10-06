from django.shortcuts import render

# Create your views here.

from app.forms import *
from django.views.generic import TemplateView
from django.http import HttpResponse

class Temp(TemplateView):
    template_name='Temp.html'
    def get_context_data(self,**args):
        ECDO=super().get_context_data(**args)
        #ECDO['name']='Vasantha'
        ECDO['SFO']=StudentForm
        return ECDO
    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Data is inserted succesfully')


