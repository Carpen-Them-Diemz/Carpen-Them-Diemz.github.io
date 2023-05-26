from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.BlogIndex.as_view(), name='blog_index'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('<category>/', views.BlogCategory.as_view(), name='blog_category'),
]
