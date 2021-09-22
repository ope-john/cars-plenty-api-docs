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
            'Auth Vehicle',
            'Sign up',
            'Login',
            'Search',
            'Filters',
            'Update Password',
            'Confirm Email',
            'Resend Confirmation',
            'Post Vehicle',
            'Follow User',
            'Unfollow User',
            'Save Vehicle',
            'Saved Vehicles',
            'Unsave Vehicle',
            'Trending deals',
            'Get messages',
            'Start message',
            'Send message',
            'Delete message'])
        if endpoints == 'Vehicles':
            st.header('Gets all vehicles in the database')
            st.subheader('GET: www.carsplenty.com/api/v1/vehicles?page_number=1')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Request Parameter')
            st.code("""
            {
                "page_number" = 1 #int
            }
            """)
            st.write('Response')
            st.code(""" 
            {
                [{
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
                }]
            }""")
        if endpoints == 'Vehicle':
            st.header('Gets vehicle details for selected vehicle')
            st.subheader('GET: www.carsplenty.com/api/v1/vehicle?id=6136c1543719c24549a6c0cf')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Request parameters')
            st.code("""{
                vehicle_id = 6136c1543719c24549a6c0cf #str
            }""")
            st.write('Response')
            st.code("""{
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
                }""")
        if endpoints == 'Sign up':
            st.header('Signs up to carsplenty')
            st.subheader('POST: www.carsplenty.com/api/v1/signup')
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
                    "confirm_email": "InRoZW9yZG9lQGVtYWlsLmNvbSI.YTj7FA.UTkqFlaeA_m234CNm0UWW-AUTOk", #str
                    "message": "Success" #str
                }""")

            pass
        if endpoints == 'Login':
            st.header('Login to carsplenty')
            st.subheader('POST: www.carsplenty.com/api/v1/login')
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
                "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI
                6ZmFsc2UsImlhdCI6MTYzMjIxNzM1MiwianRpIjoiMmMxMDg5ZjEtZjZmZS
                00MmIxLWFlNGEtYWJkY2MwZmE5OTdkIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6
                IjYxMjY2ZGRlZjRiZjY2ZTljY2RiZTkzOCIsIm5iZiI6MTYzMjIxNzM1MiwiZXhw
                IjoxNjM0ODA5MzUyfQ.j3OZwr7Q8qh7mJNlAvnxebbMD8eBtZNBfera0Z-vr9M" #str
            }""")
            st.write('Response - 403')
            st.code("""{
                    "Authentication Failed" #str
            }""")
            pass
        if endpoints == 'Search':
            st.header('Search for vehicles by brand, model, year, transmission type, colour')
            st.subheader('GET: www.carsplenty.com/api/v1/search?query=toyota')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                query = toyota #str
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
                    "Query not found" #str
                }""")
            pass
        if endpoints == 'Filters':
            st.header('Get all filters for posting and searching')
            st.subheader('GET: www.carsplenty.com/api/v1/filters')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                            {
                                "colour": [
                                    "Black",
                                    "Blue",
                                    "Grey",
                                    "Red",
                                    "Silver",
                                    "Beige",
                                    "Brown",
                                    "Burgandy",
                                    "Gold",
                                    "Green",
                                    "Ivory",
                                    "Matte Black",
                                    "Off White",
                                    "Orange",
                                    "Pearl",
                                    "Pink",
                                    "Purple",
                                    "Teal",
                                    "White",
                                    "Yellow",
                                    "Wine"
                                ],
                                "condition": [
                                    "Brand New",
                                    "Foreign Used",
                                    "Nigerian Used"
                                ],
                                "transmission": [
                                    "AMT",
                                    "Automatic",
                                    "Manual",
                                    "CVT"
                                ],
                                "vehicles": [
                                    { 
                                        "brand": "BMW"
                                        "model": "3 Series"
                                    },....
                                ]
                            }
                        }
            }""")
        if endpoints == 'Update Password':
            st.header('Change user password')
            st.subheader('PATCH: www.carsplenty.com/api/v1/update-password')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "old_password": "password", #str
                "new_password": "password1" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                "Password updated"
            }""")
            pass
        if endpoints == 'Confirm Email':
            st.header('Verifies user email')
            st.subheader('GET: www.carsplenty.com/api/v1/confirm-email/{email-token}')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
            }""")
            st.write('Response - 200')
            st.code("""{
                    "Email confirmed" #str
            }""")
            st.write('Response - 403')
            st.code("""{
                    "Email confirmation link expired" #expires after an hour
            }""")
            pass
        if endpoints == 'Resend Confirmation':
            st.header('Resends email confirmation link')
            st.subheader('GET: www.carsplenty.com/api/v1/resend-link')
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
                    "token": "InRoZW9yZG9lQGVtYWlsLmNvbSI.YTj7FA.UTkqFlaeA_m234CNm0UWW-AUTOk"
            }""")
            pass
        if endpoints == 'Post Vehicle':
            st.header('Post vehicle for verification')
            st.subheader('POST: www.carsplenty.com/api/v1/post')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                    "brand": "Honda", #str
                    "model": "Civic", #str
                    "year": 2012, #int
                    "colour": "Black", #str
                    "condition": "Nigerian Used", #str
                    "transmission": "Automatic", #str
                    "mileage": "107000 km", #str
                    "registered": true, #bool
                    "location": "Lagos State, Ajah", #str
                    "price": "3,000,000", #str
                    "VIN": "DU4M4MYV7I3N", #str
                    "negotiable": true, #bool
                    "fuel": "Petrol", #str
                    "seats": "5", #str
                    "verified": false, #bool
                    "images": ["image_1", "image_2", "image_3", "image_4", "image_5", "image_6", "image_7"], #array
                    "main_image": "main_image", #str
            }""")
            st.write('Response - 200')
            st.code("""{
                    'Reviewing' #str
            }""")
            pass
        if endpoints == 'Post Verified Vehicle':
            st.header('Post verified vehicle')
            st.subheader('POST: www.carsplenty.com/api/v1/post-verified')
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
                    'Success' #str
                }""")
            st.write('Response - 400')
            st.code("""{
                    'Failed' #str
                }""")
            pass
        if endpoints == 'Follow User':
            st.header('Follow a favorite vehicle dealer')
            st.subheader('POST: www.carsplenty.com/api/v1/follow')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "following_id": "61266ddef4bf66e9ccdbe938" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                    "User followed"
                }""")
            pass
        if endpoints == 'Unfollow User':
            st.header('Follow a favorite vehicle dealer')
            st.subheader('DELETE: www.carsplenty.com/api/v1/unfollow')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "email": "theordoe@email.com" #str,
                "follow_id": "61266ddef4bf66e9ccdbe938" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                    "User Unfollowed"
            }""")
            pass
        if endpoints == 'Save Vehicle':
            st.header('Save a favorite vehicle')
            st.subheader('POST: www.carsplenty.com/api/v1/save')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "vehicle_id": "612512e4f90e9bdfe9545acc" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                    "Saved"
            }""")
            pass
        if endpoints == 'Saved Vehicles':
            st.header('Gets all saved vehicles by user')
            st.subheader('GET: www.carsplenty.com/api/v1/saved?id=6133a854917812bea8c5a51c')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                [
                    "_id": "6137d399750edde41dcb7a55",
                    "brand": "Honda",
                    "colour": "Black",
                    "condition": "Nigerian Used",
                    "fuel": "Petrol",
                    "location": "Lagos State, Egbeda",
                    "main_image": "main_images",
                    "model": "Accord",
                    "posted": "Tue, 07 Sep 2021 22:01:41 GMT",
                    "posted_by": "6133a854917812bea8c5a51c",
                    "price": "6,000,000",
                    "seat": "5",
                    "transmission": "Automatic",
                    "verified": false,
                    "year": "2014"
                },...]
            }""")
            pass
        if endpoints == 'Unsave Vehicle':
            st.header('Delete a saved vehicle')
            st.subheader('DELETE: www.carsplenty.com/api/auth/v1/save')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                "vehicle_id": "612512e4f90e9bdfe9545acc" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                    "Success"
                }""")
            pass
        if endpoints == 'Trending deals':
            st.header('Gets all trending deals')
            st.subheader('GET: www.carsplenty.com/api/v1/trending?page_number=1')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Request parameter')
            st.code("""{
                page_number = 1, #int
            }""")
            st.write('Response - 200')
            st.code("""{
                [{
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
            pass
        if endpoints == 'Start message':
            st.header('Start a message with another user')
            st.subheader('POST: www.carsplenty.com/api/auth/v1/start-message')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                    "sender_id": "61266f7ef4bf66e9ccdbe939" #str,
                    "receiver_id": "6126774a6456949ebda14bf0" #str,
                    "message": "Is the car available?" #str,
                    "vehicle_id": "613730553719c24549a6c0d4" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                        "Sent"
                }""")
            pass
        if endpoints == 'Send message':
            st.header('Send a message reply to another user')
            st.subheader('POST: www.carsplenty.com/api/auth/v1/send-message')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                    "chat": "yes but there are a lot of potential buyers" #str,
                    "message_id": "613f12713a08934396038836" #str
            }""")
            st.write('Response - 200')
            st.code("""{
                    "Sent"
                }""")
            pass
        if endpoints == 'Get messages':
            st.header('Gets all messages for a specific user')
            st.subheader('GET: www.carsplenty.com/api/auth/v1/messages')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "messages": [{
                        "chats": [
                            {
                                "sent_by": "John Doe", #str
                                "text": "Is the car still available?", #str
                                "time": "Mon, 13 Sep 2021 09:49:23 GMT" #str
                            },
                            {
                                "sent_by": "Jane Doe", #str
                                "text": "yes but there are a lot of potential buyers", #str
                                "time": "Mon, 13 Sep 2021 10:00:24 GMT" #str
                            }
                        ],
                        "message_id": "613f12713a08934396038836", #str
                        "receiver_info": {
                            "receiver_id": "61266ddef4bf66e9ccdbe938", #str
                            "receiver_name": "Jane Doe" #str
                            },
                            "sender_info": {
                                "sender_id": "6133a854917812bea8c5a51c", #str
                                "sender_name": "John Doe" #str
                            },
                        "vehicle_info": {
                            "brand": "Toyota", #str
                            "model": "Yaris", #str
                            "year": "2014", #str
                            "main_image": "image.jpg" #base64 str
                            }
                        }
                    ]
                },...]
            }""")
            pass
        if endpoints == 'Delete message':
            st.header('Delete a message with another user')
            st.subheader('DELETE: www.carsplenty.com/api/auth/v1/delete-message')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "Deleted" #str
                }""")
            pass