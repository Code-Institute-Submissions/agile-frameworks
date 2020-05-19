from django.test import TestCase


class TestViews(TestCase):

    def test_get_packages(self):
        response = self.client.get('/packages/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'packages/packages.html')

    def test_get_package_management(self):
        response = self.client.get('/package_management/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'package/package_management.html')
