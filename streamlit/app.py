import streamlit as st
from storage.page import show_storage

def main():
    st.title('Think Digital')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Inventário']
    )

    if menu_option == 'Início':
        pass

    if menu_option == 'Inventário':
        show_storage()

if __name__ == '__main__':
    main()
