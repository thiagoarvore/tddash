import requests
import streamlit as st

class BrandRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__brands_url = f'{self.__base_url}brands/'
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_brands(self):
        response = requests.get(
            self.__brands_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_brand(self, brand):
        response = requests.post(
            self.__brands_url,
            # headers=self.__headers,
            data=brand,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')
    

class CategoryRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__categories_url = f'{self.__base_url}categories/'
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_categories(self):
        response = requests.get(
            self.__categories_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_category(self, category):
        response = requests.post(
            self.__categories_url,
            # headers=self.__headers,
            data=category,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')
    

class SupplierRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__suppliers_url = f'{self.__base_url}suppliers/'
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_suppliers(self):
        response = requests.get(
            self.__suppliers_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_supplier(self, supplier):
        response = requests.post(
            self.__suppliers_url,
            # headers=self.__headers,
            data=supplier,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')


class ProductRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__products_url = f'{self.__base_url}products/'
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_products(self):
        response = requests.get(
            self.__products_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_product(self, product):
        response = requests.post(
            self.__products_url,
            # headers=self.__headers,
            data=product,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')


class InflowRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__inflows_url = f'{self.__base_url}inflows/'
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_inflows(self):
        response = requests.get(
            self.__inflows_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_inflow(self, inflow):
        response = requests.post(
            self.__inflows_url,
            # headers=self.__headers,
            data=inflow,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')


class OutflowRepository:

    def __init__(self):
        self.__base_url = 'http://localhost:8000/api/v1/'
        self.__outflows_url = f'{self.__base_url}outflows/'
        # self.__headers = {
        #     'Authorization': f'Bearer {st.session_state.token}'
        # }

    def get_products(self):
        response = requests.get(
            self.__outflows_url,
            # headers=self.__headers
        )
        if response.status_code == 200:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao obter dados da API. Status code: {response.status_code}')
    
    def create_outflow(self, outflow):
        response = requests.post(
            self.__outflows_url,
            # headers=self.__headers,
            data=outflow,
        )
        if response.status_code == 201:
            return response.json()
        # if response.status_code == 401:
        #     logout()
        #     return None
        raise Exception(f'Erro ao cadastrar dados na API. Status code: {response.status_code}')
