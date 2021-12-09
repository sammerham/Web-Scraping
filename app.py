from flask import Flask
from flask.json import jsonify
from helper import get_reviews
app = Flask(__name__)

BASE_URL = 'https://www.lendingtree.com/reviews/personal/'

@app.route('/reviews/<lender_name>/<int:lender_id>')
def show_reviews(lender_name, lender_id):
    """
    Handles GET requests like /reviews/lender_name/lender_id
    Returns JSON format of Reviews for lender provided in url path
    """

    lender=f"{lender_name}/{lender_id}"
    url = f"{BASE_URL}{lender}"
    reviews = get_reviews(url)  

    return jsonify({'Reviews':reviews})

