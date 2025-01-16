import pandas as pd
from st_aggrid import AgGrid, ExcelExportMode

import streamlit as st

from . import service


def show_brands():
    brand_service = service.BrandService()
    brands = brand_service.get_brands()

    if brands:
        st.write("Marcas de produtos:")

        brands_df = pd.json_normalize(brands)

        AgGrid(
            data=brands_df,
            key="brands_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
        )

    else:
        st.warning("Nenhuma marca encontrado.")

    st.title("Cadastrar nova Marca")

    name = st.text_input("Nome da marca")

    if st.button("Cadastrar", key="create_brand"):
        new_brand = brand_service.create_brand(
            name=name,
        )
        if new_brand:
            st.rerun()
        else:
            st.error("Erro ao cadastrar a marca. Verifique os campos")


def show_categories():
    categories_service = service.CategoryService()
    categories = categories_service.get_categories()

    if categories:
        st.write("Marcas de produtos:")

        categories_df = pd.json_normalize(categories)

        AgGrid(
            data=categories_df,
            key="categories_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
        )

    else:
        st.warning("Nenhuma categoria encontrado.")

    st.title("Cadastrar nova Categoria")

    name = st.text_input("Nome da categoria")

    if st.button("Cadastrar"):
        new_category = categories_service.create_category(
            name=name,
        )
        if new_category:
            st.success("Categoria cadastrada")
            st.rerun()
        else:
            st.error("Erro ao cadastrar a categoria. Verifique os campos")


def show_suppliers():
    suppliers_service = service.SupplierService()
    suppliers = suppliers_service.get_suppliers()

    if suppliers:
        st.write("Fornecedores:")

        suppliers_df = pd.json_normalize(suppliers)

        AgGrid(
            data=suppliers_df,
            key="suppliers_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
        )

    else:
        st.warning("Nenhum fornecedor encontrado.")

    st.title("Cadastrar novo fornecedor")

    name = st.text_input("Nome do fornecedor")

    if st.button("Cadastrar"):
        new_supplier = suppliers_service.create_supplier(
            name=name,
        )
        if new_supplier:
            st.success("Fornecedor cadastrado")
            st.rerun()
        else:
            st.error("Erro ao cadastrar fornecedor. Verifique os campos")


def show_products():
    products_service = service.ProductService()
    products = products_service.get_products()

    if products:
        st.write("Produtos:")

        products_df = pd.json_normalize(products)
        products_df = products_df.drop(
            columns=["brand.id", "category.id"], errors="ignore"
        )
        product_search_term = st.text_input("Buscar por produto", "").lower()
        brand_search_term = st.text_input("Buscar por marca", "").lower()
        category_search_term = st.text_input("Buscar por categoria", "").lower()

        filtered_df = products_df

        if product_search_term:
            filtered_df = filtered_df[
                filtered_df["name"].str.contains(
                    product_search_term, case=False, na=False
                )
            ]
        if brand_search_term:
            filtered_df = filtered_df[
                filtered_df["brand.name"].str.contains(
                    brand_search_term, case=False, na=False
                )
            ]
        if category_search_term:
            filtered_df = filtered_df[
                filtered_df["category.name"].str.contains(
                    category_search_term, case=False, na=False
                )
            ]

        AgGrid(
            data=filtered_df,
            key="products_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
        )

    else:
        st.warning("Nenhum produto encontrado.")

    st.title("Cadastrar novo produto")

    name = st.text_input("Nome do produto")
    brand_service = service.BrandService()
    brands = brand_service.get_brands()
    brand_list = {brand["name"]: brand["id"] for brand in brands}
    selected_brand_name = st.selectbox("Marca", list(brand_list.keys()))

    category_service = service.CategoryService()
    categories = category_service.get_categories()
    category_list = {category["name"]: category["id"] for category in categories}
    selected_category_name = st.selectbox("Categoria", list(category_list.keys()))

    if st.button("Cadastrar"):
        new_product = products_service.create_product(
            name=name,
            brand=brand_list[selected_brand_name],
            category=category_list[selected_category_name],
        )
        if new_product:
            st.success("Produto cadastrado")
            st.rerun()
        else:
            st.error("Erro ao cadastrar produto. Verifique os campos")


def show_inflows():
    inflows_service = service.InflowService()
    inflows = inflows_service.get_inflows()

    if inflows:
        st.write("Entradas:")

        inflows_df = pd.json_normalize(inflows)
        inflows_df = inflows_df.drop(
            columns=[
                "product.brand.id",
                "product.category.id",
                "product.id",
                "supplier.id",
                "product.quantity",
                "product.serial_number",
                "product.mac",
            ],
            errors="ignore",
        )
        product_search_term = st.text_input("Buscar por produto", "").lower()
        brand_search_term = st.text_input("Buscar por marca", "").lower()
        category_search_term = st.text_input("Buscar por categoria", "").lower()
        supplier_search_term = st.text_input("Buscar por fornecedor", "").lower()

        filtered_df = inflows_df

        if product_search_term:
            filtered_df = filtered_df[
                filtered_df["name"].str.contains(
                    product_search_term, case=False, na=False
                )
            ]
        if brand_search_term:
            filtered_df = filtered_df[
                filtered_df["brand.name"].str.contains(
                    brand_search_term, case=False, na=False
                )
            ]
        if category_search_term:
            filtered_df = filtered_df[
                filtered_df["category.name"].str.contains(
                    category_search_term, case=False, na=False
                )
            ]
        if supplier_search_term:
            filtered_df = filtered_df[
                filtered_df["supplier.name"].str.contains(
                    supplier_search_term, case=False, na=False
                )
            ]

        AgGrid(
            data=filtered_df,
            key="inflows_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
        )

    else:
        st.warning("Nenhuma entrada encontrado.")

    st.title("Cadastrar nova entrada")

    product_service = service.ProductService()
    products = product_service.get_products()
    product_list = {product["name"]: product["id"] for product in products}
    selected_product_name = st.selectbox("Produto", list(product_list.keys()))

    supplier_service = service.SupplierService()
    suppliers = supplier_service.get_suppliers()
    supplier_list = {supplier["name"]: supplier["id"] for supplier in suppliers}
    selected_supplier_name = st.selectbox("Fornecedor", list(supplier_list.keys()))

    quantity = st.text_input("Quantidade")
    cost_price = st.text_input("Preço (use ponto ao invés de vírgula)")

    if st.button("Cadastrar"):
        new_inflow = inflows_service.create_inflow(
            product=product_list[selected_product_name],
            supplier=supplier_list[selected_supplier_name],
            quantity=quantity,
            cost_price=cost_price,
        )
        if new_inflow:
            st.success("Entrada cadastrada")
            st.rerun()
        else:
            st.error("Erro ao cadastrar entrada. Verifique os campos")


def show_outflows():
    outflows_service = service.OutflowService()
    outflows = outflows_service.get_outflows()

    if outflows:
        st.write("Saídas:")

        outflows_df = pd.json_normalize(outflows)
        outflows_df = outflows_df.drop(
            columns=[
                "product.brand.id",
                "product.category.id",
                "product.id",
                "supplier.id",
                "product.quantity",
                "product.serial_number",
                "product.mac",
            ],
            errors="ignore",
        )
        product_search_term = st.text_input("Buscar por produto", "").lower()
        brand_search_term = st.text_input("Buscar por marca", "").lower()
        category_search_term = st.text_input("Buscar por categoria", "").lower()
        implementation_search_term = st.checkbox("Apenas produtos implementados")

        filtered_df = outflows_df

        if product_search_term:
            filtered_df = filtered_df[
                filtered_df["name"].str.contains(
                    product_search_term, case=False, na=False
                )
            ]
        if brand_search_term:
            filtered_df = filtered_df[
                filtered_df["brand.name"].str.contains(
                    brand_search_term, case=False, na=False
                )
            ]
        if category_search_term:
            filtered_df = filtered_df[
                filtered_df["category.name"].str.contains(
                    category_search_term, case=False, na=False
                )
            ]
        if implementation_search_term:
            filtered_df = filtered_df[filtered_df["implemented"] == True]

        AgGrid(
            data=filtered_df,
            key="outflows_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            defaultCsvExportParams=True,
            pagination=True,
            paginationPageSize=20,
        )

    else:
        st.warning("Nenhuma saída encontrado.")

    st.title("Cadastrar nova saída")

    product_service = service.ProductService()
    products = product_service.get_products()
    product_list = {product["name"]: product["id"] for product in products}
    selected_product_name = st.selectbox("Produto", list(product_list.keys()))

    quantity = st.text_input("Quantidade")
    selling_price = st.text_input("Preço (use ponto ao invés de vírgula)")
    implemented = st.checkbox("Produto implementado?")

    if st.button("Cadastrar"):
        new_outflow = outflows_service.create_outflow(
            product=product_list[selected_product_name],
            implemented=implemented,
            quantity=quantity,
            selling_price=selling_price,
        )
        if new_outflow:
            st.success("Saída cadastrada")
            st.rerun()
        else:
            st.error("Erro ao cadastrar saída. Verifique os campos")
