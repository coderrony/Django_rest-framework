

from django.urls import path, include
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register(r'stream', views.StreamPlatformVS, basename="streamplatform")

urlpatterns = [
    path("list/", views.WatchListAv.as_view(), name="movie_list"),
    path("<int:pk>/", views.WatchDetails.as_view(), name="movie_details"),

    path('', include(router.urls)),

    #     path("stream/", views.StreamPlatformAv.as_view(), name="stream"),
    #     path("stream/<int:pk>", views.StreamDetails.as_view(), name="stream-details"),

    path("<int:pk>/review-create/",
         views.ReviewCreate.as_view(), name="review-create"),
    path("<int:pk>/reviews/",
         views.ReviewList.as_view(), name="stream-details"),
    path("review/<int:pk>/",
         views.ReviewDetail.as_view(), name="review-details"),

    # path("review/", views.ReviewList.as_view(), name="review-list"),
    # path("review/<int:pk>", views.ReviewDetail.as_view(), name="review-details"),
]
