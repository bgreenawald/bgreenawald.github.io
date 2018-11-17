# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:58:38 2018

@author: bgree
"""

from bs4 import BeautifulSoup
import re
import json

with open("content/favorite_quotes.html", "r", encoding='utf-8') as file:
    quote_text = file.read()
    
quotes = BeautifulSoup(quote_text, 'html.parser')

quote_body = quotes.body

remove_multiple_spaces = re.compile("[ ]+")
# Iterate over every section in the body, skipping the first as that is the
# selection section
all_quotes = []
for section in quote_body.find_all('section')[1:]:
    # For section, iterate over all subsections
    for subsection in section.find_all('section'):
        print(subsection.h1)
        print(subsection.h2)
        title = subsection.h2.text if subsection.h2 else "Miscellaneous" 
        for quote in subsection.find_all('li', class_="random"):
            cur_quote = {}
            cur_quote["title"] = title
            
            str_quote = " ".join([str(x) for x in quote.contents])
            str_quote = str_quote.replace("\n", "")
            str_quote = re.sub(remove_multiple_spaces, " ", str_quote)
            cur_quote["quote"] = str_quote.strip()
            
            all_quotes.append(cur_quote)
            
with open("quotes.json", "w+") as file:
    file.write(json.dumps(all_quotes, sort_keys=True, indent=4, separators=(',', ': ')))
