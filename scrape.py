import requests
from bs4 import BeautifulSoup
    
def extract_third_column(table):
    quote_cells = []
    rows = table.find_all('tr')
    for row in rows:
        cells = row.find_all(['td', 'th'])
        for cell in cells:
            text = cell.get_text(strip=True)
            if text.startswith('"'):
                quote_cells.append(text)
    return quote_cells

# URL of the Wikipedia page
url = input("enter a Wikipedia episodes list URL: ")
# url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Sailor_Moon_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_M*A*S*H_episodes"
# url = "https://en.wikipedia.org/wiki/List_of_Breaking_Bad_episodes"
# url = ""

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Initialize a list to hold headers and tables
headers = []

# Iterate over all h2, h3, and table elements in the order they appear
current_h2 = None
current_h3 = None
for element in soup.find_all(['h2', 'h3', 'table']):
    if element.name == 'h2':
        current_h2 = element.get_text(strip=True).replace("[edit]", "")
        headers.append(('h2', current_h2))
    elif element.name == 'h3':
        current_h3 = element.get_text(strip=True).replace("[edit]", "")
        headers.append(('h3', current_h3))
    elif element.name == 'table' and current_h3:
        third_column = extract_third_column(element)
        if third_column:
            headers.append(('table', third_column))

# Write the headers and table data to a text file
with open('headers_and_tables.txt', 'w', encoding='utf-8') as file:
    for tag, content in headers:
        if tag == 'h2':
            # file.write(f"{tag}: {content}\n") #includes tag in output file
            file.write(f"{content}\n") #don't include tag in output file
        if tag ==  'h3':
            # file.write(f"{tag}: {content}\n") #includes tag in output file
            file.write(f"{content}\n") #don't include tag in output file
        if tag == 'table': #episode titles
            #file.write("TABLE THIRD COLUMN:\n")
            for item in content:
                # file.write(f"{tag}: {item}\n") #includes tag in output file
                file.write(f"{item}\n") #don't include tag in output file
            file.write("\n")
            
print("Headers and tables have been written to headers_and_tables.txt")
