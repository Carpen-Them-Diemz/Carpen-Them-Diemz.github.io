from .views import ProjectsIndexView, ProjectDetailsView
from django.urls import path

app_name = 'projects'

urlpatterns = [
    path('', ProjectsIndexView.as_view(), name='projects_index'),
    path('<str:project_type>/<int:pk>/', ProjectDetailsView.as_view(), name='project_details'),
]
