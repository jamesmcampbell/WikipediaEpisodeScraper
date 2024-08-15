import requests
from bs4 import BeautifulSoup

url = input("enter a Wikipedia episodes list URL: ")
#url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"

response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

links = []

with open("episodes.txt", "w", encoding="utf-8") as f:
    for element in soup.find_all(['table']):
        trs = element.find_all('tr');
        for tr in trs:
            ths = tr.find_all(['th'])
            for th in ths:
                th_text = th.get_text(strip=True)
                links.append(f"{th_text}")
                print(th_text)
                
                
            tds = tr.find_all(['td'])
            for td in tds:
                td_text = td.get_text(strip=True)
                links.append(f"    {td_text}")
                print(td_text)
                f.write(f"{td_text}\n")
                
                
                anchors = td.find_all('a')
                for anchor in anchors:
                    link = anchor.get('href')
                    if link:
                        #print(link)
                        links.append(f"        https://en.wikipedia.org{link}")

#this section will be used to find the episode list link if there are not episodes listed in the current wikipedia article
with open('links.txt', 'w', encoding='utf-8') as file:
    for link in links:
        file.write(f"{link}\n")

print("Links have been written to links.txt")