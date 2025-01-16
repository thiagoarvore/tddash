import pandas as pd
from st_aggrid import AgGrid, ExcelExportMode
from storage.service import ProductService

import streamlit as st

from . import service


def show_implementations():
    implementation_service = service.ImplementationService()
    implementations = implementation_service.get_implementations()

    if implementations:
        st.write("Equipamentos implementados:")

        implementations_df = pd.json_normalize(implementations)
        implementations_df = implementations_df.drop(
            columns=[
                "product.brand.id",
                "product.category.id",
                "id",
                "product.id",
                "product.quantity",
            ],
            errors="ignore",
        )

        product_search_term = st.text_input("Buscar por produto", "").lower()
        client_search_term = st.text_input("Buscar por cliente", "").lower()
        serial_search_term = st.text_input("Buscar por número de série", "").lower()
        mac_search_term = st.text_input("Buscar por MAC", "").lower()
        solution_search_term = st.text_input("Buscar por solução", "").lower()

        filtered_df = implementations_df  # Começa com o DataFrame completo

        if product_search_term:
            filtered_df = filtered_df[
                filtered_df["product.name"].str.contains(
                    product_search_term, case=False, na=False
                )
            ]
        if client_search_term:
            filtered_df = filtered_df[
                filtered_df["client"].str.contains(
                    client_search_term, case=False, na=False
                )
            ]
        if serial_search_term:
            filtered_df = filtered_df[
                filtered_df["serial_number"].str.contains(
                    serial_search_term, case=False, na=False
                )
            ]
        if mac_search_term:
            filtered_df = filtered_df[
                filtered_df["mac"].str.contains(mac_search_term, case=False, na=False)
            ]
        if solution_search_term:
            filtered_df = filtered_df[
                filtered_df["solution"].str.contains(
                    solution_search_term, case=False, na=False
                )
            ]

        AgGrid(
            data=filtered_df,
            key="implementations_grid",
            enableSorting=True,
            enableFilter=True,
            columns_auto_size_mode=True,
            excel_export_mode=ExcelExportMode.MANUAL,
            pagination=True,
            paginationPageSize=20,
        )

    else:
        st.write("Nenhum produto implementado encontrado.")

    st.title("Cadastrar implementação")
    if "validated_client" not in st.session_state:
        st.session_state.validated_client = False

    product_service = ProductService()
    products = product_service.get_products()
    product_list = {product["name"]: product["id"] for product in products}
    selected_product_name = st.selectbox("Produto", list(product_list.keys()))

    serial_number = st.text_input("Número de série")
    mac = st.text_input("MAC")

    client = st.text_input("Nome do cliente")
    cnpj = st.text_input("CNPJ")
    unit = st.text_input("Unidade")
    address = st.text_input("Endereço da implementação")
    building_area = st.text_input("Área que o equipamento está implementado")

    status = st.selectbox(
        options=[
            "Não iniciado",
            "Implementação",
            "Validação cliente",
            "Concluída",
            "Bloqueada",
        ],
        label="Status",
    )
    solution = st.selectbox(
        options=[
            "Zoox Wi-fi",
            "Propz",
        ],
        label="Solução",
    )
    license = st.text_input("Licença")
    license_expiration_date = st.date_input("Data de validade da licença")

    management = st.selectbox(options=["Cliente", "Think digital"], label="Gestão")

    billing_date = st.date_input("Data de Corte")

    unifi_access = st.text_input("Acesso Unifi (apenas para Unifi)")
    unifi_password = st.text_input("Senha Unifi (apenas para Unifi)", type="password")
    unifi_url_controller = st.text_input("Unifi URL Controller (apenas para Unifi)")
    unifi_management_ip = st.text_input("Unifi Management IP (apenas para Unifi)")
    unifi_observations = st.text_area("Observações Unifi (apenas para Unifi)")
    unifi_site_unity = st.text_input("Unifi site unity (apenas para Unifi)")

    if st.button("Cadastrar"):
        new_implementation = implementation_service.create_implementation(
            product=product_list[selected_product_name],
            serial_number=serial_number,
            mac=mac,
            client=client,
            address=address,
            building_area=building_area,
            billing_date=billing_date,
            unit=unit,
            cnpj=cnpj,
            solution=solution,
            management=management,
            license=license,
            license_expiration_date=license_expiration_date,
            status=status,
            unifi_access=unifi_access,
            unifi_password=unifi_password,
            unifi_url_controller=unifi_url_controller,
            unifi_observations=unifi_observations,
            unifi_management_ip=unifi_management_ip,
            unifi_site_unity=unifi_site_unity,
        )
        if new_implementation:
            st.rerun()
        else:
            st.error("Erro ao cadastrar a implementação. Verifique os campos")
