"""
CLASS FUNCTION:
Scrapes all of the episode titles and accompanying headers for tables
"""

import requests
from bs4 import BeautifulSoup

# TESTING URLS
# url = "https://en.wikipedia.org/wiki/List_of_Sailor_Moon_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_M*A*S*H_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_The_Boys_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Ranma_%C2%BD_episodes"
# url = ""

url = input("enter a Wikipedia episodes list URL: ")

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

page_title = soup.find('h1').text # retrives title of page_title
output_file_name = page_title
output_file_name += " with headers.txt"

# output file string formatting options
# output_file_name = output_file_name.removeprefix("List of ")
# output_file_name = output_file_name.replace(" ", "_")
# output_file_name = output_file_name.lower()

# Write the headers and table data to a text file
with open(output_file_name, 'w') as file:
    for element in soup.find_all(['h2', 'h3', 'h4', 'th', 'td']):
        tag = element.name
        text = element.get_text(strip=True)
        
        if tag == 'h2':
            file.write("" + text + '\n')
        elif tag == 'h3':
            file.write(" " + text + '\n')
        elif tag == 'h4':
            file.write("  " + text + '\n')
        elif tag == 'th' or tag == 'td':
            if text.startswith('"'):
                file.write("   " + text + '\n')

print()
print("Titles and headers have been written to '" + output_file_name + "'")

