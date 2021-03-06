import unittest
from django.urls import reverse
from django.test import Client
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_todo(**kwargs):
    defaults = {}
    defaults["text"] = "text"
    defaults["complete"] = "complete"
    defaults.update(**kwargs)
    return Todo.objects.create(**defaults)


class TodoViewTest(unittest.TestCase):
    '''
    Tests for Todo
    '''
    def setUp(self):
        self.client = Client()

    def test_list_todo(self):
        url = reverse('todo_todo_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_todo(self):
        url = reverse('todo_todo_create')
        data = {
            "text": "text",
            "complete": "complete",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_todo(self):
        todo = create_todo()
        url = reverse('todo_todo_detail', args=[todo.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_todo(self):
        todo = create_todo()
        data = {
            "text": "text",
            "complete": "complete",
        }
        url = reverse('todo_todo_update', args=[todo.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)