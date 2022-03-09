from django.test import TestCase,SimpleTestCase
from .models import MyUser
from django.db.models import Count
from django.contrib.auth.models import (
    AnonymousUser,
    Group,
    Permission,
    User,
    UserManager,
)

class MyUserTest(TestCase):
	def test_values(self):
		user=MyUser.objects.create(name='Prachi',email='kalpesh@gmail.com',is_active=True,is_admin=True)
		self.assertEquals(user.email,'kalpesh@gmail.com')
		self.assertEquals(user.is_admin,True)

	def test_empty_username(self):
		with self.assertRaisesMessage(ValueError, "The given username must be set"):
			User.objects.create_user(username="")

	def test_create_user_is_staff(self):
		email = "normal@normal.com"
		user = User.objects.create_user("user", email, is_staff=True)
		self.assertEqual(user.email, email)
		self.assertEqual(user.username, "user")
		self.assertTrue(user.is_staff)

	def test_create_super_user_raises_error_on_false_is_superuser(self):
		with self.assertRaisesMessage(ValueError, "Superuser must have is_superuser=True."):
			User.objects.create_superuser(username="test",email="test@test.com",password="test",is_superuser=False,)

	def test_create_superuser_raises_error_on_false_is_staff(self):
		with self.assertRaisesMessage(ValueError, "Superuser must have is_staff=True."):
			User.objects.create_superuser(username="test",email="test@test.com",password="test",is_staff=False,)

	def test_create_user(self):
		user = User.objects.create_user(username="test",email='normal@user.com',password='foo',is_active=True,)
		assert user.email == 'normal@user.com'



class GroupTests(SimpleTestCase):
    def test_str(self):
        g = Group(name="Users")
        self.assertEqual(str(g), "Users")


