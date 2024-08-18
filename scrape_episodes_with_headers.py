"""
CLASS FUNCTION:
Scrapes all of the episode titles and accompanying headers for tables
"""

# from scrape_cells_that_start_with import scrape_cells_that_start_with

import requests
from bs4 import BeautifulSoup

url = input("enter a Wikipedia episodes list URL: ")

# TESTING URLS
# url = "https://en.wikipedia.org/wiki/List_of_Sailor_Moon_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_M*A*S*H_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_The_Boys_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Ranma_%C2%BD_episodes"
# url = ""

response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Initialize a list to hold headers and tables
elements = []

# Iterate over all h2, h3, and table elements in the order they appear
current_h2 = None
current_h3 = None
for element in soup.find_all(['h2', 'h3', 'table']):
    if element.name == 'h2':
        current_h2 = element.get_text(strip=True)
        elements.append(('h2', current_h2))
    elif element.name == 'h3':
        current_h3 = element.get_text(strip=True)
        elements.append(('h3', current_h3))
    elif element.name == 'table' and current_h3:
        # title_column_list = scrape_cells_that_start_with(element, '"')
        title_column_list = []
        
        rows = element.find_all('tr')
        for row in rows:
            cells = row.find_all(['td', 'th'])
            # TRIPLE FOR LOOP TIME COMPLEXITY IS VERY BAD
            for cell in cells:
                text = cell.get_text(strip=True)
                if text.startswith('"'):
                    title_column_list.append(text)
        
        if title_column_list:
            elements.append(('table', title_column_list))

page_title = soup.find('h1').text # retrives title of page_title
output_file_name = page_title
output_file_name += " with headers.txt"

# output file string formatting options
# output_file_name = output_file_name.removeprefix("List of ")
output_file_name = output_file_name.replace(" ", "_")
# output_file_name = output_file_name.lower()

# Write the headers and table data to a text file
with open(output_file_name, 'w', encoding='utf-8') as file:
    for tag, content in elements:
        if (tag == 'h2' and
            content != "Contents" and
            content != "Series overview" and
            content != "Ratings" and
            content != "See also" and
            content != "Notes" and
            content != "References" and
            content != "External links"):
            
            # print(content)
            file.write(f"{content}\n") #don't include tag in output file
            file.write("\n")
            
        if tag ==  'h3':
            file.write(f"{content}\n") #don't include tag in output file
        if tag == 'table': #episode titles
            for item in content:
                file.write(f"{item}\n") #don't include tag in output file
            file.write("\n")

print()
print("Titles and headers have been written to '" + output_file_name + "'")

