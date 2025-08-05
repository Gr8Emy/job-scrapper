import requests
from bs4 import BeautifulSoup

url = "https://realpython.github.io/fake-jobs/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

job_elements = soup.find_all("div", class_="card-content")

print("Latest Job Listings:\n")

for job in job_elements[:10]:  # Get first 10 jobs
    title = job.find("h2", class_="title")
    company = job.find("h3", class_="company")
    location = job.find("p", class_="location")

    print(f"{title.text.strip()} at {company.text.strip()} – {location.text.strip()}\n")
