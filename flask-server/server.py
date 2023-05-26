from flask import Flask
from serpapi import GoogleSearch

params = {
  "engine": "google",
  "q": "Mobile",
  "api_key": "e2a30aecb963d2caeb1fd6303c6c45ed641ec2df5a87afca772e7c0e63c37df7"
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]

app = Flask(__name__)

#Members API Route

@app.route("/members")
def members():
    return {"members": [organic_results[1]['title'], organic_results[2]['title'], organic_results[0]['title']]}

if __name__ == "__main__":
    app.run(debug=True)