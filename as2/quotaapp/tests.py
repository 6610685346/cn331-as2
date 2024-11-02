from django.test import TestCase
from .models import Course, Student, Subject
from django.contrib.auth.models import User


class QuotaappTestCase(TestCase):

    def setUp(self):
        # create subject
        subject1 = Subject.objects.create(
            subject_id="CN331", subject_name="SOFTWARE ENGINEER")
        Course.objects.create(course=subject1, semester="1", year="1",
                              seat=1, current_seat=0, q_status="Available", status=True)

    def test_seat_available(self):
        """ is_seat_available should be True """

        course = Course.objects.first()

        self.assertTrue(course.is_seat_available())

    def test_seat_not_available(self):
        """ is_seat_available should be False """

        user1 = User.objects.create(username=6610685049, password="Test1234")
        student1 = Student.objects.create(student=user1)

        course = Course.objects.first()
        course.student_apply.add(student1)

        self.assertFalse(course.is_seat_available())
