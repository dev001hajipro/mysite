# Django4 sandbox

Django4学習用のサンドボックス

## 参考情報

- [https://github.com/wsvincent/awesome-django](awesome-django)
- [https://medium.com/djangotube/django-roles-groups-and-permissions-introduction-a54d1070544](Django Roles, Groups, and Permissions Introduction)

## ログイン画面の実装サンプル

- [https://create-it-myself.com/know-how/implement-user-login-function-with-django/](https://create-it-myself.com/know-how/implement-user-login-function-with-django/)

## UIでdjango-bootstrap5を使う

- [https://github.com/zostera/django-bootstrap5](https://github.com/zostera/django-bootstrap5)
- [https://n-guitar.hatenablog.com/entry/2021/01/11/204659](【Django3.1】Djangoで作成したアプリケーションにBootstrap5-beta1を導入し、見た目を整える。)

### アクセス制限の調査

現状、/abc, /xxxx?=helloなど適当なURLにアクセスした場合、Djangoのエラーが表示される。
対応として、カスタム化した404ページまたは、Login画面にリダイレクトなどをしたい。

- [https://stackoverflow.com/questions/53901761/how-to-redirect-using-a-custom-django-404-error-view](How to redirect using a custom django 404 error view?)
