import os
from zulip import Client

from rest_framework.response import Response

# By default the API key file you download is named as 'download' by Zulip. You can place
# this file one directory previous to the cuurent directory your file is in
client = Client(config_file='download')

def get_zulip_user(zulip_id):
    result = client.get_user_by_id(zulip_id)
    print(result)
    return result['user']

def get_messages(zulip_id):
    request = {
        'anchor': 'newest',
        'num_before': 5000,
        'num_after': 0,
        'narrow': [
            { 'operator': 'sender', 'operand': f'user{zulip_id}@zulipchat.com' },
        ]
    }
    result = client.get_messages(request)
    result = len(result['messages'])
    return result

def get_newest_message(zulip_id):
    request = {
        'anchor': 'newest',
        'num_before': 1,
        'num_after': 0,
        'narrow': [
            { 'operator': 'sender', 'operand': f'user{zulip_id}@zulipchat.com' },
        ]
    }
    result = client.get_messages(request)
    result = result['messages']
    return result

def get_stream_messages(stream, zulip_id):
    request = {
        'anchor': 'newest',
        'num_before': 1,
        'num_after': 0,
        'narrow': [
            { 'operator': 'sender', 'operand': f'user{zulip_id}@zulipchat.com' },
            { 'operator': 'stream', 'operand': f'{stream}' },
        ]
    }
    result = client.get_messages(request)
    result = len(result['messages'])
    return result
