#!/usr/bin/python
import json
import sys

_schema_keys = [
                'description',
                'image',
                'recipeCuisine',
                'aggregateRating',
                'recipeInstructions',
                'recipeCategory',
                'name',
                'author',
                'ingredients',
                'recipeYield',
                '@context',
                '@type'
            ]

_yml_keys = [
            'name',
            'servings',
            'prep_time',
            'cook_time',
            'on_favorites',
            'categories',
            'ingredients',
            'directions',
            'photo',
            ]


def load_json(filename):
    ''' load the file into a python obj
    '''
    with open(filename) as fi:
        contents = json.load(fi)
    return contents


def default_yml_recipe():
    '''returns a default empty recipe dict in yml
    '''
    default_recipe = {}
    for key in _yml_keys:
        default_recipe[key] = ''
    return default_recipe



def translate_json_to_yml_prep(recipes):
    ''' takes list of dictionaries raw from schema and translates to paprika yml
    '''
    for recipe  in recipes:
        for key in _schema_keys:
            pass 



#yml example:
#- name:NAME
#  servings:
#  etc.



if __name__ == '__main__':
    x = load_json(sys.argv[1])
    allKeys = set()
    for item in x:
        allKeys |= set(item.keys())
    print allKeys


