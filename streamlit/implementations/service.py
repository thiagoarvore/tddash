import streamlit as st

from . import repository


class ImplementationService:

    def __init__(self):
        self.implementation_repository = repository.ImplementationRepository()

    def get_implementations(self):
        if "implementations" in st.session_state:
            return st.session_state.implementations
        implementations = self.implementation_repository.get_implementations()
        st.session_state.implementations = implementations
        return implementations

    def create_implementation(
        self,
        account_manager,
        product,
        serial_number,
        supplier,
        mac,
        client,
        address,
        cnpj,
        unit,
        building_area,
        solution,
        license,
        license_expiration_date,
        status,
        management,
        billing_date,
        unifi_url_controller=None,
        unifi_access=None,
        unifi_password=None,
        unifi_site_unity=None,
        unifi_management_ip=None,
        unifi_observations=None,
    ):
        implementation = dict(
            account_manager=account_manager,
            product=product,
            serial_number=serial_number,
            mac=mac,
            client=client,
            address=address,
            cnpj=cnpj,
            supplier=supplier,
            unit=unit,
            building_area=building_area,
            unifi_access=unifi_access,
            unifi_management_ip=unifi_management_ip,
            unifi_observations=unifi_observations,
            unifi_password=unifi_password,
            unifi_site_unity=unifi_site_unity,
            unifi_url_controller=unifi_url_controller,
            billing_date=billing_date,
            management=management,
            status=status,
            license=license,
            license_expiration_date=license_expiration_date,
            solution=solution,
        )
        new_implementation = self.implementation_repository.create_implementation(
            implementation
        )
        st.session_state.implementations.append(new_implementation)
        return new_implementation
