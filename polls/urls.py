from django.urls import path

from . import views

# ネームスペース
app_name = 'polls'

urlpatterns = [
    # ex: /polls/
    # name引数はテンプレートから{% url 'index' %}のように使う。
    # 
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # 汎用DetailViewはpkで渡す。
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # ex: /polls/5/get404/
    path('<int:question_id>/get404/', views.get404, name='get404'),

        # ex: /polls/5/get404_shortcut/
    path('<int:question_id>/get404_shortcut/', views.get404_shortcut, name='get404_shortcut'),
]
