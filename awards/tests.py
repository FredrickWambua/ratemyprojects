from awards.models import CustomUser, Project
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.test import TestCase


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
            User.objects.create_user(email='', password="iloveme123")

    def test_create_superuser(self):
            User = get_user_model()
            admin_user = User.objects.create_superuser(email='wambua@g.com', password='ihateyou123')
            self.assertEqual(admin_user.email, 'wambua@g.com')
            self.assertTrue(admin_user.is_active)
            self.assertTrue(admin_user.is_staff)
            self.assertTrue(admin_user.is_superuser)
            try:
                # username is None for the AbstractUser option
                # username does not exist for the AbstractBaseUser option
                self.assertIsNone(admin_user.username)
            except AttributeError:
                pass
            with self.assertRaises(ValueError):
                User.objects.create_superuser(
                    email='wambua@g.com', password='ihateyou123', is_superuser=False)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.test_user_project = CustomUser(username='fredricks')
        self.test_user_project.save()
        self.project_test = Project(title='UX/UI', description='For user experience and user interface, learn more')

    def test_instance(self):
        self.assertTrue(isinstance(self.project_test, Project))

    def test_save_project(self):
        self.project_test.save()
        projects = Project.objects.all()
        self.assertTrue(len(projects)>0)

    def test_delete_project(self):
        self.project_test.delete()
        projects = Project.objects.all()
        self.assertTrue(len(projects)<1)