from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from etl.models import CsvData


class CsvDataTest(TestCase):
    def test_create_user(self):
        user_dict = {}
        user_dict['username'] = "test_user"
        user_dict['email'] = "test@test.test"
        User.objects.create(**user_dict)

        self.assertEqual(
            User.objects.all().count(),1
        )

    def test_model(self):
        model_dict = {}
        model_dict['name'] = "hari shyam"
        model_dict['ipv4'] = "192.168.2.132"
        model_dict['mac_address'] = "B2:QW:34:23:RE:4R"
        CsvData.objects.create(**model_dict)
        #modelname.***
        self.assertEqual(
            CsvData.objects.all().count(),1
        )