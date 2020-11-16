import requests
from bs4 import BeautifulSoup
import cssutils


class Parser:
    def __init__(self):
        super().__init__()

    def get_data(self):
        JobsVacancy_r = requests.get("https://jobs.ge/?page=1&q=&cid=6&lid=&jid=")
        JobsVacancy_soup = BeautifulSoup(JobsVacancy_r.content, "html5lib")
        jobs_headings = JobsVacancy_soup.findAll("div", {"class": "regularEntries"})

        job_links = []
        job_names = []
        companies_names = []
        start_dates = []
        end_dates = []
        result = {
            "job_names": job_names,
            "job_links": job_links,
            "companies_names": companies_names,
            "start_dates": start_dates,
            "end_dates": end_dates,
        }
        k = 1
        for job in jobs_headings:
            jobNames = job.find_all("a", {"class": "vip"})
            companies = job.find_all("td")

            for company in companies:
                if k % 6 == 2:
                    job_title = company.find_all("a", {"class": "vip"})[0].text
                    job_names.append(job_title)

                    job_link = "https://jobs.ge/" + company.find("a")["href"]
                    job_links.append(job_link)

                elif k % 6 == 4:
                    company_name = ""
                    if company.find("a"):
                        companies_name = " ".join(str(company.find("a").text).split())
                    else:
                        companies_name = " ".join(str(company.text).split())
                    companies_names.append(companies_name)
                elif k % 6 == 5:
                    start_date = " ".join(str(company.text).split())
                    start_dates.append(start_date)
                elif k % 6 == 0:
                    end_date = " ".join(str(company.text).split())
                    end_dates.append(end_date)

                k += 1
            # print(len(result["companies_names"]))
            # print(len(result["job_names"]))
            # print(len(result["job_links"]))
            # print(len(result["start_dates"]))
            # print(len(result["end_dates"]))
            # print("k==" + str(k))
            return result


p = Parser()
p.get_data()