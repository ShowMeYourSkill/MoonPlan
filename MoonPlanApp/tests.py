import pytest
from models import Activity
from django.contrib.auth import authenticate
from django.urls import reverse
from django.test import Client
from django.contrib.auth.models import User



#def test_first():
    #assert 2 + 2 == 5


@pytest.mark.django_db
def test_create_activity(client):
    """
    Test AddActivityView view.
    :param client: Django Client() object.
    :return: Assert if User model object is correctly created, and redirect to all object view.
    """
    assert Activity.objects.count() == 0
    post_data = {
        'theme': 'Test_theme',
        'description': 'Test_description',
        'category': '1',
    }
    response = client.post(reverse('all_view'), post_data)
    assert response.status_code == 302
    assert Activity.objects.count() == 1
    assert Activity.objects.first().theme == post_data['login']


def test_login_view(client):
    """
        Test members/login_user view.
        :param client: Django Client() object.
        :return: Asser if user is correctly logged-in and view redirects to next url.
    """
    assert User.objects.count() == 0
    User.objects.create_user(username='Test_user', password='Test_password')
    assert User.objects.count() == 1
    post_data = {
        'username': 'Test_user',
        'password': 'Test_password'
    }
    response = client.post(reverse('login/login'), post_data)
    assert response.status_code == 302
    assert authenticate(username='Test_user', password='Test_password')