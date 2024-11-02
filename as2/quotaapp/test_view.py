from django.test import TestCase, Client
from django.urls import reverse
from django.db.models import Max
from .models import Subject, Course, Student
from django.contrib.auth.models import User


class QuotaappViewTestCase(TestCase):

    def setUp(self):
        # create subject
        subject1 = Subject.objects.create(
            subject_id="CN331", subject_name="SOFTWARE ENGINEER")

        Course.objects.create(course=subject1, semester="1", year="1",
                              seat=9999, current_seat=1, q_status="Available", status=True)
        user = User.objects.create_user(
            username=6610685049, password="Test1234")
        Student.objects.create(student=user)

    def test_index_view_status_code(self):
        """ index view's status code is ok """

        c = Client()
        response = c.get(reverse('quotaapp:index'))
        self.assertEqual(response.status_code, 200)

    def test_complete_view_status_code(self):
        """ complete view's status code is OK """

        c = Client()
        response = c.get(reverse('quotaapp:complete'))
        self.assertEqual(response.status_code, 200)

    def test_can_login(self):
        """ correct username and password should return status code 200 """

        c = Client()
        c.post(reverse('users:login'), {
               'username': "6610685049", 'password': "Test1234"})
        response = c.get(reverse('users:index'))
        self.assertEqual(response.status_code, 200)

    def test_cannot_login(self):
        """ wrong username and password should return 302 """
        c = Client()
        c.post(reverse('users:login'), {
               'username': "6610685050", 'password': "Test1234"})
        response = c.get(reverse('users:index'))
        self.assertEquals(response.status_code, 302)
