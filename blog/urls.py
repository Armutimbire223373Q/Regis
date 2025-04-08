from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path('post/<int:year>/<int:month>/<int:day>/<slug:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_posts, name='category'),
    path('search/', views.post_search, name='post_search'),
    path('newsletter/subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
] 