from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.
class UsersManagersTests(TestCase):
    
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='freddy@g.com', password = 'iloveme123')
        self.assertEqual(user.email, 'freddy@g.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            # username is None for the AbstractUser option
            # username does not exist for the AbstractBaseUser option
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password="foo")
