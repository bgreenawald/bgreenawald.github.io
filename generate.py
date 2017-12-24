import re
import json
import os

# Create an object to hold our JSON file
dicts = []

# Iterate through all blog files
for subdir, dirs, files in os.walk("blog"):
    for file in files:
        with open(subdir + os.sep + file) as file_name:

            # For each file, get the necesary info and append to our dict
            text = file_name.read()

            name = re.findall("name = .+;", text)
            name = name[0].replace("name = \"", "").replace("\";", "")

            content = re.findall("content = [\"\<\>a-zA-Z ,.\n\/?\-()0-9!']+;", text)
            content = content[0].replace("content = \"", "").replace("\";", "")

            date = re.findall("date = .+;", text)
            date = date[0].replace("date = \"", "").replace("\";", "")

            path = re.findall("path = .+;", text)
            path = path[0].replace("path = \"", "").replace("\";", "")

            dicts.append({"name": name, "content": content, "date": date, "location": path})
            file_name.close()

# Write the file to the json object
with open("data.json", "w+") as file:
    file.write(json.dumps(dicts))
    file.close()
