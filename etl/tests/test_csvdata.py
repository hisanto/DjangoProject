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
        self.assertEqual(response.status_code,200)

    def test_create_data(self):
        url = reverse("csvdata_create")
        data = {
            "name":"test",
            "ipv4":"192.167.4.3",
            "mac_address" :"23:23:we:33:23:df"
        }
        respo = self.client.post(url,data=data)
        self.assertEqual(respo.status_code,302)