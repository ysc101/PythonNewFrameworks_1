import requests
def api_test():
    url="http://192.168.0.162:8082/api/LoginApi/GetUserDetails"
    params={
        "UserName":"AUDITWORK4",
        "PassWord":"Pass@123"
    }
    response=requests.get(url, params=params)
    if response.status_code==200:
       try:
        data=response.json()
        print("Response Data: ",data)
       except requests.exceptions.JSONDecodeError:
        print("Response not in json")
    else:
       print("Response Status Code: ",response.status_code)
       print(response.text)
api_test()