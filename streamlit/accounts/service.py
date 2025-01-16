from accounts.repository import AccountsRepository

import streamlit as st


class AccountsService:

    def __init__(self):
        self.accounts_repository = AccountsRepository()

    def get_accounts(self):
        if "accounts" in st.session_state:
            return st.session_state.accounts
        accounts = self.accounts_repository.get_users()
        st.session_state.accounts = accounts
        return accounts
