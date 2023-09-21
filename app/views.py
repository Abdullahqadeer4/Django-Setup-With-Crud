from django.shortcuts import render

from django.http import HttpResponse

# def home(request):
#     return render(request,"app/index.html")


#Write all logical code here

def home(request):
     peoples=[
         {'name':"Abdul Rafay",'age':17},
         {'name':"Afraheem",'age':26},
         {'name':"Abdullah",'age':24},
         {'name':"Saif",'age':16},
         {'name':"Athar",'age':28}
         
     ]
     for people in peoples:
         print(people)
    #IF YOU WANT TO SEND DATA TO HTML PAGE, USE RENDER (Dynamic data)
    #For static data simply return httpresponse
     return render(request,"app/index.html",context={'peoples':peoples})
# Create your views here.

# def home(request):
#     return HttpResponse("<h1>Hey I am a Django Servver</h1>")
# # def list(request):
# #     list1=[1,2,3,4,5]
# #     return HttpResponse("this is a list",list1)
# def success(request):
#     return HttpResponse("Success")
def aboutus(request):
    return render(request,"app/aboutus.html")
def contact(request):
    return render(request,"app/contact.html")