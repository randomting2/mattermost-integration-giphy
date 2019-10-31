# -*- coding: utf-8 -*-
import logging
import os
import sys
import json

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
    print("la") 
    return "OK"


@app.route('/', methods=['POST'])
def new_post():
    """
    Mattermost new post event handler
    """
    try:
        bo = True
        # NOTE: common stuff
        slash_command = False
        resp_data = {}
        resp_data['username'] = USERNAME
        resp_data['icon_url'] = ICON_URL

        data = request.form
        print(data)
        if not 'token' in data:
            raise Exception('Missing necessary token in the post data')

        #if MATTERMOST_GIPHY_TOKEN.find(data['token']) == -1:
        #    raise Exception('Tokens did not match, it is possible that this request came from somewhere other than Mattermost')

        # NOTE: support the slash command
        if 'command' in data:
            slash_command = True
            resp_data['response_type'] = 'in_channel'
        if data.get('channel_name')==u'bingochan':
            if datetime.datetime.today().weekday() == 3:
                if data.get('text').lower()==u'in':
                    if (int((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))>=10) and (int((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))<=13): 
                        print('<div title="player-name-{}">{}</div> !'.format((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%Y-%m-%d')                                                                          
        ,data.get('user_name').title()) )
                        print("la")
                        resp_data['text'] = '''`{}` joined the game! Be ready at  1:45p.m.\n'''.format(data.get('user_name').title())
                    elif (int((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))<10):
                        print((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))
                        resp_data['text'] = '''`{}` is a little too soon! See ya later!\n'''.format(data.get('user_name').title())
                    else:
                        print((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))
                        resp_data['text'] = '''`{}` is a little too late! See ya next week!\n'''.format(data.get('user_name').title())  
                elif data.get('text').lower()==u'bingo!':
                    if (int((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))>=13) and (int((datetime.datetime.today()).strftime('%M'))>=00):                
                        print('<div title="winner-name-{}">{}_{}</div> !'.format((datetime.datetime.today()+datetime.timedelta(hours=+2)).strftime('%Y-%m-%d')                                                                          
            ,data.get('user_name').title(),(datetime.datetime.today()+datetime.timedelta(hours=+2)).strftime('%Y-%m-%d-%H-%M-%s'))) 
                        resp_data['text'] = '''`{}` just claimed a bingo! \n'''.format(data.get('user_name').title())
                    elif (int((datetime.datetime.today()+datetime.timedelta(hours=+1)).strftime('%H'))>13):
                        resp_data['text'] = '''It's too late to bingo !\n'''.format(data.get('user_name').title())
                    else:
                        resp_data['text'] = '''It's too soon to bingo !\n'''.format(data.get('user_name').title())                        
                else:
                    bo = False
            else:
                resp_data['text'] = '''Sorry `{}`, there is no bingo today, see you on Thursday!\n'''.format(data.get('user_name').title())     
        else:
            bo = False
    except Exception as err:
        msg = err.message
        logging.error('unable to handle new post :: {}'.format(msg))
        resp_data['text'] = msg
    finally:
        resp = Response(content_type='application/json')
        resp.set_data(json.dumps(resp_data))
        if bo:
            return resp
