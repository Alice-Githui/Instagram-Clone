from django.test import TestCase
from .models import Profile, Image, Comment

# Create your tests here.
class ProfileTestClass(TestCase):
    #setUp method
    def setUp(self):
        self.alice=Profile(profile_name="Alice", profile_photo="https://www.pexels.com/photo/person-holding-midnight-black-samsung-galaxy-s8-turn-on-near-macbook-pro-1092671/", bio="Person holding a galaxy phone")

    def test_instance(self):
        self.assertTrue(isinstance(self.alice, Profile))

    def test_save_method(self):
        self.alice.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_delete_profile(self):
        self.john=Profile(profile_name="John", profile_photo="https://www.pexels.com/photo/person-holding-phone-while-logging-in-on-instagram-application-174938/", bio="Man holding a phone")
        self.john.save_profile()

        profiles=Profile.objects.all()
        self.john.delete_profile()
        self.assertEqual(len(profiles), 0)


class CommentTestClass(TestCase):
    #setup method

    def setUp(self):
        self.commentone=Comment(comment="Great Picture")

    def test_instance(self):
        self.assertTrue(isinstance(self.commentone, Comment))

    def test_save_method(self):
        self.commentone.save_comment()
        comments=Comment.objects.all()
        self.assertTrue(len(comments) > 0)

    def test_delete_comment(self):
        self.commentone=Comment(comment="commentone")
        self.commentone.save_comment()

        comments=Comment.objects.all()
        self.commentone.delete_comment()
        self.assertEqual(len(comments),0)

class ImageTestClass(TestCase):
    #setUp method

    def setUp(self):
        self.alice=Profile(profile_name="Alice", profile_photo="https://www.pexels.com/photo/person-holding-phone-while-logging-in-on-instagram-application-174938/", bio="Cool Cat")
        self.alice.save_profile()

        self.commentone=Comment(comment="Great Picture")
        self.commentone.save_comment()

        self.imageone=Image(image="https://www.pexels.com/photo/person-holding-phone-while-logging-in-on-instagram-application-174938/", image_name="Log into IG", caption="Man holding phone to log in to IG", profile=self.alice, comments=self.commentone, likes=4)
        self.imageone.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.imageone, Image))

    def tearDown(self):
        Profile.objects.all().delete()
        Comment.objects.all().delete()
        Image.objects.all().delete()

    def test_save_image(self):
        self.imageone.save_image()
        images=Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_image(self):
        images=Image.objects.all()

        self.imageone.delete_image()
        self.assertEqual(len(images), 0)


    

