from django.urls import path
from .views import TaskDetail, TaskList, apiOverview
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("", apiOverview),
    path("task/", TaskList.as_view()),
    path("task/<int:pk>", TaskDetail.as_view()),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]