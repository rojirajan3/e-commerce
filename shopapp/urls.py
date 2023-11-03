from django.urls import path
from shopapp import views

urlpatterns = [
    path('indexpage/',views.indexpage,name="indexpage"),
    path('addcat/',views.addcat,name="addcat"),
    path('catdb/',views.catdb,name="catdb"),
    path('dis/',views.dis,name="dis"), 
    path('edit/<int:dataid>/',views.edit,name="edit"),
    path('updatecate/<int:dataid>/',views.updatecate,name="updatecate"),  
    path('delete/<int:dataid>/',views.delete,name="delete"),
    path('addpro/',views.addpro,name="addpro"),
    path('prodb/',views.prodb,name="prodb"),
    path('disprod/',views.disprod,name="disprod"),
    path('updateprod/<int:dataid>/',views.updateprod,name="updateprod"),  
    path('editprod/<int:pro_id>/',views.editprod,name="editprod"),
    path('deletepro/<int:dataid>/',views.deletepro,name="deletepro"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_Login/',views.admin_Login,name="admin_Login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
   
]
