import requests

PIXELA_ENDPOINT="https://pixe.la/v1/users"
username="mralone"
api_token="anuragstoken"


user_params={
    "token":"anuragstoken",
    "username":"mralone",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

# response=requests.post(url=PIXELA_ENDPOINT,json=user_params)
# print(response.text)

graph_endpoint=f"{PIXELA_ENDPOINT}/{username}/graphs"

ID="graphone1"

grapsh_params={
    "id":ID,
    "name":"coding",
    "unit":"hours",
    "type":"float",
    "color":"ajisai"

}

headers={
    "X-USER-TOKEN":api_token
}

today="20220909"

graph_post_endpoint=f"https://pixe.la/v1/users/{username}/graphs/{ID}/{today}"
post_params={
    # "date":today,
    "quantity":"1",

}
response=requests.delete(url=graph_post_endpoint,json=post_params,headers=headers)
print(response.text)