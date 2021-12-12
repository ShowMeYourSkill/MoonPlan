from MoonPlanApp.models import Activity, CATEGORIES, Groups
from django import forms
from django.contrib.admin.templatetags.admin_list import search_form
from django.forms import ModelForm


class AddActivityForm(ModelForm):
    class Meta:
        model = Activity
        fields ='__all__'

class AddGroupForm(ModelForm):
    class Meta:
        model = Groups
        fields = '__all__'





    # theme = forms.CharField(max_length=100, label="Nazwa")
    # description = forms.CharField(max_length=100, label="Opis")
    # category = forms.ChoiceField(
    #     choices=CATEGORIES, label="Category", widget=forms.RadioSelect
    # )

    #class Meta:
        #model = search_form
    #year_of_birth = forms.IntegerField(min_value=1900, max_value=2023)