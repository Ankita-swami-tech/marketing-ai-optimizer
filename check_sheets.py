import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds",
         "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "service_account.json", scope
)

client = gspread.authorize(creds)

print("\n🔍 Sheets visible to the Service Account:\n")

files = client.list_spreadsheet_files()
for f in files:
    print(f"{f['name']}  -->  {f['id']}")
