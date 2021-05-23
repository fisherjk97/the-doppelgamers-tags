
  
# importing the module
import json

constant_hash_tags = ["#photomode", "doppelgamers", "virtualphotography" ]
constant_mentions = ["@NintendoOfAmerica", "@Sora_Sakurai"]

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
        content += " " + d["Message"]
        day_num = day_num + 1
        content += "\n"
        
        content += add_hashtags(constant_hash_tags)
        content += add_hashtags(constant_mentions)
        if "HashTags" in d:
            content += add_hashtags(d["HashTags"])

        content += "\n"
        print(content)

    return content


def add_hashtags(hashtags):
    content = ""
    count = 0
    if(hashtags):
        for h in hashtags:
            if count == 0:
                content +=  h
            else:
                content += " " + h
            count += 1
        content += "\n"
    return content

def main():
    characters = read("characters.json")
    content = generate_hash_tags(characters)

    text_file = open("characters_twitter.txt", "wt")
    n = text_file.write(content)
    text_file.close()


if __name__ == "__main__":
    main()