#!/usr/bin/env python3
#
# Copyright (C) 2018 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Import file content into MoinMoin Wiki
"""

import os
import sys
import glob
import argparse
import logging
import requests
import bs4

from urllib.parse import urlparse, urljoin
from time import sleep


def login(url, username, password):
    """Login to MoinMoin Wiki and returns session cookie"""
    payload = {
        "action": "login",
        "name": username,
        "password": password,
        "login": "Login",
        "login": "Login",
    }
    r = requests.post(url, data=payload)
    if r.status_code == 200:
        logging.info("Successfully logged in as {}".format(username))
        return r.cookies
    else:
        r.raise_for_status()


def get_ticket(url, session):
    """Get ticket and new rev for URL"""
    payload = {"action": "edit", "editor": "text"}
    r = requests.get(url, params=payload, cookies=session)
    r.raise_for_status()
    try:
        html = bs4.BeautifulSoup(r.text, features="html.parser")
        ticket = html.find(attrs={"name": "ticket"})["value"]
        rev = html.find(attrs={"name": "rev"})["value"]
        logging.info("Got ticket to edit {}".format(url))
        return ticket, rev
    except:
        logging.critical("Failed to get ticket to edit {}".format(url))
        sys.exit(1)


def edit_page(url, session, text, ticket, rev):
    """Post content to page"""
    payload = {
        "action": "edit",
        "editor": "text",
        "rev": rev,
        "ticket": ticket,
        "button_save": "Save Changes",
        "savetext": text,
        "comment": "Automated import",
    }
    r = requests.post(url, data=payload, cookies=session)
    r.raise_for_status()
    logging.info("Successfully edited page {}".format(url))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-u", "--username", required=True, help="Username for MoinMoin Wiki"
    )
    parser.add_argument(
        "-p", "--password", required=True, help="Password for MoinMoin Wiki"
    )
    parser.add_argument(
        "-f",
        "--files",
        required=True,
        help="Files with text to import. " "Use file name or pattern like 'page-*.txt'",
    )
    parser.add_argument(
        "-b",
        "--url",
        required=True,
        help="Base URL for page " "like https://wiki.example.com/Website/Archive/",
    )
    parser.add_argument(
        "-l",
        "--log",
        dest="loglevel",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Log level. Default: INFO",
    )
    args = parser.parse_args()

    LEVEL = logging.getLevelName(args.loglevel)
    FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
    logging.basicConfig(level=LEVEL, format=FORMAT, datefmt="%Y-%m-%d %H:%M:%S")

    x = urlparse(args.url)
    base_url = "{}://{}/".format(x.scheme, x.netloc)

    session = login(base_url, args.username, args.password)

    for file in glob.glob(args.files):
        file_name = os.path.splitext(os.path.basename(file))[0]
        url = urljoin(args.url, file_name)
        ticket, rev = get_ticket(url, session)
        with open(file) as f:
            edit_page(url, session, f.read(), ticket, rev)
        # wait to prevent triggering the surge protection of the wiki
        sleep(1)


if __name__ == "__main__":
    main()
