#!/usr/bin/python

from BeautifulSoup import BeautifulSoup
import requests as req
import json
from pprint import pprint

_times = [
            'prepTime',
            'cookTime',
            'totalTime',
         ]


def find_recipe(soup, recipes=[]):
    ''' look for recipes in the given html
    '''
    recipeDict = {}
    for item in soup.findAll('script', type='application/ld+json'):
        try:
            recipeData = json.loads(item.contents[0])
            assert recipeData['@type'] == 'Recipe'
            break
        except:
            pass
    if recipeDict:
        for item in soup.findAll('time'):
            try:
                itemprop = item['itemprop']
                if itemprop in _times:
                    recipeDict[itemprop] = item.contents[0]
            except:
                pass
        recipes.append(recipeDict)
    return recipes





def main():
    ''' Get a recipe and pprint it
    '''
    doc = raw_input('what website?')
    soup = BeautifulSoup(req.get(doc).text)
    pprint( find_recipe(soup))



if __name__=='__main__':
    main()
