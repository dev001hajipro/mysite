from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

# テスト用データベースは、`python manage.py runserver`の時と違うので
# 最初はデータがない。

class ContactModelTests(TestCase):
    pass

class ContactIndexViewTests(TestCase):
    def test_no_data(self):
        print(reverse('news:list'))
        res = self.client.get(reverse('news:list'))
        self.assertEqual(res.status_code, 200)
        print(res.context)
        self.assertQuerysetEqual(res.context['contact_list'], [])
    
