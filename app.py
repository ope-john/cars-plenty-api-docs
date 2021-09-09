import streamlit as st

st.title('Cars Plenty Api documentation')

navi = st.sidebar.selectbox(
    "Navigation",
    ['Home', 'Documentation'])
st.write(navi)

if navi == 'Home':
    st.write('Cars plenty is a car marketplace and auctioning platform')
    st.write('Disclamer: The webpages contained in this website are strictly confidential and solely for the use of development process of the Carplenty app and may not be reproduced or circulated without approval for Carsplenty prior written consent. If you are not the intented recipient, you may not disclose or use the information in this documentation in any way.')

if navi == 'Documentation':
    sub_nav = st.sidebar.selectbox(
    "Docs",
    ['App', 'Auction', 'Wallet'])
    if sub_nav == 'App':
        endpoints = st.sidebar.selectbox(
        "Endpoints",
        [
            'Vehicles', 
            'Vehicle', 
            'Sign up',
            'Login',
            'Search',
            'Update Password',
            'Confirm Email',
            'Resend Confirmation',
            'Post Vehicle',
            'Post Verified Vehicle'])
        if endpoints == 'Vehicles':
            st.header('Gets all vehicles in the database')
            st.subheader('GET: https://carsplenty.com/api/v1/vehicles')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""
            {
                "page_number": 1 #int
            }
            """)
            st.write('Response')
            st.code(""" 
            {
                "data": [{
                    "_id": "6136be2d3719c24549a6c0ce", #str
                    "brand": "Ford", #str
                    "colour": "Brown", #str
                    "condition": "Foriegn Used", #str
                    "fuel": "Petrol", #str
                    "location": "Lagos State, Ikeja", #str
                    "main_image": "main_image", #str
                    "model": "Edge", #str
                    "posted": "Tue, 07 Sep 2021 02:19:35 GMT", #str
                    "posted_by": "6133a854917812bea8c5a51c", #str
                    "price": "3,000,000", #str
                    "seat": "5", #str
                    "transmission": "Automatic", #str
                    "verified": true, #bool
                    "views": 0, #int
                    "year": "2009" #strr
                },...]
            }""")
        if endpoints == 'Vehicle':
            st.header('Gets vehicle details for selected vehicle')
            st.subheader('GET: https://carsplenty.com/api/v1/vehicle')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "vehicle_id": "6136c1543719c24549a6c0cf" #str
            }""")
            st.write('Response')
            st.code("""{
                "data": {
                    "dealer_info": {
                        "account_created": "4 days ago", #str
                        "email": "janedoe@email.com", #str
                        "name": "Jane Doe", #str
                        "number_of_ads": 1, #int
                        "phone_number": "08030001000", #str
                        "profile_picture": null, #None
                        "listings": [], #array
                        "dealer_id": "61266ddef4bf66e9ccdbe938" #str
                    },
                    "vehicle": {
                        "_id": "6136c1543719c24549a6c0cf" #str,
                        "brand": "Toyota", #str
                        "colour": "White", #str
                        "condition": "Foriegn Used", #str
                        "fuel": "Petrol", #str
                        "images": ["image_1", "image_2", "image_3", "image_4", "image_5", "image_6", "image_7"], #array
                        "location": "Lagos State, Abule Egba", #str
                        "main_image": "main_image", #str
                        "mileage": "43000 km", #str
                        "model": "Venza", #str
                        "negotiable": false, #bool
                        "posted": "1 day ago", #str
                        "posted_by": "61266ddef4bf66e9ccdbe938", #str
                        "price": "6,000,000", #str
                        "registered": false, #bool
                        "seat": "5", #str
                        "transmission": "Automatic", #str
                        "verified": true, #bool
                        "views": 1, #int
                        "year": "2012" #str
                    }
                }
            }""")
        if endpoints == 'Sign up':
            st.header('Signs up to carsplenty')
            st.subheader('POST: https://carsplenty.com/api/v1/signup')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "name": "Theordore Doe", #str
                "email": "theordoe@email.com", #str
                "phone_number": "07030009000", #str
                "password": "password" #str
            }""")
            st.write('Response')
            st.code("""{
                "data": {
                    "confirm_email": "InRoZW9yZG9lQGVtYWlsLmNvbSI.YTj7FA.UTkqFlaeA_m234CNm0UWW-AUTOk", #str
                    "message": "Success" #str
                }
            }""")

            pass
        if endpoints == 'Login':
            st.header('Login to carsplenty')
            st.subheader('GET: https://carsplenty.com/api/v1/login')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "email": "johndoe@email.com", #str
                "password": "password" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                "data": {
                    "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMTEyNDk5OCwianRpIjoiZmY1MDBiMjgtMTZlOS00OTM1LTliMjYtMmEwOGE0MzhlMWEwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI2MTMzYTg1NDkxNzgxMmJlYThjNWE1MWMiLCJuYmYiOjE2MzExMjQ5OTgsImV4cCI6MTYzMzcxNjk5OH0.CRsHKed1MKf5H-9OrP6eeCTzb2bh4rrQTfIGcFPuDJc", #str
                    "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMTEyNDk5OCwianRpIjoiYjY2NDFjNmYtZWUyMy00ZjlhLThhZmMtMDRjNGVhZjIxYzk1IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjYxMzNhODU0OTE3ODEyYmVhOGM1YTUxYyIsIm5iZiI6MTYzMTEyNDk5OCwiZXhwIjoxNjMzNzE2OTk4fQ.nQYpE91ChJ5ImF3v01aYs7uQNq2LGFqieAu3yP5xRQ4", #str
                    "user_data": {
                        "account_created": "4 days ago", #str
                        "email": "johndoe@email.com", #str
                        "followers": 0, #int
                        "name": "John Doe", #str
                        "phone_number": "08030001000", #str
                        "profile_picture": null, #none
                        "user_id": "6133a854917812bea8c5a51c" #str
                        }
                    }
                }
            }""")
            st.write('Response - 403')
            st.code("""{
                "access token": "Token not generated", #str
                "message": "Authentication Failed" #str
            }""")
            pass
        if endpoints == 'Search':
            st.header('Search for vehicles by brand, model, year, transmission type, colour')
            st.subheader('GET: https://carsplenty.com/api/v1/search')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "search": "toyota" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                "data": [
                    {
                        "_id": "6136c1543719c24549a6c0cf", #str
                        "brand": "Toyota", #str
                        "colour": "White", #str
                        "condition": "Foriegn Used", #str
                        "fuel": "Petrol", #str
                        "location": "Lagos State, Abule Egba", #str
                        "main_image": "image", #str
                        "model": "Venza", #str
                        "posted": "Tue, 07 Sep 2021 02:19:35 GMT", #str
                        "posted_by": "61266ddef4bf66e9ccdbe938", #str
                        "price": "6,000,000", #str
                        "seat": "5", #str
                        "transmission": "Automatic", #str
                        "verified": true, #bool
                        "views": 2, #int
                        "year": "2012" #str
                    },...]
            }""")
            st.write('Response - 404')
            st.code("""{
                "data": {
                    "message": "Query not found" #str
                }
            }""")
            pass
        if endpoints == 'Update Password':
            st.header('Change user password')
            st.subheader('PATCH: https://carsplenty.com/api/v1/update-password')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "email": "janedoe@email.com", #str
                "new_password": "password" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                "message": "Success" #str
            }""")
            pass
        if endpoints == 'Confirm Email':
            st.header('Verifies user email')
            st.subheader('GET: https://carsplenty.com/api/v1/confirm-email/{email-token}')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
            }""")
            st.write('Response - 200')
            st.code("""{
                "message": "Email confirmed" #str
            }""")
            st.write('Response - 403')
            st.code("""{
                "message": "Email confirmation link expired" #expires after an hour
            }""")
            pass
        if endpoints == 'Resend Confirmation':
            st.header('Resends email confirmation link')
            st.subheader('GET: https://carsplenty.com/api/v1/resend-link')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "email": "theordoe@email.com" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                "data":{
                "token": "InRoZW9yZG9lQGVtYWlsLmNvbSI.YTj7FA.UTkqFlaeA_m234CNm0UWW-AUTOk"
                }
            }""")
            pass
        if endpoints == 'Post Vehicle':
            st.header('Post vehicle for verification')
            st.subheader('POST: https://carsplenty.com/api/v1/post')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                    "brand": "Honda", #str
                    "model": "Civic", #str
                    "year": "2012", #str
                    "colour": "Black", #str
                    "condition": "Nigerian Used", #str
                    "transmission": "Automatic", #str
                    "mileage": "107000 km", #str
                    "registered": true, #bool
                    "location": "Lagos State, Ajah", #str
                    "price": "3,000,000", #str
                    "VIN": "DU4M4MYV7I3N", #str
                    "posted_by": "6133a854917812bea8c5a51c", #str
                    "negotiable": true, #bool
                    "fuel": "Petrol", #str
                    "seats": "5", #str
                    "verified": false, #bool
                    "images": ["image_1", "image_2", "image_3", "image_4", "image_5", "image_6", "image_7"], #array
                    "main_image": "main_image", #str
            }""")
            st.write('Response - 200')
            st.code("""{
                'message': 'Reviewing' #str
            }""")
            pass
        if endpoints == 'Post Verified Vehicle':
            st.header('Post verified vehicle')
            st.subheader('POST: https://carsplenty.com/api/v1/post-verified')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                    "brand": "Honda", #str
                    "model": "Civic", #str
                    "year": "2012", #str
                    "colour": "Black", #str
                    "condition": "Nigerian Used", #str
                    "transmission": "Automatic", #str
                    "mileage": "107000 km", #str
                    "registered": true, #bool
                    "location": "Lagos State, Ajah", #str
                    "price": "3,000,000", #str
                    "VIN": "DU4M4MYV7I3N", #str
                    "posted_by": "6133a854917812bea8c5a51c", #str
                    "negotiable": true, #bool
                    "fuel": "Petrol", #str
                    "seats": "5", #str
                    "verified": true, #bool
                    "images": ["image_1", "image_2", "image_3", "image_4", "image_5", "image_6", "image_7"], #array
                    "main_image": "main_image", #str
            }""")
            st.write('Response - 200')
            st.code("""{
                'message': 'Success' #str
            }""")
            st.write('Response - 400')
            st.code("""{
                'message': 'Failed' #str
            }""")
            pass