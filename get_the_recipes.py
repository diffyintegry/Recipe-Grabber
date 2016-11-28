#!/usr/bin/python

from find_recipe_schema import find_recipe
from BeautifulSoup import BeautifulSoup
import requests as req
import json
import time

def get_all_urls(soup):
    ''' crawl for urls
    '''
    recipes = []
    for divTag in soup.findAll('div',{'class':'lcp_catlist_item'}):
        for aTag in divTag.findAll('a'):
            print '%s %s' % (aTag['href'], aTag['title'])
            
            time.sleep(1)
            find_recipe(BeautifulSoup(req.get(aTag['href']).text), aTag['href'], recipes)
            
            break
    return recipes



def main():
    url = raw_input('')
    soup = BeautifulSoup(req.get(url).text)
    with open('recipes_out.json','w') as fi:
        json.dump(get_all_urls(soup),fi)


if __name__ == '__main__':
    main()
