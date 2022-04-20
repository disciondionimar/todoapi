from rest_framework.test import APITestCase
from authentication.models import User

class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user('user', 'user@email.com', 'Password123!@')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'user@email.com' )

    def test_creates_superuser(self):
        user = User.objects.create_superuser('user', 'user@email.com', 'Password123!@')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'user@email.com' )

    def test_raises_error_when_no_username_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,username="", email="user@email.com", password="Password123!@")


    def test_raises_error_with_message_when_no_username_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(username='', email='user@email.com', password='Password123!@')        
    
    def test_raises_error_when_no_email_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,username="user", email="", password="Password123!@")

    def test_raises_error_with_message_when_no_email_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(username='user', email='', password='Password123!@')
    
    def test_raises_error_when_superuser_is_staff_is_false(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(username='admin', email='admin@email.com', password='Password123!@', is_staff=False)
    
    def test_raises_error_when_superuser_is_superuser_is_false(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(username='admin', email='admin@email.com', password='Password123!@', is_superuser=False)

