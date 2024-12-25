from django.urls import path 
from .views import blog_single ,blog_home ,search
app_name='blog'

urlpatterns = [
    path('', blog_home,name='blog_home'),
    path('<int:id>/', blog_single,name='blog_single'),
    path('search/',search,name='search'),
    path('category/<str:cat_name>/',blog_home,name='category')
]