"""
CLASS FUNCTION:
Scrapes all of the episode titles and accompanying headers for tables
"""

import requests
from bs4 import BeautifulSoup

# gets the first cell in a table that contains quotes at the start
# this corresponds to the cells that contain episodes
def get_cell_with_quotes(table):
    quote_cells = []
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['td', 'th'])
        # TRIPLE FOR LOOP TIME COMPLEXITY IS VERY BAD
        for cell in cells:
            text = cell.get_text(strip=True)
            if text.startswith('"'):
                quote_cells.append(text)
    return quote_cells

url = input("enter a Wikipedia episodes list URL: ")
# url = "https://en.wikipedia.org/wiki/List_of_Sailor_Moon_episodes"
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
        # current_h2 = element.get_text(strip=True).replace("[edit]", "")
        current_h2 = element.get_text(strip=True)
        elements.append(('h2', current_h2))
    elif element.name == 'h3':
        # current_h3 = element.get_text(strip=True).replace("[edit]", "")
        current_h3 = element.get_text(strip=True)
        elements.append(('h3', current_h3))
    elif element.name == 'table' and current_h3:
        third_column = get_cell_with_quotes(element)
        if third_column:
            elements.append(('table', third_column))

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
        if tag == 'h2':
            # file.write(f"{tag}: {content}\n") #includes tag in output file
            file.write(f"{content}\n") #don't include tag in output file
        if tag ==  'h3':
            # file.write(f"{tag}: {content}\n") #includes tag in output file
            file.write(f"{content}\n") #don't include tag in output file
        if tag == 'table': #episode titles
            # file.write("TABLE THIRD COLUMN:\n")
            for item in content:
                # file.write(f"{tag}: {item}\n") #includes tag in output file
                file.write(f"{item}\n") #don't include tag in output file
            file.write("\n")
            
print("Headers and tables have been written to '" + output_file_name + "'")

