
import sys
import requests
import json
from bs4 import BeautifulSoup

# Pass in a URL containing hRecipe...

URL = 'http://britishfood.about.com/od/recipeindex/r/applepie.htm'




def parse_hrecipe(url):
    req = requests.get(URL)
    
    soup = BeautifulSoup.BeautifulSoup(req.text)
    
    hrecipe = soup.find(True, 'hrecipe')

    if hrecipe and len(hrecipe) > 1:
        fn = hrecipe.find(True, 'fn').string
        author = hrecipe.find(True, 'author').find(text=True)
        ingredients = [i.string 
                            for i in hrecipe.findAll(True, 'ingredient') 
                                if i.string is not None]

        instructions = []
        for i in hrecipe.find(True, 'instructions'):
            if type(i) == BeautifulSoup.Tag:
                s = ''.join(i.findAll(text=True)).strip()
            elif type(i) == BeautifulSoup.NavigableString:
                s = i.string.strip()
            else:
                continue

            if s != '': 
                instructions += [s]

        return {
            'name': fn,
            'author': author,
            'ingredients': ingredients,
            'instructions': instructions,
            }
    else:
        return {}


recipe = parse_hrecipe(URL)
print json.dumps(recipe, indent=4)
