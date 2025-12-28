import requests
from datetime import datetime 

USERNAME = "trial84"
TOKEN = "afhdsdsfsgse34s4dfsd"
GRAPH_ID = "python-days"
HEADERS = {
    "X-USER-TOKEN": TOKEN,
}

# Method to create a user on the pixela
def create_user():
    params = {
        "token": TOKEN,
        "username" : USERNAME,
        "agreeTermsOfService" : "yes",
        "notMinor" : "yes"
    }

    create_user_endpoint = "https://pixe.la/v1/users"
    response = requests.post(url=create_user_endpoint, json=params)
    print(response.text)

#create graph on pixela
def create_graph():
    create_graph_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs"
    params = {
        "id": GRAPH_ID,
        "name" : "Coding Days",
        "unit" : "Lessons",
        "type": "int",
        "color":"ajisai",
    }
    response = requests.post(url=create_graph_endpoint, HEADERS=HEADERS, json=params)
    print(response.text)

def post_pixel():
    today = datetime.now()
    
    post_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}"
    params = {
        "date":today.strftime("%Y%m%d"),
        "quantity":input("How many python Lessons did you complete today?"),
    }
    response = requests.post(url=post_pixel_endpoint, json=params, headers=HEADERS)
    print(response.text)


#create_user()
#create_graph()
post_pixel()