from datetime import datetime
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid, ExcelExportMode
from . import service


def get_sector(action):
    actions_map = {
        'brands': show_brands,
        'categories': show_categories,
        # 'suppliers': show_suppliers,
        # 'products': show_products,
        # 'entries': show_entries,
        # 'exits': show_exits,
    }
    return actions_map.get(action)

def show_storage():
    
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    action = None

    with col1:
        if st.button('Marcas'):
            action = 'brands'
    with col2:
        if st.button('Categorias'):
            action = 'categories'
    with col3:
        if st.button('Fornecedores'):
            action = 'suppliers'
    with col4:
        if st.button('Produtos'):
            action = 'products'
    with col5:
        if st.button('Entradas'):
            action = 'inflows'
    with col6:
        if st.button('Saídas'):
            action = 'outflows'
    
    st.divider()

    sector_function = get_sector(action)
    if sector_function:
        sector_function()


def show_brands():
    brand_service = service.BrandService()
    brands = brand_service.get_brands()

    if brands:
        st.write('Marcas de produtos:')

        brands_df = pd.json_normalize(brands)

        AgGrid(
            data=brands_df,
            key='brands_grid',
        )

    else:
        st.warning('Nenhuma marca encontrado.')
    
    st.title('Cadastrar nova Marca')

    name = st.text_input('Nome da marca')

    if st.button('Cadastrar'):
        new_brand = brand_service.create_brand(
            name=name,
        )
        if new_brand:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a marca. Verifique os campos')

def show_categories():
    categories_service = service.CategoryService()
    categories = categories_service.get_categories()

    if categories:
        st.write('Marcas de produtos:')

        categories_df = pd.json_normalize(categories)

        AgGrid(
            data=categories_df,
            key='categories_grid',
        )

    else:
        st.warning('Nenhuma categoria encontrado.')
    
    st.title('Cadastrar nova Categoria')

    name = st.text_input('Nome da categoria')

    if st.button('Cadastrar'):
        new_category = categories_service.create_category(
            name=name,
        )
        if new_category:
            st.rerun()
        else:
            st.error('Erro ao cadastrar a categoria. Verifique os campos')