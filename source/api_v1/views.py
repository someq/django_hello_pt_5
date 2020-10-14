import json
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import ensure_csrf_cookie

from webapp.models import Article


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed('Only GET request are allowed')


class ArticleCreateView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        print(data)
        article = Article.objects.create(
            author_id=data['author_id'],
            title=data['title'],
            text=data['text']
        )
        return JsonResponse({
            'pk': article.pk,
            'author_id': article.author_id,
            'title': article.title,
            'text': article.text,
            'created_at': article.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': article.updated_at.strftime('%Y-%m-%d %H:%M:%S'),
        })