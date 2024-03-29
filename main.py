import gspread, requests
from google.oauth2.service_account import Credentials
from common import *
from pathlib import Path

def main():
    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
    CREDENTIALS = Credentials.from_service_account_file(Path(__file__).parent / "creds.json", scopes=SCOPES)

    client = gspread.authorize(CREDENTIALS)
    sheet_id = "1B3wYLvuxOS3Ccr-mOckz_PFXt968fWB64PaoYVBEpN8"
    sheet = client.open_by_key(sheet_id)
    api_key = get_col_values(sheet.get_worksheet_by_id("1095471238"), "api-key")[1]

    sheet = sheet.sheet1
    headers = get_headers(sheet)
    urls = get_col_values(sheet, "linkedin url")
    names = get_col_values(sheet, "name")

    for index, url in enumerate(urls):
        try:
            if index == 0 or "scrapped" in ";".join(sheet.row_values(index + 1)).lower():
                continue
            
            req = requests.post("https://api.developers.kaspr.io/profile/linkedin", 
                                json=get_request_body(get_id(url), names[index]), 
                                headers=get_request_headers(api_key))
            if req.status_code == 200:
                res = req.json()
                
                profile = res.get("profile")
                cells_to_fill = get_cells_to_fill(profile)

                for cell in cells_to_fill:
                    sheet.update_cell(index + 1, headers.index(cell.get("name")) + 1, cell.get("value"))

        except:pass

if __name__ == "__main__":
    main()