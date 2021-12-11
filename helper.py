import requests
from bs4 import BeautifulSoup


def get_reviews(URL):
    """Takes in url, returns a list of dictionaries of reviews."""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find("section", {"class": "lenderReviews"})

    if results is None:
        return {'err':"Please enter a valid lender's name and or id"}

    reviews_elements = results.find_all("div", class_="mainReviews")


    reviews = []
    for review_element in reviews_elements:
        review = {}
        review['Customer_Name'] =  " ".join(review_element.find("p", class_="consumerName").text.split())
        review['Review_Title']= review_element.find("p", class_="reviewTitle").text.strip()
        review['Review_Text'] = review_element.find("p", class_="reviewText").text.strip()
        review['Review_Date']= review_element.find("p", class_="consumerReviewDate").text.strip()
        review['Review_Rating'] = review_element.find("div", class_="numRec").text.strip()
        reviews.append(review)
    
    return reviews


# if I need to use urllib3
# import urllib3
# http = urllib3.PoolManager()
# page = http.request("GET", URL).data
# soup = BeautifulSoup(page, "html.parser")
