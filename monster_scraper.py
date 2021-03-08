import requests
from pprint import pprint
from bs4 import BeautifulSoup


URL = 'https://www.monster.com/jobs/search/?q=Software-Developer&where=Australia'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id='ResultsContainer')

job_elems = results.find_all('section', class_='card-content')

#find all available software jobs in the link specified
for job_elem in job_elems:
    #print(job_elem, end='\n'*2)
    # logo_elem = job_elem.find('img')['src']
    title_elem = job_elem.find('h2', class_='title')
    company_elem = job_elem.find('div', class_='company')
    location_elem = job_elem.find('div', class_='location')
    if None in (title_elem, company_elem, location_elem):
        continue
    # print(logo_elem)
    print(title_elem.text.strip())
    print(company_elem.text.strip())
    print(location_elem.text.strip())
    print()


#python jobs only with links
# python_jobs = results.find_all('h2', string='Python Developer')
python_jobs = results.find_all('h2', string=lambda text: 'test' in text.lower())

for p_job in python_jobs:
    link = p_job.find('a')['href']
    print(p_job.text.strip())
    print(f"Apply here: {link}\n")

#print(results.prettify())

#Whole board class="page-content" id="mainContent

#logo = class = div.mux-company-logo.thumbnail
#logo = class = title  = class = company    = class = location
#<time datetime="2017-05-26T12:00">25 days ago</time>
# class="card-content"

