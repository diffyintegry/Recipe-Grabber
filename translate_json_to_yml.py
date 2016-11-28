#!/usr/bin/python
import json
import sys
from collections import defaultdict
from unidecode import unidecode
from HTMLParser import HTMLParser

h = HTMLParser()

_schema_keys_to_yml = {
                'description' : 'notes',
                'image' : 'photo',
                'recipeCuisine' : 'notes',
                'recipeInstructions' : 'directions',
                'recipeCategory' : 'categories',
                'name' : 'name',
                'author' : 'source',
                'ingredients' : 'ingredients',
                'recipeYield' : 'servings',
                'prepTime' : 'prep_time',
                'cookTime' : 'cook_time',
                'source_url' : 'source_url',
                'notes' : 'notes',
            }

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
            'source_url',
            'source',
            'notes',
            ]
def remove_non_ascii(input):
    ''' borrowed from http://stackoverflow.com/a/35492167
    '''
    return unidecode(unicode(input, encoding = "utf-8"))



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
    all_ymls = []
    for recipe  in recipes:
        yml_recipe = defaultdict(str)
        for key in _schema_keys_to_yml:
            if key in recipe:
                handle_key(recipe[key], yml_recipe, key)
        all_ymls.append(yml_recipe)
    return all_ymls



def handle_key(incomingData, yml_out, key):
    '''different handling for each type of key
    '''
    try:
        if key in (
                    'description',
                    'recipeCuisine',
                    'recipeCategory',
                    'recipeYield',
                    'prepTime',
                    'cookTime',
                    'source_url',
                    'name',
                    'notes',
                    ):
            if yml_out[_schema_keys_to_yml[key]]:
                yml_out[_schema_keys_to_yml[key]] += '\n'
            yml_out[_schema_keys_to_yml[key]] += incomingData
        elif key in ('recipeInstructions','ingredients'):
            yml_out[_schema_keys_to_yml[key]] = '\n'.join(incomingData)
        #elif key == 'notes':
        #    yml_out[_schema_keys_to_yml[key]] = '\n'.join(incomingData)
        elif key == 'author':
            yml_out[_schema_keys_to_yml[key]] = incomingData['name']
        elif key == 'image':
            yml_out[_schema_keys_to_yml[key]] = ''
    except:
        pass
#yml example:
#- name:NAME
#  servings:
#  etc.
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
            'source_url',
            'source',
            'notes',
            ]

def yml_prep_to_yml(list_of_yml_dicts):
    '''translates the yml_prepped dicts into yml string
    '''
    strList = []
    for item in list_of_yml_dicts:
        strList.append('- ')
        for key in _yml_keys:
            if not item[key]:
                continue
	    line = item[key].replace('<br>','\n').replace('<br/>','\n').replace('\n','\r\n    ')
	    line = line.replace('<span class="fn">','').replace('</span>','')
	    line = line.replace('<span class ="fn">','').replace('<span class = "fn">','').replace('<span class= "fn">','')
	    line = h.unescape(line)
	    line = remove_non_ascii(line.encode('UTF-8'))
	    line = line.replace('\n','')
            strList.append(key)
            strList.append(': ')
            if key in ('ingredients', 'directions','notes'):
                strList.append('|\r\n    ')
            strList.append(line)
            strList.append('\r\n  ')
        del(strList[-1])
        strList.append('\r\n')
    print u''.join(strList).encode('utf-8').strip()
            





if __name__ == '__main__':
    json_data = load_json(sys.argv[1])
    yml_prep = translate_json_to_yml_prep(json_data)
    yml_prep_to_yml(yml_prep)



















