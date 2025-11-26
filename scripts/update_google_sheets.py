import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# -------------------------------------------------------
# GOOGLE SHEETS CONFIG
# -------------------------------------------------------
SPREADSHEET_NAME = "Marketing_AI_Data"
CSV_FILES = {
    "Google_News": "data/google_news_latest.csv",
    "Google_Trends": "data/google_trends_latest.csv",
    "Reddit": "data/reddit_latest.csv",
    "YouTube": "data/youtube_latest.csv",
}

# -------------------------------------------------------
# AUTHENTICATE GOOGLE SHEETS
# -------------------------------------------------------
def get_client():
    scope = [
        "https://www.googleapis.com/auth/spreadsheets",
        "https://www.googleapis.com/auth/drive",
    ]

    creds = ServiceAccountCredentials.from_json_keyfile_name(
        "credentials/sheets_key.json", scope
    )

    return gspread.authorize(creds)


# -------------------------------------------------------
# UPLOAD ALL CSVs TO GOOGLE SHEET
# -------------------------------------------------------
def upload_to_sheet():
    print("🚀 Uploading data to Google Sheets...")

    client = get_client()

    # Open sheet
    try:
        sheet = client.open(SPREADSHEET_NAME)
    except:
        print("❌ Sheet not found. Creating new sheet...")
        sheet = client.create(SPREADSHEET_NAME)

    # Share with owner (optional)
    # sheet.share("youremail@gmail.com", perm_type="user", role="writer")

    # Update each tab
    for tab_name, file_path in CSV_FILES.items():
        print(f"📌 Updating tab: {tab_name}")

        df = pd.read_csv(file_path)

        try:
            worksheet = sheet.worksheet(tab_name)
        except:
            worksheet = sheet.add_worksheet(title=tab_name, rows="1000", cols="20")

        worksheet.clear()

        worksheet.update([df.columns.values.tolist()] + df.values.tolist())

    print("🎉 ALL DATA UPDATED SUCCESSFULLY!")


# -------------------------------------------------------
# RUN
# -------------------------------------------------------
if __name__ == "__main__":
    upload_to_sheet()
