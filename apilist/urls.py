from django.urls import include, path
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()
# router.register(r'anime',views.AnimeViewSet)
#
# urlpatterns = [
#     path('',include(router.urls)),
#     path('get-anime-list',include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    path('anime/', views.anime_list),
    path('anime/<int:pk>/', views.anime_detail),
    path('anime/<str:status>/', views.anime_status)
]
