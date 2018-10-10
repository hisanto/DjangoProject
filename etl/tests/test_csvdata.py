from django.test import TestCase, Client
from django.urls import reverse


class CsvDataViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list_csvdata(self):
        url = reverse("csvdata_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_list_malformed_url(self):
        url = reverse("csvdata_create")
        response = self.client.get(url)
        self.assertEqual(response.status_code,404)


