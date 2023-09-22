from django.urls import path
from app.views import itemlist,locationlist
from app.views import itemdetails,locationdetails


from django.urls import path
urlpatterns = [ 
   path('items/',itemlist.as_view()),
   path('location/',locationlist.as_view()),
   path('items/<int:pk>/',itemdetails.as_view()),
   path('location/<int:pk>/',locationdetails.as_view())
   
]
