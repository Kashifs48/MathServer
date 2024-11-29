from django.contrib import admin 
from django.urls import path 
from skapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('areaofrectangle/',views.rectarea,name="areaofrectangle"),
    path('',views.rectarea,name="areaofrectangleroot")
]
