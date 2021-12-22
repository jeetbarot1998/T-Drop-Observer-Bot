import os

DEBUG = False  # Set False on server
Secret_key = ['b898c8a4e8d3ed914f6ff61cf244de2c8a28a58c857a4473a04760e886595950', '79fe38c34cf65cad8c07d8ccdb63f349abd0450b87962aacc2b82e4c693ef093' ]
Private_key = 'barotjeet98@gmail.com'
# jobs_by_industry_data_url = "https://data.ny.gov/api/views/pxa9-czw8/rows.json"
# covid_daily_count_data_url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
#
base_url_for_movie = 'https://www.google.com/search?q='

user_detials_list = [{ 'email':'jeetbarot1998@gmail.com', 'Name': 'Jeet S Barot', 'Age': 23, 'id': 0, 'user_type': 'Owner'},
                     {'email':'ashwinidroid@gmail.com' , 'Name': 'Ashwitty Kumar', 'Age': 22, 'id': 1, 'user_type': 'Owner'},
                     {'email':'rubenmukherjee@outlook.com' , 'Name': 'Ruben Mukherjee', 'Age': 26, 'id': 2, 'user_type': 'Owner'}]


check_for_scheduler_status = "RUN"

SQL_ALCHEMY_DB_URL = os.environ.get('DATABASE_URL')