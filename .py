import pandas as pd
import requests
from bs4 import BeautifulSoup
from csv import writer

bot = {'User-agent': 'your bot 0.1'}
base_url = 'https://www.theaa.com'
search_url = 'https://www.theaa.com/used-cars/displaycars?fullpostcode=mk18%201sf&travel=2000&page='
page_count = 1

listLinks = []
distanceList = []

for page_count in range(1, 3):
  page = requests.get(search_url + str(page_count), headers=bot).text
  soup = BeautifulSoup(page, 'html.parser')
  
  lists = soup.find_all('div', class_='vl-item clearfix')
  dis_lists = soup.find_all('div', class_='vl-location')
  
  for list in lists:
    link = list.find('a', class_='image-link').get('href')
    listLinks.append(base_url + link)

  for location in dis_lists:
    dist = location.find('strong', class_='strong-inline').get_text()
    distanceList.append(dist)
    
with open('carData.csv', 'w', encoding='utf8', newline='') as file:
  thewriter = writer(file)
  header = ['sales_title', 'price', 'mileage', 'year', 'fuel_type', 'transmission',
    'body_type', 'colour', 'doors', 'engine_size', 'co2_Emissions',
    'no_of_reviews', 'rating_value', 
  ]
  thewriter.writerow(header)
   
  for link in listLinks:
    res = requests.get(link, headers=bot).text
    soup_two = BeautifulSoup(res, 'html.parser')
    
    try:
      car_make = soup_two.find('span', class_='make').get_text()
      car_model = soup_two.find('span', class_='model').get_text()
      car_title = soup_two.find('span', class_='variant new-transport--regular').get_text()
      price = soup_two.find('strong', class_='total-price').get_text()

      #here I iterated the list to check for div elements that has the attr content
      no_of_reviews = [
        item['content']
        for item in soup_two.find_all('div', attrs={'content': True})
      ][1]

      rating_value = [
        item['content']
        for item in soup_two.find_all('div', attrs={'content': True})
      ][3]
   
      data = soup_two.find_all('span', class_='vd-spec-value')
      mileage = data[0].get_text()
      year = data[1].get_text()
      fuel_type = data[2].get_text()
      transmission = data[3].get_text()
      body_type = data[4].get_text()
      colour = data[5].get_text()
      doors = data[6].get_text()
      engine_size = data[7].get_text()
      co2_Emissions = data[8].get_text()

    except IndexError:
      car_make = ''
      car_model = ''
      car_title = ''
      mileage = ''
      year = ''
      fuel_type = ''
      transmission = ''
      body_type = ''
      colour = ''
      doors = ''
      engine_size = ''
      co2_Emissions = ''
      price = ''

    title = car_make + ' ' + car_model + ' ' + car_title

    content = {
      'sales_title': [title],
      'price': [price],
      'mileage': [mileage],
      'year': [year],
      'fuel_type': [fuel_type],
      'transmission': [transmission],
      'body_type': [body_type],
      'colour': [colour],
      'doors': [doors],
      'engine_size': [engine_size],
      'co2_Emissions': [co2_Emissions],
      'no_of_reviews': [no_of_reviews],
      'rating_value': [rating_value],
    }

    #READ DISTANCR AND STORE IN A DF USING PANDAS
    x = {'distance': distanceList}
    ds = pd.DataFrame(x)
    ds.to_csv('dsdata.csv', sep='\t', encoding='utf-8', index= False)


    ##thewriter.writerow(content)

df1 = pd.read_csv('sda_carDataSet.csv')

df2 = pd.read_csv('dsdata.csv')

print(df1)