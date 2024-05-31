import requests
from bs4 import BeautifulSoup

base_url = "https://www.nytimes.com/"
r = requests.get(base_url)
r_html = r.text
titles = []
soup = BeautifulSoup(r_html, features="html.parser")

for i in soup.find_all("h2","css-1vvhd4r e1voiwgp0"):
    titles.append(i.text)

#ask the user to specify the name of the output file that will be saved
file_name = input("Name the file you want to save the output to with .txt extension: ")

#write the results to a txt file
with open(file_name, 'w') as file:
    for title in titles:
        file.write(title + '\n')

print("Result are in " + file_name)