from django.shortcuts import render
from django.views import View
from .models import Project, AIProject


class ProjectsIndexView(View):
    def get(self, request):
        projects = Project.objects.all()
        ai_projects = AIProject.objects.all()
        context = {'projects': projects,
                   'ai_projects': ai_projects,
                   }
        return render(request, 'projects/projects_index.html', context)


class ProjectDetailsView(View):
    def get(self, request, pk, project_type):
        project_type = project_type.replace('-', ' ')
        if project_type == 'Machine Learning':
            project = AIProject.objects.get(pk=pk)
        else:
            project = Project.objects.get(pk=pk)
        context = {'project': project}
        return render(request, 'projects/project_details.html', context)
