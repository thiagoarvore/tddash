import pandas as pd
from accounts.service import AccountsService
from st_aggrid import AgGrid, ExcelExportMode
from storage.service import ProductService, SupplierService

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
                "supplier.id",
                "account_manager.id",
                "account_manager.password",
                "account_manager.last_login",
                "account_manager.is_superuser",
                "account_manager.username",
                "account_manager.is_staff",
                "account_manager.is_active",
                "account_manager.date_joined",
                "account_manager.groups",
                "account_manager.user_permissions",
                "account_manager.first_name",
                "account_manager.last_name",
                "account_manager.created_at",
                "account_manager.updated_at",
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
    account_service = AccountsService()
    accounts = account_service.get_accounts()
    account_list = {
        f"{account['first_name']} {account['last_name']}": account["id"]
        for account in accounts
    }

    supplier_service = SupplierService()
    suppliers = supplier_service.get_suppliers()
    supplier_list = {supplier["name"]: supplier["id"] for supplier in suppliers}
    selected_supplier = st.selectbox("Fornecedor", list(supplier_list.keys()))

    product_service = ProductService()
    products = product_service.get_products()
    product_list = {product["name"]: product["id"] for product in products}

    if selected_supplier:
        selected_account = st.selectbox("Account manager", list(account_list.keys()))
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

        management = st.selectbox(options=["Cliente", "Think Digital"], label="Gestão")

        billing_date = st.date_input("Data de Corte")

        if selected_supplier.lower() == "unifi":

            unifi_access = st.text_input("Acesso Unifi (apenas para Unifi)")
            unifi_password = st.text_input(
                "Senha Unifi (apenas para Unifi)", type="password"
            )
            unifi_url_controller = st.text_input(
                "Unifi URL Controller (apenas para Unifi)"
            )
            unifi_management_ip = st.text_input(
                "Unifi Management IP (apenas para Unifi)"
            )
            unifi_observations = st.text_area("Observações Unifi (apenas para Unifi)")
            unifi_site_unity = st.text_input("Unifi site unity (apenas para Unifi)")

    if st.button("Cadastrar"):
        if not serial_number:
            st.error("O número de série é obrigatório!")
            return
        if not mac:
            st.error("O MAC é obrigatório!")
            return
        if not selected_supplier:
            st.error("O fornecedor é obrigatório!")
            return
        if not selected_product_name:
            st.error("O produto é obrigatório!")
            return
        if not client:
            st.error("O cliente é obrigatório!")
            return
        if not cnpj:
            st.error("O CNPJ é obrigatório!")
            return
        if not address:
            st.error("O endereço é obrigatório!")
            return
        if not building_area:
            st.error("A área na qual o equipamento está implantado é obrigatório!")
            return
        if not license:
            st.error("A licença é obrigatório!")
            return
        if not license_expiration_date:
            st.error("a data de validade da licença é obrigatório!")
            return
        if not selected_account:
            st.error("O responsável pela conta é obrigatório!")
            return

        if selected_product_name.lower() == "unifi":
            new_implementation = implementation_service.create_implementation(
                account_manager=account_list[selected_account],
                product=product_list[selected_product_name],
                serial_number=serial_number,
                supplier=selected_supplier,
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
        else:
            new_implementation = implementation_service.create_implementation(
                account_manager=account_list[selected_account],
                product=product_list[selected_product_name],
                serial_number=serial_number,
                mac=mac,
                client=client,
                supplier=supplier_list[selected_supplier],
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
            )
        if new_implementation:
            st.success("Implementação cadastrada!")
            return
        else:
            st.error("Erro ao cadastrar a implementação. Verifique os campos")
