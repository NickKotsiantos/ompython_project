from flask import Flask, render_template, url_for, request
import yelp_api
app = Flask(__name__)

@app.route("/")
def index():
    address = request.values.get('address')
    term = request.values.get('term')
    if address:
    	businesses = yelp_api.yelp_search(address, term)
    	business_1 = businesses[0]
    	business_2 = businesses[1]
    	business_3 = businesses[2]
    else:
    	businesses = None
    	business_1 = None
    	business_2 = None
    	business_3 = None
    return render_template('index.html', businesses=businesses, address=address,
    	business_1=business_1, business_2=business_2, business_3=business_3)

@app.route("/about")
def about():
	return render_template('about.html')


if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)




