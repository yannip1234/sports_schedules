from types import SimpleNamespace

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .scripts import scraper_threaded
import os
import requests
import json
from datetime import datetime, timedelta

def today(response):
    now = datetime.now()
    monday = (now - timedelta(days=now.weekday()))
    sunday = monday + timedelta(days=6)
    # url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate={(monday - timedelta(days=7)).strftime("%Y-%m-%d")}&endDate={sunday.strftime("%Y-%m-%d")}'
    # url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2021-10-26&endDate=2021-10-7&teamId=111'
    url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2021-10-26&endDate=2021-11-03'
    nfl = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates={datetime.now().strftime("%Y%m%d")}'
    # nhl = f'https://statsapi.web.nhl.com/api/v1/schedule?startDate={monday.strftime("%Y-%m-%d")}&endDate={sunday.strftime("%Y-%m-%d")}'
    nhl = f'http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?dates={datetime.now().strftime("%Y%m%d")}&limit=100'
    res = requests.get(url)
    obj = json.loads(res.content, object_hook=lambda d: SimpleNamespace(**d))
    obj.dates = sorted(obj.dates, key=lambda x: x.date, reverse=True)
    res_nfl = requests.get(nfl)
    nfl = json.loads(res_nfl.content, object_hook=lambda d: SimpleNamespace(**d))
    nfl.events = sorted(nfl.events, key=lambda x: x.date, reverse=True)
    # res_nhl = requests.get(nhl)
    # nhl = json.loads(res_nhl.content, object_hook=lambda d: SimpleNamespace(**d))
    # nhl.dates = sorted(nhl.dates, key=lambda x: x.date, reverse=True)
    res_nhl = requests.get(nhl)
    nhl = json.loads(res_nhl.content, object_hook=lambda d: SimpleNamespace(**d))
    nhl.events = sorted(nhl.events, key=lambda x: x.date, reverse=True)
    # l=[]
    # for date in obj.dates:
    #     for game in date.games:
    #         l.append(json.loads(requests.get(f'https://statsapi.mlb.com/api/v1/game/{game.gamePk}/boxscore').content, object_hook=lambda d: SimpleNamespace(**d)))
    return render(response, 'links/index.html', {
        'dates': obj.dates,
        'games_nfl': nfl.events,
        'games_nhl': nhl.events
        # 'game_data': l
    })

def week(response):
    now = datetime.now()
    monday = (now - timedelta(days=now.weekday()))
    sunday = monday + timedelta(days=6)
    # url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate={(monday - timedelta(days=7)).strftime("%Y-%m-%d")}&endDate={sunday.strftime("%Y-%m-%d")}'
    # url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2021-10-26&endDate=2021-10-7&teamId=111'
    url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2021-10-26&endDate=2021-11-03'
    nfl = f'https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard'
    # nhl = f'https://statsapi.web.nhl.com/api/v1/schedule?startDate={monday.strftime("%Y-%m-%d")}&endDate={sunday.strftime("%Y-%m-%d")}'
    nhl = f'http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?dates={monday.strftime("%Y%m%d")}-{sunday.strftime("%Y%m%d")}&limit=100'
    print(nhl)
    res = requests.get(url)
    obj = json.loads(res.content, object_hook=lambda d: SimpleNamespace(**d))
    obj.dates = sorted(obj.dates, key=lambda x: x.date, reverse=True)
    res_nfl = requests.get(nfl)
    nfl = json.loads(res_nfl.content, object_hook=lambda d: SimpleNamespace(**d))
    nfl.events = sorted(nfl.events, key=lambda x: x.date, reverse=True)
    # res_nhl = requests.get(nhl)
    # nhl = json.loads(res_nhl.content, object_hook=lambda d: SimpleNamespace(**d))
    # nhl.dates = sorted(nhl.dates, key=lambda x: x.date, reverse=True)
    res_nhl = requests.get(nhl)
    nhl = json.loads(res_nhl.content, object_hook=lambda d: SimpleNamespace(**d))
    nhl.events = sorted(nhl.events, key=lambda x: x.date, reverse=True)
    # l=[]
    # for date in obj.dates:
    #     for game in date.games:
    #         l.append(json.loads(requests.get(f'https://statsapi.mlb.com/api/v1/game/{game.gamePk}/boxscore').content, object_hook=lambda d: SimpleNamespace(**d)))
    return render(response, 'links/index.html', {
        'dates': obj.dates,
        'games_nfl': nfl.events,
        'games_nhl': nhl.events
        # 'game_data': l
    })


def test(response):
    now = datetime.now()
    monday = (now - timedelta(days=now.weekday()))
    sunday = monday + timedelta(days=6)
    # url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate={(monday - timedelta(days=7)).strftime("%Y-%m-%d")}&endDate={sunday.strftime("%Y-%m-%d")}'
    # url = f'http://statsapi.mlb.com/api/v1/schedule/games/?sportId=1&startDate=2021-10-26&endDate=2021-10-7&teamId=111'
    # nhl = f'http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?dates={monday.strftime("%Y%m%d")}-{sunday.strftime("%Y%m%d")}'
    nhl = 'http://site.api.espn.com/apis/site/v2/sports/hockey/nhl/scoreboard?dates=20211113-20211114'
    res_nhl = requests.get(nhl)
    nhl = json.loads(res_nhl.content, object_hook=lambda d: SimpleNamespace(**d))
    nhl.events = sorted(nhl.events, key=lambda x: x.date, reverse=True)
    # print(nhl.events)
    # l=[]
    # for date in obj.dates:
    #     for game in date.games:
    #         l.append(json.loads(requests.get(f'https://statsapi.mlb.com/api/v1/game/{game.gamePk}/boxscore').content, object_hook=lambda d: SimpleNamespace(**d)))
    return render(response, 'links/test.html', {
        'games_nhl': nhl.events
        # 'game_data': l
    })


# Create your views here.
def MLB(response):
    gm = scraper_threaded.BTS('MLB')
    # gm.generate_m3u()
    print(gm.games)
    return render(response, 'links/links.html', {
        'games': gm.games
    })


def MLB_m3u8(response):
    category = 'MLB'
    gm = scraper_threaded.BTS(category)
    gm.generate_m3u()
    with open(f'{category}.m3u', 'r') as f:
        file = f.read()
        response = HttpResponse(f.read(),
                                content_type="audio/x-mpegurl")  # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(f'{category}.m3u')
        return response


def NBA(response):
    gm = scraper_threaded.BTS('NBA')
    # gm.generate_m3u()

    return render(response, 'links/links.html', {
        'games': gm.games
    })


def NBA_m3u8(response):
    category = 'NBA'
    gm = scraper_threaded.BTS(category)
    gm.generate_m3u()
    with open(f'{category}.m3u', 'r') as f:
        file = f.read()
        response = HttpResponse(f.read(),
                                content_type="audio/x-mpegurl")  # mimetype is replaced by content_type for django 1.7
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(f'{category}.m3u')
        return response
