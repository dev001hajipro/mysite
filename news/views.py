from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Article, Contact
from .forms import ConcatForm


def year_archive(request, year):
    ls = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': ls}
    return render(request, 'news/year_archive.html', context)


def month_archive(request, year, month):
    ls = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': ls}
    return render(request, 'news/month_archive.html', context)


def article_detail(request, year, month, pk):
    ls = Article.objects.filter(pub_date__year=year)
    context = {'year': year, 'article_list': ls}
    return render(request, 'news/article_detail.html', context)


class ListView(generic.ListView):
    def get_queryset(self):
        return Contact.objects.order_by('-pub_date')


class SearchListView(generic.ListView):
    """検索画面と一覧画面"""
    template_name = "news/contact_search_list.html"

    def get_queryset(self):
        print('query=', self.kwargs.get('query'))
        print("GET.get('query')=", self.request.GET.get('query'))
        query = self.request.GET.get('query')
        if query:
            return Contact.objects.filter(
                Q(subject__contains=query)
                | Q(message__contains=query))
        else:
            return Contact.objects.all()


class CreateView(generic.CreateView):
    """連作先作成画面"""
    form_class = ConcatForm
    template_name = 'news/contact_form.html'
    success_url = reverse_lazy('news:list')


class DetailView(generic.DetailView):
    model = Contact
    template_name = 'news/contact_detail.html'


class UpdateView(generic.UpdateView):
    # https://stackoverflow.com/questions/53692418/django-updateview-misses-queryset
    # ??? ContactFormクラス内にMetaクラスがあり、そこでmodelを記述しているが
    # ここでも記述しないといけない?
    # Answer:
    # CreateViewはデータベースからデータを取ってくる必要がない。
    # UpdateViewはデータベースからQuery問い合わせが必要。ただしform_classのMetaからは取得しない
    # そのため違和感がある。
    model = Contact
    form_class = ConcatForm
    template_name = 'news/contact_update_form.html'
    success_url = reverse_lazy('news:list')


class DeleteView(generic.DeleteView):
    model = Contact
    # DeleteViewではフォーム(form_class)を使わない。
    # つまり、generic.DeleteViewはUpdateViewのようにModelFormに対応していない。
    # そのため、form_classを用意してHTMLのformで表示しようとしても、フィールドは空になる。
    #form_class = ConcatForm
    template_name = 'news/contact_confirm_delete.html'
    success_url = reverse_lazy('news:list')
