from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views as authviews
from accounting.auth.custom_auth_token import CustomAuthToken

from accounting.views.expense_view_set import ExpenseViewSet
from accounting.views.merchant_view_set import MerchantViewSet
from accounting.views.project_view_set import ProjectViewSet
from accounting.views.user_view_set import UserViewSet


router = routers.DefaultRouter()
router.register(r'expenses', ExpenseViewSet, 'expense')
router.register(r'projects', ProjectViewSet, 'project')
router.register(r'merchants', MerchantViewSet, 'merchant')
router.register(r'users', UserViewSet, 'user')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('token/', CustomAuthToken.as_view())
]