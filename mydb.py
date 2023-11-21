# import mysql.connector as mc
# mydb=mc.connect(host="localhost",user="root",passwd="Akhilesh@2003",database="db1")
# mycursor=mydb.cursor()
# mycursor.execute("select * from sample")
# for i in mycursor:
#     print(i)
# mydb.close()


# import mysql.connector
# from mysql.connector import errorcode

# try:
#   mydb = mysql.connector.connect(host="localhost",user="root",passwd="Akhilesh@2003",database="db1")
#   mycursor=mydb.cursor()
#   mycursor.execute("select * from sample")
#   for i in mycursor:
#      print(i)
# except mysql.connector.Error as err:
#   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#     print("Something is wrong with your user name or password")
#   elif err.errno == errorcode.ER_BAD_DB_ERROR:
#     print("Database does not exist")
#   else:
#     print(err)
# else:
#   mydb.close()
from flask import Flask, render_template, request,redirect
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="student",
  password="123",
  database="laundry"
)

username = 123
password = 123
mycursor = mydb.cursor()
mycursor.execute(f"SELECT * FROM login_cred WHERE username = '{username}' and password = '{password}'")
student_details = mycursor.fetchone()
print(student_details)


# import streamlit as st

# def login():
#     st.subheader('Login')

#     username = st.text_input('Username')
#     password = st.text_input('Password', type='password')

#     if st.button('Login'):
#         # Add your authentication logic here
#         if username == 'username' and password == 'password':
#             st.success('Logged in as {}'.format(username))
#         else:
#             st.error('Incorrect username or password')

# def signup():
#     st.subheader('Signup')

#     new_username = st.text_input('New Username')
#     new_password = st.text_input('New Password', type='password')

#     if st.button('Signup'):
#         # Add your signup logic here
#         st.success('Your account has been created!')

# def main():
#     st.title('Login/Signup Form')

#     tabs = st.radio('Navigation', ['Login', 'Signup'])

#     if tabs == 'Login':
#         login()
#     elif tabs == 'Signup':
#         signup()

# if __name__ == '__main__':
#     main()
