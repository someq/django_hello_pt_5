from django.contrib.auth import get_user_model
from django.db.models import Model
from django.http import HttpResponseRedirect
from django.test import TestCase
from django.urls import reverse

from webapp.models import Tag, STATUS_MODERATED, Article


class NotAuthArticleCreateTestCase(TestCase):
    def test_get_create_article(self):
        response = self.client.get(reverse('webapp:article_create'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('webapp:article_create')
        self.check_redirect(response, redirect_url)

    def test_post_create_article(self):
        response = self.client.post(reverse('webapp:article_create'))
        redirect_url = reverse('accounts:login') + '?next=' + reverse('webapp:article_create')
        self.check_redirect(response, redirect_url)

    def check_redirect(self, response, redirect_url):
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        self.assertEqual(response.url, redirect_url)


class AuthArticleCreateTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        User: Model = get_user_model()
        user, created = User.objects.get_or_create(username='admin')
        if created:
            user.set_password('admin')
            user.save()
        cls.user = user

        cls.tags = []
        for tag in ['django', 'python', 'info']:
            tag_obj = Tag.objects.create(name=tag)
            cls.tags.append(tag_obj)

    def setUp(self) -> None:
        self.client.login(username='admin', password='admin')

    def tearDown(self) -> None:
        self.client.logout()

    def test_create_article_success(self):
        url = reverse('webapp:article_create')
        tags = [self.tags[0].pk, self.tags[1].pk]
        data = {'title': 'TestTestTest', 'text': 'Test', 
                'status': STATUS_MODERATED, 'tags': tags}
        response = self.client.post(url, data)
        article = Article.objects.order_by('pk').last()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(type(response), HttpResponseRedirect)
        redirect_url = reverse('webapp:article_view', kwargs={'pk': article.pk})
        self.assertEqual(response.url, redirect_url)
        self.assertEqual(article.title, data['title'])
        self.assertEqual(article.text, data['text'])
        self.assertEqual(article.status, STATUS_MODERATED)
        self.assertEqual(article.author, self.user)
        tags = [self.tags[0].name, self.tags[1].name, self.user.username]
        article_tag_names = article.tags.values_list('name', flat=True)
        for tag in tags:
            self.assertIn(tag, article_tag_names)

    # def test_article_author_is_current_user(self):
    #     ...

    # def test_article_creates_tag_with_username(self):
    #     ...
