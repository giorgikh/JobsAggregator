from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import cssutils

# # PalitraNews
# toi_r = requests.get("https://palitranews.ge/category/news")
# toi_soup = BeautifulSoup(toi_r.content, "html5lib")
# toi_headings = toi_soup.findAll(
#     "a", {"class": "col-md-3 col-sm-12 col-xs-12 newsblockcol"}
# )
# # toi_headings = toi_headings[0:-13]  # removing footers
# palitra_news = []
# palitraNewsCount = 0

# for th in toi_headings:
#     if palitraNewsCount == 4:
#         break
#     Palitralink = th.attrs["href"]
#     PalitraText = th.find("p").text
#     PalitraDate = th.find("span").text
#     palitra_news.append(
#         {
#             "PalitraText": PalitraText,
#             "Palitralink": Palitralink,
#             "PalitraDate": PalitraDate,
#         }
#     )
#     palitraNewsCount += 1


# # Imedi News
# ImediNews_r = requests.get("https://imedinews.ge/ge/all-news")
# ImediNews_soup = BeautifulSoup(ImediNews_r.content, "html5lib")
# ImediNews_headings = ImediNews_soup.findAll("a", {"class": "single-item"})
# ImediNews_headings = ImediNews_headings[0:-1]
# imedi_news = []
# Newscount = 0
# for imediNews in ImediNews_headings:
#     if Newscount == 4:
#         break
#     start = int(str(imediNews).find("background-image:url('")) + 22
#     end = int(str(imediNews).find(")")) - 1
#     # print(str(imediNews)[start:end])
#     imgurl = str(imediNews)[start:end]
#     link = imediNews.attrs["href"]
#     text = imediNews.find("h3").text
#     date = imediNews.find("p", {"class": "date"}).text
#     imedi_news.append({"link": link, "text": text, "imgurl": imgurl, "date": date})
#     Newscount += 1

# jobs.ge
# from modules.insertInformation import insertInformation
# JobsVacancy_r = requests.get("https://jobs.ge/?page=1&q=&cid=6&lid=&jid=")
# JobsVacancy_soup = BeautifulSoup(JobsVacancy_r.content, "html5lib")
# jobs_headings = JobsVacancy_soup.findAll("div", {"class": "regularEntries"})

# num = 0
# for job in jobs_headings:
#     # t = job.find("a", {"class": "vip"})
#     # link = job.attrs["href"]
#     jobName = job.find_all("a", {"class": "vip"})
#     for i in jobName:
#         lk = i.attrs["href"]

#         print("https://jobs.ge" + lk)
#         exit()
from news.modules.parser import Parser
from news.models import Vacancies

listLen = 0


def getData():
    result = Parser()
    result = result.get_data()
    job_names = result["job_names"]
    job_links = result["job_links"]
    companies_names = result["companies_names"]
    start_dates = result["start_dates"]
    end_dates = result["end_dates"]
    data = zip(job_links, job_names, companies_names, start_dates, end_dates)
    listLen = len(companies_names)
    return data


# from models import Companies
def insert_data_db(listLen):
    Vacancies.objects.all().delete()
    for i in range(listLen):
        # company = " ".join(str(companies_name[i]["company_name"]).split())
        # if company != "":
        # if company not in inserted_list:
        c = Vacancies(
            job_title=job_names[i],
            job_link=job_links[i],
            job_start_date=start_dates[i],
            job_end_date=end_dates[i],
            job_company=companies_names[i],
        )
        # inserted_list.append(company)
        c.save()
        # v = Vacancies(vacancy_title=,vacancy_desc=,vacancy_company=id)


def index(request):
    data = getData()
    insert_data_db(listLen)
    return render(
        request,
        "news/index.html",
        {
            "data": data,
        },
    )


#    "job_names": job_names,
#             "job_links": job_links,
#             "companies_names": companies_names,
#             "start_dates": start_dates,
#             "end_dates": end_dates,
#             "ranges": ranges,