import json
import random
import re

from bs4 import BeautifulSoup

# Read in all of the quotes from local.
with open("content/favorite_quotes.html", "r", encoding="utf-8") as file:
    quote_text = file.read()

# Parse the quote with Beautiful Soup
quote_body = BeautifulSoup(quote_text, "html.parser").body

# Compile the regular expression for removal of multiple spaces.
remove_multiple_spaces = re.compile("[ ]+")

# Compile regex to get additional information
additional_info_match = re.compile("<i>.+</i>$")

# Iterate over every section in the body, skipping the first as that is the
# selection section
all_quotes = {}
for section in quote_body.find("div", {"id": "wrapper"}).find_all("section", recursive=False)[1:]:
    content_type = section.get("id", "none")
    cur_content = []

    # For section, iterate over all subsections
    for subsection in section.find_all("section"):
        cur_elem = {}

        cur_elem["id"] = subsection.get("id", "misc")

        # Extract out the title of the media, or make it 'Miscellaneous'
        cur_elem["title"] = subsection.h2.text if subsection.h2 else "Miscellaneous"

        # Extract out the author of the media, else make is 'None'
        cur_elem["author"] = subsection.h3.text if subsection.h3 else "None"

        cur_quotes = []

        # Iterate over all of the quotes with the appropriate classname
        for quote in subsection.find_all("li"):
            cur_quote = {}

            # Clean up the quote and store
            str_quote = " ".join([str(x) for x in quote.contents])
            str_quote = str_quote.replace("\n", "")
            str_quote = re.sub(remove_multiple_spaces, " ", str_quote)
            cur_quote["quote"] = str_quote.strip()

            # Extract additional information
            additional_info = additional_info_match.findall(cur_quote["quote"])

            if len(additional_info) > 1:
                raise ValueError("Found more than one possible match.")
            elif len(additional_info) == 1:
                cur_quote["quote"] = re.sub(additional_info_match, "", cur_quote["quote"]).strip()
                cur_quote["additional_information"] = additional_info[0].replace("<i>", "").replace("</i>", "")

            # Add in whether the quote is of class random
            cur_quote["random"] = True if quote.get("class", None) == ["random"] else False

            cur_quotes.append(cur_quote)

        cur_elem["quotes"] = cur_quotes
        cur_content.append(cur_elem)


    all_quotes[content_type] = cur_content

# Dump the quotes
with open("site_data/temp_quotes.json", "w+") as file:
    file.write(json.dumps(all_quotes, sort_keys=True, indent=4, separators=(",", ": ")))


# Create the quotes for the homepage

# Iterate over all types
random_quotes = []
for content_type in all_quotes:
    type_ = content_type.replace("_", " ")
    type_ = type_ if type_ != "self" else "other"

    for media in all_quotes[content_type]:
        for quote in media["quotes"]:
            # Skip any quotes not marked random
            if not quote["random"]:
                continue
            cur_quote = {}
            cur_quote["author"] = media["author"]
            cur_quote["title"] = media["title"]
            if "additional_information" in quote:
                quote_text = f"{quote['quote']} <i>{quote['additional_information']}</i>"
            else:
                quote_text = quote["quote"]
            cur_quote["quote"] = quote_text
            cur_quote["type"] = type_

            random_quotes.append(cur_quote)

random.shuffle(random_quotes)

# Dump the quotes
with open("temp_random_quotes.json", "w+") as file:
    file.write(json.dumps(random_quotes, sort_keys=True, indent=4, separators=(",", ": ")))
