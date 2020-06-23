import json
import os
import random
import re

import boto3
from bs4 import BeautifulSoup

def create_blog_data():
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
    with open("site_data/blog_data.json", "w+") as file:
        file.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))


def create_random_quotes():
    # Create the quotes for the homepage
    with open("site_data/quotes.json", "r") as file:
        all_quotes = json.loads(file.read())

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
                cur_quote["author"] = media.get("author", "None")
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
    with open("site_data/random_quotes.json", "w+") as file:
        file.write(json.dumps(random_quotes, sort_keys=True, indent=4, separators=(",", ": ")))


def load_site_data():
    s3 = boto3.client("s3")

    DATA_DIR = "site_data"
    for filename in os.listdir(DATA_DIR):
        print(f"Loading {DATA_DIR}/{filename}")
        with open(f"{DATA_DIR}/{filename}", "rb") as file:
            resp = s3.put_object(
                ACL="public-read",
                Body=file.read(),
                Bucket="bhg5yd-personal-site",
                Key=filename,
            )


if __name__ == "__main__":
    create_blog_data()
    create_random_quotes()
    load_site_data()
