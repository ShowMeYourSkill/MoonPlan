from django.contrib.auth.decorators import login_required
from django.views import View
from requests import request

from .models import *
from django.shortcuts import render, redirect
from .forms import AddActivityForm


class CategoryView(View):
    """shows all added Categories"""
    def get(self, request):
        return render(request, "base.html")



def AddActivityView(request):
    """(POST) for add registration activities"""
    form = AddActivityForm
    if request.method == 'POST':
        #print('Printing Post:', request.POST)
        form = AddActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_view')

    context = {'form': form}
    return render(request, 'add_theme.html', context)

def ActivitiesView(request):
    """Shows all users' available activities"""
    activities = Activity.objects.all()

    return render(request, 'categories.html', {'activities': activities})

@login_required
def GroupsView(request):
    """Shows all users' available Groups"""
    grupy = Groups.objects.all()

    return render(request, 'categorie.html', {'grupy': grupy})



















    # def get(self, request):
    #     form = AddActivityForm()
    #     ctx = {"form": form}
    #     return render(request, "add_theme.html", ctx)
    #
    # def post(self, request):
    #     form = AddActivityForm(request.POST)
    #     if form.is_valid():
    #         theme = form.cleaned_data["theme"]
    #         description = form.cleaned_data["description"]
    #         category = form.cleaned_data["category"]
    #         form = Activity.objects.create(
    #             theme=theme,
    #             description=description,
    #             category=category,
    #         )
    #         return redirect("index", Activity_id=theme.id)
    #     #theme_id=theme.id
