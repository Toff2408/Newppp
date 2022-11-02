from django.urls import path
from .views import *
urlpatterns = [ 
    path('',index,name='index'),
    path('products',products,name='products'),
    path('signin',signin,name='signin'),
    path('signout',signout,name='signout'),
    path('signup',signup,name='signup'),
    path('categories',categories,name ='categories'),
    path('singlecategory/<str:id>',singlecategory,name ='singlecategory'),
    path('details/<str:id>',details,name='details'),
    path('shopcart',shopcart,name='shopcart'),

]


