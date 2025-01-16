import requests
from login.service import logout

import streamlit as st


class AccountsRepository:

    def __init__(self):
        self.__base_url = "http://localhost:8000/api/v1/"
        self.__accounts_url = f"{self.__base_url}accounts/"
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_users(self):
        response = requests.get(
            self.__accounts_url,
            # headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(
            f"Erro ao obter os perfis. Status code: {response.status_code} {response.text}"
        )
