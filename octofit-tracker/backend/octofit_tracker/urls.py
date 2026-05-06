"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from rest_framework.reverse import reverse

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)

urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

def api_root(request, format=None):
    codespace_name = os.environ.get('CODESPACE_NAME')
    if codespace_name:
        base_url = f'https://{codespace_name}-8000.app.github.dev'
    else:
        base_url = request.build_absolute_uri('/')[:-1]
    return Response({
        'users': base_url + reverse('user-list', request=request, format=format),
        'teams': base_url + reverse('team-list', request=request, format=format),
        'activities': base_url + reverse('activity-list', request=request, format=format),
        'leaderboard': base_url + reverse('leaderboard-list', request=request, format=format),
        'workouts': base_url + reverse('workout-list', request=request, format=format),
    })
