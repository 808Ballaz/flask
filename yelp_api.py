from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import os   # use this to import your secret keys

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_businesses(location, term):
	auth = Oauth1Authenticator(
		consumer_key=os.environ['consumer_key'],
		consumer_secret=os.environ['consumer_secret'],
		token=os.environ['token'],
		token_secret=os.environ['token_secret']
	)

	client = Client(auth)

	params = {
		'term': 'food',
		'lang': 'en',
		'limit': 10,
	}

	response = client.search(location, **params)

	business_list = []

	for business in response.businesses:     # note businesses is an attribute, not a function
		# print(business.name, business.rating, business.phone)
		business_list.append({"name": business.name,
			"rating": business.rating,
			"phone": business.phone
		})

	return business_list

businesses = get_businesses("Oakland",'food')

for business in businesses:
	print(business)
