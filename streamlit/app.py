from implementations.page import show_implementations
from storage.page import (show_brands, show_categories, show_inflows,
                          show_outflows, show_products, show_suppliers)

import streamlit as st


def main():
    if "menu_option2" not in st.session_state:
        st.session_state["menu_option2"] = None

    st.title("Think Digital")

    menu_option = st.sidebar.selectbox(
        "Selecione uma opção", ["Início", "Estoque", "Equipamentos implementados"]
    )

    if menu_option == "Início":
        st.session_state["menu_option2"] = None
        st.write("Bem-vindo ao sistema!")

    if menu_option == "Equipamentos implementados":
        st.session_state["menu_option2"] = None
        show_implementations()

    if menu_option == "Estoque":
        menu_option2 = st.sidebar.selectbox(
            "Selecione uma opção",
            ["Marcas", "Categorias", "Suppliers", "Produtos", "Entradas", "Saídas"],
        )
        st.session_state["menu_option2"] = menu_option2

        if menu_option2 == "Marcas":
            show_brands()
        if menu_option2 == "Categorias":
            show_categories()
        if menu_option2 == "Suppliers":
            show_suppliers()
        if menu_option2 == "Produtos":
            show_products()
        if menu_option2 == "Entradas":
            show_inflows()
        if menu_option2 == "Saídas":
            show_outflows()


if __name__ == "__main__":
    main()
