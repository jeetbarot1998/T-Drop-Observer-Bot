import urllib.request, json
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import requests
from config import base_url_for_movie
from connections.postgress_connection import connection
import datetime
import ast
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# def data_fetch_from_api(external_url):
#     with urllib.request.urlopen(external_url) as url:
#         api_raw_data = json.loads(url.read().decode('utf-8'))
#         list_data = api_raw_data['data']
#         return list_data

def web_scraper(movie_name):
    url1 = base_url_for_movie +str(movie_name) + '+genre'
    html1 = requests.get(url1)
    soup = BeautifulSoup(html1.text, 'html.parser')
    scraped_value = (soup.find_all('div', class_={'BNeawe deIvCb AP7Wnd'}))
    genre_list_for_movie = list()
    for index, value in enumerate(scraped_value):
        if index != 0 and index != len(scraped_value):
            genre_list_for_movie.extend(value)
    return genre_list_for_movie

def search_common(movie_name1, movie_name2):
    genre_1 = web_scraper(movie_name1)
    genre_2 = web_scraper(movie_name2)
    common = common_movie_search(genre_1,genre_2)
    result = insert_into_db(movie_name1, movie_name2)
    if result == 1:
        return common
    else:
        return 0


def insert_into_db(movie_name1, movie_name2):
    cursor = connection.cursor()
    try:
        insert_query = """ INSERT INTO movie_entries(movie_1, movie_2, inserted_on) VALUES(%s, %s, %s) """
        item_purchase_time = datetime.datetime.now()
        item_tuple = (movie_name1, movie_name2, item_purchase_time)
        cursor.execute(insert_query, item_tuple)
        connection.commit()
        return 1
    except Exception as err_msg:
        return 'Error occured while inserting int DB' + str(err_msg)
    finally:
        cursor.execute("SELECT *FROM movie_entries")
        all_val_in_db = cursor.fetchall()
        print('here select====================', all_val_in_db)

