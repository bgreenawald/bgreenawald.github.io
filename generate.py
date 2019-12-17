import json
import os
from random import shuffle
import re

from bs4 import BeautifulSoup


"""
Write all of the blogs to JSON in order to be searched.
"""
# Create an object to hold our JSON file
dicts = []

# Iterate through all blog files
for subdir, dirs, files in os.walk("blog"):
    for file in files:
        with open(subdir + os.sep + file) as file_name:

            # For each file, get the necesary info and append to our dict
            text = file_name.read()

            name = re.findall("titleBegin [\"\<\>a-zA-Z ,.\n\/?\-()0-9!:']+ titleEnd", text)
            name = name[0].replace("titleBegin -->", "").replace("<!-- titleEnd", "")

            content = re.findall("contentBegin [\"\<\>a-zA-Z ,.\n\/?\-()0-9!\t'=:%~_#\[\]\\\{\}\+$*`]+ contentEnd", text)
            try:
                content = content[0].replace("contentBegin -->", "").replace("<!-- contentEnd", "")
            except IndexError:
                print(file_name)

            date = re.findall("dateBegin [\"\<\>a-zA-Z ,.\n\/?\-()0-9!']+ dateEnd", text)
            date = date[0].replace("dateBegin ", "").replace(" dateEnd", "")

            path = re.findall("pathBegin [\"\<\>a-zA-Z ,.\n\/?\-()0-9!']+ pathEnd", text)
            path = path[0].replace("pathBegin ", "").replace(" pathEnd", "")

            dicts.append({"name": name, "content": content, "date": date, "location": path})
            file_name.close()

# Write the file to the json object
with open("data/data.json", "w+") as file:
    file.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))


"""
Write all of the quotes to JSON for random quotes.
"""
# Read in all of the quotes from local.
with open("content/favorite_quotes.html", "r", encoding='utf-8') as file:
    quote_text = file.read()

# Parse the quote with Beautiful Soup
quote_body = BeautifulSoup(quote_text, 'html.parser').body

# Compile the regular expression for removal of multiple spaces.
remove_multiple_spaces = re.compile("[ ]+")

# Iterate over every section in the body, skipping the first as that is the
# selection section
all_quotes = []
for section in quote_body.find_all('section')[1:]:
    content_type = section.get('id') if section.get('id') else 'None'
    content_type = content_type if content_type != "self" else 'other'
    # For section, iterate over all subsections
    for subsection in section.find_all('section'):
        # Extract out the origin of the quote, or make it 'Miscellaneous'
        title = subsection.h2.text if subsection.h2 else "Miscellaneous"
        # Extract out the title of the quote, else make is 'None'
        author = subsection.h3.text if subsection.h3 else "None"
        # Iterate over all of the quotes with the appropriate classname
        for quote in subsection.find_all('li', class_="random"):
            # Store the origin of the quote
            cur_quote = {}
            cur_quote["title"] = title
            cur_quote["author"] = author
            cur_quote["type"] = content_type.replace("_", " ")

            # Clean up the quote and store
            str_quote = " ".join([str(x) for x in quote.contents])
            str_quote = str_quote.replace("\n", "")
            str_quote = re.sub(remove_multiple_spaces, " ", str_quote)
            cur_quote["quote"] = str_quote.strip()

            all_quotes.append(cur_quote)

# Shuffle all quotes
shuffle(all_quotes)

# Dump the quotes
with open("data/quotes.json", "w+") as file:
    file.write(json.dumps(all_quotes, sort_keys=True, indent=4, separators=(',', ': ')))

