import urllib.request
import urllib.parse
import requests
import re
import csv

url1 = "/w/index.php?title=%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"

def read_url(page_text):
    # look for the next URL
    index1 = page_text.find("Следующая страница")
    assert(index1 >= 0)
    if (index1 == 0) or (page_text[index1-1] == "("):
        #print("End of chain")
        return ""
    index2 = page_text.rfind("href=", 0, index1)
    assert(index2 >= 0)
    # the next URL is between the next two quote characters
    quote1 = page_text.find("\"", index2+1)
    quote2 = page_text.find("\"", quote1+1)
    assert(quote1 >= 0)
    assert(quote2 >= 0)
    s = decoded_content[quote1+1:quote2]
    s = s.replace("&amp;", "&")
    return s
    

url = url1
i = 1

dictionary = {}

while url != "":
    urlenc = "https://ru.wikipedia.org/" + url
    try:
        with requests.get(urlenc) as response:
            decoded_content = response.text  # Reads the content as bytes
            url = read_url(decoded_content)

            tmp = decoded_content.find("mw-category mw-category-columns")

            list_begin = decoded_content[tmp:].find("<ul>") + tmp
            list_end = decoded_content[tmp:].find("</ul>") + tmp
            
            
            positions = [match.start() for match in re.finditer('title="', decoded_content[list_begin:list_end])]
            positions = list(map(lambda x:x+list_begin, positions))
            #print(len(positions))

            for pos in positions:
                letter = decoded_content[pos+7]
                if letter in dictionary.keys():
                    dictionary[letter] += 1
                else:
                    dictionary[letter] = 1
            

            


            
    except urllib.error.URLError as e:
        print(f"Error accessing URL: {e.reason}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    #print("Next URL=", url)
    i += 1

#print(dictionary)

# CSV file name
csv_filename = "beasts.csv"
with open(csv_filename, 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(dictionary.items())
csvfile.close()



