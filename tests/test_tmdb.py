from moviebotapi import MovieBotServer
from moviebotapi.core.models import MediaType
from moviebotapi.core.session import AccessKeySession
from moviebotapi.ext import MediaMetaSelect
from tests.constant import SERVER_URL, ACCESS_KEY

server = MovieBotServer(AccessKeySession(SERVER_URL, ACCESS_KEY))


def test_get():
    meta = MediaMetaSelect(tmdb=server.tmdb.get(MediaType.TV, 86163))
    assert meta


def test_search():
    server.tmdb.search(MediaType.Movie, '子弹列车')


def test_search_multi():
    server.tmdb.search_multi('权利的堡垒')
