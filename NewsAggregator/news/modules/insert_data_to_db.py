# from news.models import Companies, Vacancies
import sys
import os

p = os.path.dirname(__file__)
print(p)
sys.path.insert(
    0,
    "e:/ContectAggregator/NewsAggregator/NewsAggregator/news/modules/insert_data_to_db.py",
)
print(sys.path)

from NewsAggregator.news.models import Companies, Vacancies

# class insert_data_to_db:
#     def __init__(self):
#         super().__init__()
#         t = "string"
#         self.t = t

#     def test(self):
#         print(self.t)
