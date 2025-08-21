from django.shortcuts import render

from django.views.generic import View

from sheet1.forms import SheetForm


class DrNameCretae(View):

    def get(self,request,*args,**kwargs):

        form_instance=SheetForm()

        return render(request,"drsheet.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=SheetForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

        return render(request,"drsheet.html",{"form":form_instance})