import requests


class ImplementationRepository:

    def __init__(self):
        self.__base_url = "http://localhost:8000/api/v1/"
        self.__brands_url = f"{self.__base_url}implementations/"
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_implementations(self):
        response = requests.get(
            self.__brands_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(
            f"Erro ao obter dados da API. Status code: {response.status_code} {response.text}"
        )

    def create_implementation(self, implementation):
        response = requests.post(
            self.__brands_url,
            # headers=self.__headers,
            data=implementation,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(
            f"Erro ao cadastrar dados na API. Status code: {response.status_code} {response.text}"
        )
