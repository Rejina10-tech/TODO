from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.views import TodoViewSet
from .views.logout import LogoutView
from .views.reset_pass import PasswordResetRequestView, PasswordResetConfirmView
from .views.register import RegisterAPIView




router = DefaultRouter()
router.register(r'tasks', TodoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/logout/', LogoutView.as_view(), name='logout'),
     path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/password-reset/', PasswordResetRequestView.as_view(), name='password_reset'),
    path('api/password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]
