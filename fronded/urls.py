from django.urls import path
from fronded import views

urlpatterns  = [
    path('homepage/',views.homepage,name="homepage"),
    path('productpage/',views.productpage,name="productpage"),
    path('singleprod/<proid>',views.singleprod,name="singleprod"),
     path('filteredpage/<cat_name>/',views.filteredpage,name="filteredpage"),

]