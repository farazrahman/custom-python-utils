import pandas as pd
import smtplib
import requests
import json
from bs4 import BeautifulSoup
from typing import List, Dict
from datetime import datetime, timedelta


def fetch_website_details(url_address: str, header: Dict[str, str]):
    """
    Function to scrape and parse html content from a URL
    :param url_address: get the url address of the website you want to parse
    :param header: get the request headers.
    :return:
    """
    URL = url_address
    header = header
    page = requests.get(URL, headers=header)
    page.raise_for_status()
    soup = BeautifulSoup(page.text, 'html.parser')
    response = soup.text
    response_json = json.loads(response)
    return response_json