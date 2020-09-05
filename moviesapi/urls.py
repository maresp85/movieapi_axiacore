from django.contrib import admin
from django.urls import path
from movies.views import MovieAPI, DetailMovieAPI, RatingMovieAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', MovieAPI.as_view(), name="movie"),
    path('movie/<int:pk>', MovieAPI.as_view(), name="movie"),
    path('movie/detail/<int:pk>', DetailMovieAPI.as_view(), name="moviedetail"),
    path('updateratingmovie/<int:pk>', RatingMovieAPI.as_view(), name="updateratingmovie"),
    #JWT
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
