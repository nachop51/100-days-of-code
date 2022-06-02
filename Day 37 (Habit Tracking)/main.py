import requests
from datetime import datetime


token = "your token here"
username = "your username here"  # this is the username you use to login to pixela
graph_id = "graph1"
# In order to create a new user, you need to send a POST request to the following URL:
# this is the endpoint for creating a new user
pixela_endpoint = 'https://pixe.la/v1/users'

# user_params = {
#     "token": token,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }

# response = requests.post(pixela_endpoint, json=user_params)
# check the response with the following command:
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

# graph_config = {
#     "id": "graph1",
#     "name": "My first graph",
#     "unit": "Count",
#     "type": "float",
#     "color": "ajisai",
# }

# In order to authenticate to pixela, you need to send a POST request to the following URL:
headers = {
    "X-USER-TOKEN": token,
}

# response = requests.post(
#     url=graph_endpoint, json=graph_config, headers=headers)

# print(response.text)

# To add values to the graph we can use the following endpoint with that configuration:
# post_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/"

# this is the date in the format of YYYYMMDD
date = datetime.now().strftime("%Y%m%d")

date = str(int(date) - 1)

# post_config = {
#     "date": date,
#     "quantity": "1",
# }

# response = requests.post(post_endpoint, json=post_config, headers=headers)

# print(response.text)

# Update using PUT request
# update_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"

# update_config = {
#     "date": date,
#     "quantity": "2",
# }

# response = requests.put(update_endpoint, json=update_config, headers=headers)

# print(response.text)

# Delete enpoints using DELETE request
delete_endpoint = f"{pixela_endpoint}/{username}/graphs/{graph_id}/{date}"

response = requests.delete(delete_endpoint, headers=headers)

print(response.text)
