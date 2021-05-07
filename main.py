import requests
from datetime import datetime

TOKEN = "rteyugdhjkeiyefbj"
USER_NAME = "amdonatusprince"
GRAPH_ID = "graph1"
TODAY = datetime.now()
print(TODAY)

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"
create_pixel_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}"
update_pixel_enpoint = f"{pixela_endpoint}/{USER_NAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"


user_param = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_param = {
    "id": GRAPH_ID,
    "name": "Coding Habit Tracker",
    "unit": "hours",
    "type": "int",
    "color": "sora"
}

pixel_param = {
    "date": TODAY.strftime("%Y%m%d"),
    "quantity": input("How many hours did you code today? ")
}
update_pixel_param = {
    "quantity": "14"
}

# create_user_response = requests.post(url=pixela_endpoint, json=user_param)
# create_graph_response = requests.post(url=graph_endpoint, json=graph_param, headers=headers)
#create_pixel_response = requests.post(url=create_pixel_endpoint, json=pixel_param, headers=headers)
# update_pixel_response = requests.put(url=update_pixel_enpoint, json=update_pixel_param, headers=headers)
# delete_pixel_response = requests.delete(url=update_pixel_enpoint, json=update_pixel_param, headers=headers)

#print(create_pixel_response.text)
