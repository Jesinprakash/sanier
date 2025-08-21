import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.conf import settings

def get_google_sheet():
    scope = ["https://spreadsheets.google.com/feeds", 
             "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        settings.GOOGLE_SHEETS_CREDENTIALS, scope
    )
    client = gspread.authorize(creds)
    return client.open_by_key(settings.GOOGLE_SHEET_ID).sheet1


def add_or_update_google_sheet(obj_id, name, dob):
    sheet = get_google_sheet()
    records = sheet.get_all_records()

    # Check if record exists by ID
    for idx, row in enumerate(records, start=2):  # start=2 because row 1 = header
        if row.get("ID") == obj_id:
            # Update row
            sheet.update(f"A{idx}:C{idx}", [[obj_id, name, str(dob)]])
            return

    # If not found → append new row
    sheet.append_row([obj_id, name, str(dob)])
