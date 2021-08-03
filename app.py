import streamlit as st
import sqlite3
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import datetime
time = datetime.datetime.now()
import pywhatkit as py
import emailscrape
import base64



def main():
    st.title("Marketing Automation Tool")
    menu = ["Lead Extraction","Whatsapp Automation"]
    choice = st.sidebar.selectbox("Menu",menu)
    if choice == "Lead Extraction":
        query = st.text_input('Enter your query to want to scrape emails from')
        num = st.slider('Enter number of websites you want scrape emails from')
        bad_words = ['facebook', 'instagram', 'youtube', 'twitter', 'wiki']
        button = st.button('Get me emails')
        if button:
            df = emailscrape.get_info(query, num, 'en', 'data.csv', reject=bad_words)
            st.write(df)
            def get_table_download_link_csv(df):
                csv = df.to_csv().encode()
                b64 = base64.b64encode(csv).decode()
                href = f'<a href="data:file/csv;base64,{b64}" download="captura.csv" target="_blank">Download csv file</a>'
                return href
            st.markdown(get_table_download_link_csv(df), unsafe_allow_html=True)
    
    if choice == "Whatsapp Automation":
        st.title("Automating your Whatsapp Message")
        phonelist = st.text_input("Please input numbers you want to automate with seperated by ,")
        message = st.text_area("Enter your Message")
        submit = st.button("Enter")
        i=1
        if submit:
            phone = phonelist.split(',')
            for each in phone:
                py.sendwhatmsg("+968"+each,message,time.hour,(time.minute+i))
                i=i+1
            st.success("Message Send!")








if __name__ == '__main__':
    main()
