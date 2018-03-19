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

            name = re.findall("titleBegin [\"\<\>a-zA-Z ,.\n\/?\-()0-9!:']+ titleEnd", text)
            name = name[0].replace("titleBegin -->", "").replace("<!-- titleEnd", "")

            content = re.findall("contentBegin [\"\<\>a-zA-Z ,.\n\/?\-()0-9!\t'=:%~_#\[\]\\\{\}\+]+ contentEnd", text)
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
with open("data.json", "w+") as file:
    file.write(json.dumps(dicts, sort_keys=True, indent=4, separators=(',', ': ')))
    file.close()
