from django.test import TestCase
from django.contrib.auth.models import User
from accounting.models.expense import Expense
from accounting.utils.demo_data_util import DemoDataUtil

class DemoDataUtilTest(TestCase):
    '''Test for DemoDataUtil'''

    def test_create(self):
        '''Test that all entries in the csv files are created'''

        User.objects.create(username='Test user', password='123')
        user = User.objects.all()[0]
        
        util = DemoDataUtil()
        util.create_demo_data(user)

        expenses = Expense.objects.all()
        for e in expenses:
            print(e)

