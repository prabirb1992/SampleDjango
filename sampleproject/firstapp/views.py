from django.shortcuts import render
from django.views.generic import View


class Controller(View):
    def get(self,request):
        context={"name":"Prabir",
                 "surname":"Bhattacharya",
                 "address":"Dum Dum Cantonment",
                 "project":"Sample project"}
        return render(request,"home.html",context)

# Create your views here.
