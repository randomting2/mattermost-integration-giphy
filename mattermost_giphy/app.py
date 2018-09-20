# -*- coding: utf-8 -*-
import logging
import os
import sys
import json
from urlparse import urlsplit
from urlparse import urlunsplit

import requests
import random
import datetime
from flask import Flask
from flask import request
from flask import Response

from mattermost_giphy.settings import *


logging.basicConfig(
    level=logging.INFO, format='[%(asctime)s] [%(levelname)s] %(message)s')
app = Flask(__name__)

@app.route('/new_post')
def root():
    """
    Home handler
    """
    print "la" 
    return "OK"


@app.route('/', methods=['POST'])
def new_post():
    """
    Mattermost new post event handler
    """
    try:
        print "ici"
        # NOTE: common stuff
        slash_command = False
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        data = request.form
        print data


        if not 'token' in data:
            raise Exception('Missing necessary token in the post data')

        #if MATTERMOST_GIPHY_TOKEN.find(data['token']) == -1:
        #    raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        # NOTE: support the slash command
        if 'command' in data:
            slash_command = True
            resp_data['response_type'] = 'in_channel'
        if data.get('channel_name')==u'bingo':
            if data.get('text').lower()==u'in':
                print '''<div title="player-name-`{}`">`{}`</div> !'''.format(datetime.datetime.today().strftime('%Y-%m-%d')
,data.get('user_name').title())
                resp_data['text'] = '''`{}` joined the game! Be ready at  1p.m. :\n'''.format(data.get('user_name').title())
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        return resp
