import streamlit as st

st.set_page_config(page_title='Chat with IRS Pub17 2023', page_icon=':books:')

def main():
    
    st.header('Chat with IRS Pub17 2023 :books:')
    st.text_input('Ask a tax question:')

with st.sidebar:
    st.subheader('pdf')
    st.file_uploader('upload here and click on process')
    st.button('process')

if __name__ == '__main__':
    main()