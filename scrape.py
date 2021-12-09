import requests
from bs4 import BeautifulSoup
import json

URL = 'https://www.lendingtree.com/reviews/personal/first-midwest-bank/52903183'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("section", {"class": "lenderReviews"})
reviews_elements = results.find_all("div", class_="mainReviews")

reviews = []
for review_element in reviews_elements:
    review = {}
    review['review_title']= review_element.find("p", class_="reviewTitle").text .strip()
    review['review_text'] = review_element.find("p", class_="reviewText").text .strip()
    review['customer_name'] = review_element.find("p", class_="consumerName").text .strip()
    review['review_date']= review_element.find("p", class_="consumerReviewDate").text .strip()
    review['review_rating'] = review_element.find("div", class_="numRec").text .strip()
    reviews.append(review)
    print('hellooooooooo---->>>>>>>>>>>>', review)
  

# print('reviews------>>>>', reviews)
reviews_json = json.dumps(reviews)
print('reviews------>>>>', reviews_json)



