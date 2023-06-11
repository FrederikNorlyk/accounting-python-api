import csv
import random
import datetime

from django.contrib.auth.models import User

from accounting.models.expense import Expense
from accounting.models.project import Project
from accounting.models.merchant import Merchant

class DemoDataUtil:
    '''Utility for creating demo data for a user'''

    def __init__(self) -> None:
        self.projects_names = self.get_rows('projects.csv')
        self.merchant_names = self.get_rows('merchants.csv')
        self.expenses = self.get_rows('expenses.csv')
        self.expense_amounts = self.get_rows('expenses.csv', column=1)

    def create_demo_data(self, user: User):
        '''Create random expenses, merchants, and projects for the given user'''
        
        for name in self.projects_names:
            Project.objects.create(
                name=name,
                user=user
            )

        for name in self.merchant_names:
            Merchant.objects.create(
                name=name,
                user=user
            )
        
        projects = Project.objects.filter(user_id=user.id)
        merchants = Merchant.objects.filter(user_id=user.id)

        i = 0
        for note in self.expenses:
            Expense.objects.create(
                date=self.random_date(),
                note=note,
                amount=self.expense_amounts[i],
                project=projects[random.randrange(0, projects.count() - 1)],
                merchant=merchants[random.randrange(0, merchants.count() - 1)],
                user=user
            )
        
            i += 1

    def get_rows(self, filename: str, column = 0):
        '''Gets all rows in the given csv file'''

        with open(f'accounting/data/{filename}', encoding="utf-8") as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            rows = []

            for row in csv_reader:
                    rows.append(row[column])

            return rows

    def random_date(self):
        '''Create a random date, no further than one year ago'''

        max_date = datetime.date.today()
        min_date = max_date - datetime.timedelta(days=365)

        delta = max_date - min_date
        random_days = random.randrange(delta.days)
        return min_date + datetime.timedelta(days=random_days)