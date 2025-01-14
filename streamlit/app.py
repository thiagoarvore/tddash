import streamlit as st

def main():
    st.title('Think Digital')

    menu_option = st.sidebar.selectbox(
        'Selecione uma opção',
        ['Início', 'Inventário']
    )

    if menu_option == 'Início':
        pass

    if menu_option == 'Inventário':
        pass

if __name__ == '__main__':
    main()
