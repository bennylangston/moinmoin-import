#!/usr/bin/env python

import os
import argparse
import logging
import requests
import bs4

from urllib.parse import urljoin


def login(username, password):
    """Login to MoinMoin Wiki and returns session cookie"""
    payload = {'action':'login', 'name': username, 'password': password,
               'login': 'Login', 'login': 'Login'}
    r = requests.post('https://intra.greenbone.net/', data = payload)
    return r.cookies


def get_ticket(url, session):
    """Get ticket and new rev for URL"""
    payload = {'action': 'edit', 'editor': 'text'}
    r = requests.get(url, params = payload, cookies = session)
    html = bs4.BeautifulSoup(r.text, features='html.parser')
    ticket = html.find(attrs={"name": "ticket"})['value']
    rev = html.find(attrs={"name": "rev"})['value']
    return ticket, rev


def edit_page(url, session, text, ticket, rev):
    """Post content to page"""
    payload = {'action': 'edit', 'editor': 'text', 'rev': rev,
               'ticket': ticket, 'button_save': 'Save Changes',
               'savetext': text, 'comment': 'Automated import'}
    r = requests.post(url, data = payload, cookies = session)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--username', required = True,
                        help = 'Username for MoinMoin Wiki')
    parser.add_argument('-p', '--password', required = True,
                        help = 'Password for MoinMoin Wiki')
    parser.add_argument('-f', '--file', required = True,
                        help = 'File with text to import')
    parser.add_argument('-b', '--url', required = True,
                        help = 'Base URL for page '
                                'like https://intra.greenbone.net/QM/test/')
    args = parser.parse_args()

    session = login(args.username, args.password)
    file_name = os.path.splitext(os.path.basename(args.file))[0]
    url = urljoin(args.url, file_name)
    ticket, rev = get_ticket(url, session)
    with open(args.file) as f:
        edit_page(url, session, f.read(), ticket, rev)


if __name__ == '__main__':
    main()
