from django.urls import path

from webapp.views import article_list_view, article_create_view, article_detail_view, article_update_view

urlpatterns = [
    path('', article_list_view, name='articles'),
    path('create/', article_create_view, name='create_article'),
    path('article/<int:pk>/', article_detail_view, name='article_detail'),
    path('article/<int:pk>/update/', article_update_view, name='update_article'),
]
