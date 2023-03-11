from django.urls import path

from . import views

# namespace
app_name = 'news'

urlpatterns = [
    path('articles/<int:year>', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>', views.article_detail),

    path('contact/', views.ListView.as_view(), name='list'),
    path('contact/search', views.SearchListView.as_view(), name='search_list'),
    path('contact/detail/<int:pk>', views.DetailView.as_view(), name='detail'),
    path('contact/update/<int:pk>', views.UpdateView.as_view(), name='update'),
    path('contact/delete/<int:pk>', views.DeleteView.as_view(), name='delete'),
    path('contact/create/', views.CreateView.as_view(), name='create'),

    path('develop_tips/', views.develop_tips, name='develop_tips'),
]
