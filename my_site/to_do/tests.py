from django.test import TestCase
from django.urls import reverse


# Create your tests here.
class TestToDo(TestCase):

    def test_index(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='to_do/index.html')


    def test_post_task(self):
        response = self.client.get(reverse('add_task'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='to_do/add_task.html')