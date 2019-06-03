# coding: utf-8

from slackbot.bot import respond_to
import requests


@respond_to('')
def mention_func(message):
    name = message.channel._client.users[message.body['user']]["profile"]['display_name']
    payload = {'name': name, 'emoji_level': 9, "punctiuation_level": 0}
    r = requests.post("https://ojichat.appspot.com/post", data=payload)
    data = r.json()
    message.reply(data['message'])
