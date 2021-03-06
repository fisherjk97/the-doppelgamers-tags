
  
# importing the module
import json
from typing import Set

hash_tags = ["#photomode", "doppelgamers", "virtualphotography", "smashbros", "smashbrosultimate", "switchshare"]
mentions = ["@NintendoAmerica", "@Sora_Sakurai"]

def read(file):
    # Opening JSON file
    data = []
    with open(file) as json_file:
        data = json.load(json_file)
    
        for d in data:
            print(d)

    return data

def generate_hash_tags(data):
    content = ""
    day_num = 1
    for d in data:
        content += "Day " + str(day_num) + " of photographing every #SmashBros character."
        content += " " + d["Message"].replace("{Name}", "#"+d["Name"])
        day_num = day_num + 1

        d = update(d)

        data = to_set(d["HashTags"])

        print(data)

        content += "\n"
        content += print_hashtags(d["HashTags"])
        content += "\n"
        content += print_mentions(d["Mentions"])
        content += "\n"
        content += "\n"
        print(content)

    return content


def format_games(games):

    elements = ['#{0}'.format(element).replace(" ", "").replace(".", "").replace("'","").lower() for element in games]
    return elements


def update(d):
    if "HashTags" not in d:
            d["HashTags"] = []

    if "Mentions" not in d:
        d["Mentions"] = []

    d["HashTags"].extend(format_games(d["Games"]))
    d["HashTags"].extend(hash_tags)
    d["Mentions"].extend(mentions)


    res = []
    [res.append(x) for x in d["HashTags"] if x not in res]
    d["HashTags"] = res

    return d


def to_set(hashtags):

    result = set()
    for h in hashtags:
       result.add(h)
    return result


def print_hashtags(hashtags):
    content = ""
    count = 0
    if(hashtags):
        for h in hashtags:
            if h:
                if not h.startswith("#", 0, 1):
                        h = "#" + h
                if count != 0:
                    content +=  " " + h
                else:
                    content += h
                count += 1
    return content


def print_mentions(mentions):
    content = ""
    count = 0
    if(mentions):
        for h in mentions:
            if not h.startswith("@", 0, 1):
                h = "@" + h
            if count != 0:
                content +=  " " + h
            else:
                content += h
            count += 1
    return content

def main():
    characters = read("characters.json")
    content = generate_hash_tags(characters)

    text_file = open("characters_twitter.txt", "wt")
    n = text_file.write(content)
    text_file.close()


if __name__ == "__main__":
    main()