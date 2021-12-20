import requests
from bs4 import BeautifulSoup


def get_reviews(URL):
    """Takes in url, returns a list of dictionaries of reviews."""
    try:
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        results = soup.find("section", {"class": "lenderReviews"}) 
        
    # page reviews
        reviews_elements = results.find_all("div", {"class":"mainReviews"})

    # building a list of dictionaries of reviews from reviews parsed from page html
        reviews = []
        for review_element in reviews_elements:
            review = {}
            review['customer_name'] =  " ".join(review_element.find("p", {"class":"consumerName"}).text.split())
            review['review_title']= review_element.find("p", {"class":"reviewTitle"}).text.strip()
            review['review_text'] = review_element.find("p", {"class":"reviewText"}).text.strip()
            review['review_date']= review_element.find("p", {"class":"consumerReviewDate"}).text.strip()
            review['review_rating'] = review_element.find("div", {"class":"numRec"}).text.strip()
            reviews.append(review)
    
        return reviews
    except:
        return {'err': "Please enter a valid lender's name and or id"}


