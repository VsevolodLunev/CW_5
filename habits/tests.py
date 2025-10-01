from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        pass

    def test_owner_can_list_habits(self):
        pass

    def test_owner_can_list_nice_habits(self):
        pass

    def test_regular_user_can_list_habits(self):
        pass
