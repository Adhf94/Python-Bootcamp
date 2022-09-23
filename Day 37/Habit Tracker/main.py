import requests
import datetime as dt



#Pïxela endpoint
url = "https://pixe.la/v1/users"
#Username, and password
USERNAME = "USERNAME"
TOKEN = "TOKEN"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url, json=user_params)
# print(response.text)

#Graph endpoint
graph_endpoint = f"{url}/{USERNAME}/graphs"
GRAPH_ID = "agraph1"
graph_config = {
    "id": GRAPH_ID,
    "name": "My graph",
    "unit": "Habit Day",
    "type": "int",
    "color": "sora",
}

#PROVIDE HEADER KEY
headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#Updating GRAPH
today = dt.datetime.today().strftime("%Y%m%d")
graph_post = f"{graph_endpoint}/{GRAPH_ID}"


request_body = {
    "date": today,
    "quantity": "2",

}

# response = requests.post(graph_post, json=request_body, headers=headers)
# print(response.text)
# response = requests.delete(graph_post, json=request_body, headers=headers)
# print(response.text)
