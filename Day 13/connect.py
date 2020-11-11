import os
import requests
import pandas as pd
import pprint
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('API_KEY')
api_token = os.getenv('API_ACCESS_TOKEN')

headers = {
    'Authorization': f'Bearer {api_token}',
    'Content-Type': 'application/json;charset=utf-8'
}

api_version = 4
search_query = "Anaconda"

api_base_url = f"https://api.themoviedb.org/{api_version}"
endpoint_path = f"/search/movie"
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"



# Using Api v 4
r = requests.get(endpoint, headers=headers)
if r.status_code in range(200, 299):
    data = r.json()
    results = data['results']
    if len(results) > 0:
        movie_ids = set()
        for result in results:
            _id = result['id']
            movie_ids.add(_id)


# Using API v 3
output_file = "movies.csv"
movie_data =[]

for movie_id in movie_ids:
    api_version = 3
    api_base_url = f"https://api.themoviedb.org/{api_version}"
    endpoint_path = f"/movie/{movie_id}"
    endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}"
    r = requests.get(endpoint)
    if r.status_code in range(200,299):
        data = r.json()
        movie_data.append(data)

fd = pd.DataFrame(movie_data)
fd.to_csv(output_file, index="False")