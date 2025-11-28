import requests
import pytest
Import pytest_check as check
from faker import Faker
from datetime import datetime


fake = Faker()

class TestGetUser:

    @pytest.mark.get
    def test_get_response_code(self, api_url):
        respose = requests.get(api_url + "users")
        
        assert respose.status_code == 200

    @pytest.mark.get
    def test_get_response_data(self, api_url):
        response = requests.get(api_url + "users")
        data = response.json() #lista

        assert len(data) > 0
        assert isinstance(data,list)

        first_user = data[0]
        print(first_user)
        key_structure = ["id","name","username","phone","address","website"]

        for i in key_structure:
            assert i in first_user , f"campo{1} , no esta en {first_user}"



class TestPostUser:
    @pytest.mark.post
    def test_post_response_code(self,api_url):

        new_user = {
            "name":fake.name(),
            "email":fake.email(),
            "phone":fake.phone_number(),
            #"createdAt": "2022-05-05"
        }


        response = requests.post(api_url + "users", new_user)
        assert response.status_code == 201

        data = response.json()
        print(data)     #para ver los print al final del comando se coloca -s
        assert "id" in data

        #user_created = data[0]

        if "createdAt" in data:
            created_at = data["createdAt"]
            current_year = datetime.now().year
            assert str(current_year) in created_at , f"no esta en el año"

        


class TestUserWorkFlow:

    def test_completo_user(self, api_url):
        #GET: Obtener  los usuarios
