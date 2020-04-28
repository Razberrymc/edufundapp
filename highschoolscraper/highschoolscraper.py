from bs4 import BeautifulSoup
import requests
from random import randint
import time

url = 'https://www.collegesimply.com/k12/lists/public-high-schools/top-rated/state'

state_list = ["/alabama/", "/alaska/", "/arizona/", "/arkansas/", "/california/", "/colorado/", "/connecticut/", "/delaware/", "/florida/", "/georgia/", "/hawaii/", "/idaho/", "/illinois/", "/indiana/", "/iowa/", "/kansas/", "/kentucky/", "/louisiana/", "/maine/", "/maryland/", "/massachusetts/", "/michigan/", "/minnesota/", "/mississippi/", "/missouri/", "/montana/", "/nebraska/", "/nevada/", "/new-hampshire/", "/new-jersey/", "/new-mexico/", "/new-york/", "/north-carolina/", "/north-dakota/", "/ohio/", "/oklahoma/", "/oregon/", "/pennsylvania/", "/rhode-island/", "/south-carolina/", "/south-dakota/", "/tennessee/", "/texas/", "/utah/", "/vermont/", "/virginia/", "/washington/", "/west-virginia/", "/wisconsin/", "/wyoming/"]

school_list = []

school_name_list = []
location_list = []
rating_list = []
test_list = []

import csv

csvfile = open("highschooldata.csv", "w", newline="", encoding="utf-8")
c = csv.writer(csvfile)

c.writerow(["school name", "location", "state", "rating", "state test proficiency", "population", "graduation rate", "standardized test performance", "upperclassmen taking ACT or SAT","AP class enrollment rate","AP test pass rate","white student percentage","black student percentage","hispanic student percentage","asian pacific student percentage","native american indian student percentage","hawaiian pacific islander student percentage","two or more races student percentage"])


def get_info(state_url):
    #masterlist = []
    page = requests.get(url + state_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    nameinfo = soup.find_all('h4', class_="card-title mb-1", limit=3)
    for name in nameinfo:
        school = name.find('a')
        #school_name_list.append(school.get_text())
        #masterlist.append(school.get_text())
        #print(school.get_text())

    locationinfo = soup.find_all('div', class_="col ml-n2", limit=4)
    for location in locationinfo:
        place = location.find('p')
        #location_list.append(place.get_text())
        #masterlist.append(place.get_text())
        #print(place.get_text())

    ratinginfo = soup.find_all('ul', class_="list-unstyled small mb-0", limit=3)
    for rating in ratinginfo:
        number = rating.find('li')
        #rating_list.append(number.get_text())
        #masterlist.append(number.get_text())
        #print(number.get_text())

    #print("\n")

    testinfo = soup.find_all('ul', class_="list-unstyled small", limit=3)
    for test in testinfo:
        score = test.find('li')
        #test_list.append(score.get_text())
        #masterlist.append(score.get_text())
        #print(score.get_text())

    #print("\n")

    linkinfo = soup.find_all('h4', class_="card-title mb-1", limit=3)
    for link in linkinfo:
        school_list.append(link.a.get('href'))

    #c.writerow(masterlist)

for state in state_list:
    get_info(state)




population_list = []
grad_rate_list = []
standard_test_list = []
test_participation_list = []
ap_list = []
ap_pass_list = []
white_student_percentage_list = []
black_student_percentage_list = []
hispanic_student_percentage_list = []
asian_pacific_student_percentage_list = []
native_american_indian_student_percentage_list = []
hawaiian_pacific_islander_student_percentage_list = []
two_or_more_races_student_percentage_list = []


def get_data(school_url):
    masterlist = []
    page = requests.get('https://www.collegesimply.com' + school_url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #find school name
    name_info = soup.find('h1', id='headerTitle')
    try:
        masterlist.append(name_info.get_text())
    except:
        masterlist.append("N/A")

    #find location
    location_info = soup.find('span', itemprop='addressLocality')
    try:
        masterlist.append(location_info.get_text())
    except:
        masterlist.append("N/A")

    #find state
    whichstate = soup.find('span', itemprop='addressRegion')
    try:
        masterlist.append(whichstate.get_text())
    except:
        masterlist.append("N/A")

    #find rating
    rating_info = soup.find_all('span', class_='display-3 mb-0')
    try:
        masterlist.append(rating_info[1].text.strip())
    except:
        masterlist.append("N/A")

    #find state test proficiency
    test_info = soup.find_all('span', class_='display-3 mb-0')
    try:
        masterlist.append(test_info[5].text.strip())
    except:
        masterlist.append("N/A")

    #find population
    population = soup.find('span', class_="display-3 mb-0")
    try:
        population_list.append(population.get_text())
        masterlist.append(population.get_text())
    except:
        population_list.append("N/A")
        masterlist.append("N/A")

    #find graduation rate
    grad_rate = soup.find_all('span', class_='display-3 mb-0')
    try:
        grad_rate_list.append(grad_rate[3].text.strip())
        masterlist.append(grad_rate[3].text.strip())
    except:
        grad_rate_list.append("N/A")
        masterlist.append("N/A")

    #find standardized test performance
    standard_test = soup.find_all('span', class_='display-3 mb-0')
    try:
        standard_test_list.append(standard_test[5].text.strip())
        masterlist.append(standard_test[5].text.strip())
    except:
        standard_test_list.append("N/A")
        masterlist.append("N/A")

    #find upperclassmen taking ACT or SAT
    test_participation = soup.find_all('span', class_='display-3 mb-0')
    try:
        test_participation_list.append(test_participation[7].text.strip())
        masterlist.append(test_participation[7].text.strip())
    except:
        test_participation_list.append("N/A")
        masterlist.append("N/A")

    #find AP class enrollment rate
    ap = soup.find_all('span', class_='display-3 mb-0')
    try:
        ap_list.append(ap[9].text.strip())
        masterlist.append(ap[9].text.strip())
    except:
        ap_list.append("N/A")
        masterlist.append("N/A")

    #find AP test pass rate
    ap_pass = soup.find_all('td', class_='table-value')
    try:
        ap_pass_list.append(ap_pass[36].text.strip())
        masterlist.append(ap_pass[36].text.strip())
    except:
        ap_pass_list.append("N/A")
        masterlist.append("N/A")

    #racial demographics

    #find white student percentage
    white_student_percentage = soup.find_all('td')
    try:
        white_student_percentage_list.append(white_student_percentage[15].text.strip())
        masterlist.append(white_student_percentage[15].text.strip())
    except:
        white_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    #find black student percentage
    black_student_percentage = soup.find_all('td')
    try:
        black_student_percentage_list.append(black_student_percentage[18].text.strip())
        masterlist.append(black_student_percentage[18].text.strip())
    except:
        black_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    #find hispanic student percentage
    hispanic_student_percentage = soup.find_all('td')
    try:
        hispanic_student_percentage_list.append(hispanic_student_percentage[21].text.strip())
        masterlist.append(hispanic_student_percentage[21].text.strip())
    except:
        hispanic_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    #find asian pacific student percentage
    asian_pacific_student_percentage = soup.find_all('td')
    try:
        asian_pacific_student_percentage_list.append(asian_pacific_student_percentage[24].text.strip())
        masterlist.append(asian_pacific_student_percentage[24].text.strip())
    except:
        asian_pacific_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    #find native american indian student percentage
    native_american_indian_student_percentage = soup.find_all('td')
    try:
        native_american_indian_student_percentage_list.append(native_american_indian_student_percentage[27].text.strip())
        masterlist.append(native_american_indian_student_percentage[27].text.strip())
    except:
        native_american_indian_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    #find hawaiian pacific islander student percentage
    hawaiian_pacific_islander_student_percentage = soup.find_all('td')
    try:
        hawaiian_pacific_islander_student_percentage_list.append(hawaiian_pacific_islander_student_percentage[30].text.strip())
        masterlist.append(hawaiian_pacific_islander_student_percentage[30].text.strip())
    except:
        hawaiian_pacific_islander_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    #find two or more races student percentage
    two_or_more_races_student_percentage = soup.find_all('td')
    try:
        two_or_more_races_student_percentage_list.append(two_or_more_races_student_percentage[33].text.strip())
        masterlist.append(two_or_more_races_student_percentage[33].text.strip())
    except:
        two_or_more_races_student_percentage_list.append("N/A")
        masterlist.append("N/A")

    c.writerow(masterlist)


for school in school_list:
    get_data(school)

#masterlist = zip(school_name_list, location_list, rating_list, test_list, population_list, grad_rate_list, standard_test_list, test_participation_list, ap_list, ap_pass_list, white_student_percentage_list, black_student_percentage_list, hispanic_student_percentage_list, asian_pacific_student_percentage_list, native_american_indian_student_percentage_list, hawaiian_pacific_islander_student_percentage_list, two_or_more_races_student_percentage_list)

#import csv

#with open(newfilePath, "w") as f:
    #writer = csv.writer(f)
    #for row in masterlist:
        #writer.writerow(row)

csvfile.close()
