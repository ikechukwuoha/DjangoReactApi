from django.urls import path, include
from .views import ArticleViewSet, UserViewSet
from rest_framework.routers import DefaultRouter



app_name = 'api'


router = DefaultRouter()
router.register('articles',  ArticleViewSet, basename='articles')
router.register('users',  UserViewSet)



urlpatterns = [
    path('', include(router.urls))
    
    
    # path('articles/', views.article_list, name='article_list'),
    # path('articles/<int:pk>/', views.article_details, name='article_details'),
    
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view())
    
    
]