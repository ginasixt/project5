from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from capstone.models import Group, Activity
from datetime import datetime

class CreateActivity_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.create_activity_url = reverse('create_activity')

    def test_create_activity(self):
        response = self.client.post(self.create_activity_url, {
            'name': 'Test Activity'
        })
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(Activity.objects.filter(name='Test Activity').exists())


class JoinGroup_Test(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.activity = Activity.objects.create(name='Test Activity')
        self.group = Group.objects.create(
            name='Test Group', 
            activity=self.activity, 
            creator=self.user,
            time_and_date=datetime.now()  # Add this line
        )
        self.join_group_url = reverse('join_group', args=[self.group.id])
    def test_join_group(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.join_group_url)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect
        self.assertTrue(self.group.users.filter(username='testuser').exists())       