import re
import requests

from collections import Iterable
from lxml import etree
from .parser import parse_search_parameters, parse_aspx_state


def flat_params(parameters):
    params = []
    for k, v in parameters.items():
        if isinstance(v, Iterable) and not isinstance(v, str):
            for i in v:
                params.append((k, i))
        else:
            params.append((k, v))
    return params


def get_aspx_state(qno):
    SEARCH_URL = f'https://stats.moe.gov.tw/search.aspx?qno={qno}'
    r = requests.get(SEARCH_URL)
    return parse_aspx_state(r.text)


def get_qno(eventtarget, state, recursive=False):
    URL = f'https://stats.moe.gov.tw/default.aspx'
    post_back = {'__EVENTTARGET': eventtarget, '__EVENTARGUMENT': ''}
    r = requests.post(URL, flat_params(post_back) + flat_params(state))

    qno = r.url.split('=')[-1]
    if not recursive:
        return qno

    # Recursive
    # Check left.aspx have anything
    LEFT_URL = f'https://stats.moe.gov.tw/left.aspx?qno={qno}'
    r = requests.get(LEFT_URL)
    root = etree.HTML(r.text)
    if not root.xpath('//a[contains(@href, "search.aspx")]'):
        return qno

    # Gather all links
    return [(list(i.itertext())[0], i.get('href').split('=')[-1])
                for i in root.xpath('//a[contains(@href, "search.aspx")]')[1::2]]


def get_all_qno():
    URL = f'https://stats.moe.gov.tw'
    r = requests.get(URL)
    state = parse_aspx_state(r.text)

    qnos = []
    root = etree.HTML(r.text)
    for a in root.xpath('//a[@onclick="document.forms[0].target=\'_blank\';"]'):
        qnos.append((a.text, get_qno(a.get('id').replace('_', '$'), state, recursive=True)))
    return qnos


def get_search_parameters(qno):
    SEARCH_URL = f'https://stats.moe.gov.tw/search.aspx?qno={qno}'
    r = requests.get(SEARCH_URL)
    return parse_search_parameters(r.text)


def get_search_result(qno, parameters, type='csv', state={}, fill_state=True):
    RESULT_URL = f'https://stats.moe.gov.tw/result.aspx?qno={qno}'

    # Step 1: get the data
    if fill_state:
        state = get_aspx_state(qno)
    r = requests.post(RESULT_URL, flat_params(state) + flat_params(parameters))

    # Step 2: Convert to CSV
    state = parse_aspx_state(r.text)
    r = requests.post(RESULT_URL, flat_params(state) + flat_params({'ToCsvButton.x': 12, 'ToCsvButton.y': 18}))
    return map(lambda x: x.split(','), r.text.split('\r\n'))
