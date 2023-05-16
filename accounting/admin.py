from django.contrib import admin
from .models.expense import Expense
from .models.project import Project


admin.site.register(Expense)
admin.site.register(Project)