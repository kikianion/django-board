from django.contrib.auth.models import User
from django.test import TestCase
#from django.core.urlresolvers import reverse
from django.urls import resolve, reverse
from ..views import BoardListView

from ..forms import NewTopicForm
from ..models import Board, Post, Topic
from ..views import board_topics, home, new_topic

# Create your tests here.

class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        # self.assertEquals(view.func, home)
        self.assertEquals(view.func.view_class, BoardListView)

    def test_home_view_contains_link_to_topics_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
