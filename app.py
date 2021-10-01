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
            'Refresh',
            'User',
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
            st.subheader('GET: www.carsplenty.com/api/v1/vehicles?limit=5&offset=0')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Request Parameter')
            st.code("""
            {
                "limit" = 5 
                "offset" = 0
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
            st.subheader('GET: www.carsplenty.com/api/v1/vehicle/6136c1543719c24549a6c0cf')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
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
                "refresh_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYzMjU2MTI2Nywian
                RpIjoiMmNiMDAxNWYtMDkxNS00NTQ0LWJjNzItNjQwYzM0NzQ5YWUwIiwidHlwZSI6InJlZnJlc2giLCJzdWIiOiI2MTI2NmRkZWY
                0YmY2NmU5Y2NkYmU5MzgiLCJuYmYiOjE2MzI1NjEyNjcsImV4cCI6MTYzNTE1MzI2N30.6QbHkIY0ViflYmRjJPUowWTZw-U9lQzkQ
                fMOyd6p84o",
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
        if endpoints == 'Refresh':
            st.header('Refreshes access tokens')
            st.subheader('POST: www.carsplenty.com/api/v1/refresh')
            st.write('Headers')
            st.code('"Authorization": "refresh_token"')
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
            pass
        if endpoints == 'User':
            st.header('Gets user details')
            st.subheader('POST: www.carsplenty.com/api/v1/user')
            st.write('Headers')
            st.code('"Authorization": "Bearer token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.write('Response - 200')
            st.code("""{
                "user_data": {
                    "account_created": "1 month ago",
                    "email": "janedoe@email.com",
                    "followers": 4,
                    "following": [
                        "61266f7ef4bf66e9ccdbe939"
                    ],
                    "last_seen": "15 hours ago",
                    "name": "Jane Doe",
                    "phone_number": "07020005000",
                    "profile_picture": "image_",
                    "user_id": "61266ddef4bf66e9ccdbe938"
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
        if endpoints == 'Follow User':
            st.header('Follow a favorite vehicle dealer')
            st.subheader('POST: www.carsplenty.com/api/v1/follow/61266ddef4bf66e9ccdbe938')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "User followed"
                }""")
            pass
        if endpoints == 'Unfollow User':
            st.header('Follow a favorite vehicle dealer')
            st.subheader('DELETE: www.carsplenty.com/api/v1/unfollow/61266ddef4bf66e9ccdbe938')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "User Unfollowed"
            }""")
            pass
        if endpoints == 'Save Vehicle':
            st.header('Save a favorite vehicle')
            st.subheader('POST: www.carsplenty.com/api/v1/save/612512e4f90e9bdfe9545acc')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.write('Response - 200')
            st.code("""{
                    "Saved"
            }""")
            pass
        if endpoints == 'Saved Vehicles':
            st.header('Gets all saved vehicles by user')
            st.subheader('GET: www.carsplenty.com/api/v1/saved')
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
            st.subheader('DELETE: www.carsplenty.com/api/v1/unsave/612512e4f90e9bdfe9545acc')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "Success"
                }""")
            pass
        if endpoints == 'Trending deals':
            st.header('Gets all trending deals')
            st.subheader('GET: www.carsplenty.com/api/v1/trending?limit=5&offset=0')
            st.write('Headers')
            st.code('"Authorization": "None"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Request parameter')
            st.code("""{
                "limit" = 5 
                "offset" = 0
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
            st.subheader('POST: www.carsplenty.com/api/v1/start-message')
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
            st.subheader('POST: www.carsplenty.com/api/v1/send-message')
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
            st.subheader('GET: www.carsplenty.com/api/v1/messages')
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
            st.subheader('DELETE: www.carsplenty.com/api/v1/delete-message/613f12713a08934396038836')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "Deleted" #str
                }""")
            pass
    if sub_nav == 'Auction':
        endpoints = st.sidebar.selectbox(
        "Endpoints",
        [
            'Auctions', 
            'Auction',
            'Bid',
        ])
        if endpoints == 'Auctions':
            st.header('Gets all vehicles up for auction')
            st.subheader('GET: www.carsplenty.com/api/v1/auctions')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{
                    "next_page": "?limit=5&offset=5",
                    "prev_page": "?limit=5&offset=-5",
                    "vehicles": [
                        {
                            "_id": "615327251e50c460ebdf3289",
                            "brand": "Toyota",
                            "color": "Black",
                            "completed": false,
                            "condition": "Foreign Used",
                            "current_bid": 550000,
                            "end_time": "Sun, 03 Oct 2021 02:19:35 GMT",
                            "fuel": "Petrol",
                            "main_image": "main_image",
                            "mileage": "166200 km",
                            "minimum_bid": 500000,
                            "model": "Matrix",
                            "posted": "3 days ago",
                            "selling_price": 700000,
                            "start_time": "Fri, 01 Oct 2021 02:19:35 GMT",
                            "status": true,
                            "transmission": "Automatic",
                            "year": "2007"
                        },...]
                }""")
            pass
        if endpoints == 'Auction':
            st.header('Gets details of vehicle up for auction')
            st.subheader('GET: www.carsplenty.com/api/v1/auction/615327251e50c460ebdf3289')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Response - 200')
            st.code("""{              
                    "auction": {
                        "_id": "615327251e50c460ebdf3289",
                        "bids": [
                            {
                                "bid": 550000,
                                "bidder": "Ron Doe",
                                "bidder_email": "rondoe@email.com",
                                "bidder_id": "61365a6b9578b7708a9791d3",
                                "bidder_number": "07020006000",
                                "time": "Tue, 28 Sep 2021 17:34:44 GMT"
                            }
                        ],
                        "brand": "Toyota",
                        "color": "Black",
                        "completed": false,
                        "condition": "Foreign Used",
                        "current_bid": 550000,
                        "end_time": "Sun, 03 Oct 2021 02:19:35 GMT",
                        "end_timeago": "in 1 day",
                        "fuel": "Petrol",
                        "images": [
                            "image_1",
                            "image_2",
                            "image_3",
                            "image_4"
                        ],
                        "inspector_report": "report.pdf",
                        "main_image": "main_image",
                        "mileage": "166200 km",
                        "minimum_bid": 500000,
                        "model": "Matrix",
                        "posted": "3 days ago",
                        "seats": "5",
                        "selling_price": 700000,
                        "start_time": "Fri, 01 Oct 2021 02:19:35 GMT",
                        "start_timeago": "14 hours ago",
                        "status": true,
                        "transmission": "Automatic",
                        "year": "2007"
                    },
                    "latest_bid": {
                        "bid": 550000,
                        "time": "10 hours ago""
                    },
                    "status": true #If false bid will be disabled
                }""")
            pass
        if endpoints == 'Bid':
            st.header('Bid for vehicle up for auction')
            st.subheader('POST: www.carsplenty.com/api/v1/bid')
            st.write('Headers')
            st.code('"Authorization": "Bearer Token"')
            st.code('"Content-type": "Application/json"')
            st.code('"Charset": "UTF-8"')
            st.write('Json request')
            st.code("""{
                    "auction_id": "615327251e50c460ebdf3289",
                    "new_bid": 550000
            }""")
            st.write('Response - 200')
            st.code("""{              
                    "Bid placed"
                }""")
            pass