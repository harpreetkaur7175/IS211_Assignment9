import requests
from bs4 import BeautifulSoup

URL = "http://www.footballlocks.com/nfl_point_spreads.shtml"

def main():
   response = requests.get(URL)
   soup = BeautifulSoup(response.text, features="lxml")

   # Specify details of the table I want
   tables = soup.find_all('table', cols="4", width="580")
   print(f"How many tables? {len(tables)}")

   # find all the rows in that table
   rows = tables[0].find_all("tr")

   # Print the spreads
   header = True
   for row in rows:
       cells = row.find_all("td")
       if header:
           header = False
           continue

       favorite = cells[1].text.replace("At ", "")
       underdog = cells[3].text.replace("At ", "")
       spread = float(cells[2].text)
       print(f"Favorite = {favorite}, Underdog = {underdog}, Spread = {spread}")


if __name__ == "__main__":
   main()

