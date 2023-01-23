# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('project_3')

values = SHEET.worksheet('data')

data_1 = values.get_all_values()

pprint(data_1)

print("This servey contains three questions. \n")


movie = input("Enter how many time in a week you watch a movie : \n")
game = input("Enter how many time in a week you play a game : \n")
work = input("Enter how many time in a week you work in the evening : \n")
gym = input("Enter how many time in a week you go the gym : \n")

data_str=[]

data_str.append(movie)
data_str.append(game)
data_str.append(work)
data_str.append(gym)

worksheet_to_update = SHEET.worksheet("data")

    # adds new row to the end of the current data
worksheet_to_update.append_row(data_str)

values = SHEET.worksheet('data')

data_2 = values.get_all_values()

pprint(data_2)