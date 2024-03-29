def get_headers(sheet):
    headers = sheet.row_values(1)
    headers = list(map(lambda x: x.lower().strip(), headers))
    return headers

def get_col_values(sheet, col_name):
    headers = get_headers(sheet)
    return sheet.col_values(headers.index(col_name) + 1)

def get_request_body(id, name):
    return {
        "id": id,
        "name": name,
        "dataToGet": [
            "phone",
            "workEmail",
            "directEmail"
        ]
    }

def get_request_headers(token):
    return {
        "Content-Type": "application/json",
        "Content": "application/json",
        "Accept": "application/json",
        "accept-version": "v2.0",
        "authorization": f"Bearer {token}"
    }

def get_id(url):
    urls = url.split("/")
    return urls[4]



def get_cells_to_fill(profile):
    return [
        {
            "name": "id",
            "value": profile.get("id")
        },
        {
            "name": "first name",
            "value": profile.get("firstName")
        },
        {
            "name": "last name",
            "value": profile.get("lastName")
        },
        {
            "name": "company name",
            "value": profile.get("companyName")
        },
        {
            "name": "title",
            "value": profile.get("title")
        },
        {
            "name": "phones",
            "value": ";".join(profile.get("phones")).replace("+", "")
        },
        {
            "name": "emails directs",
            "value": ";".join(profile.get("directEmails"))
        },
        {
            "name": "work emails",
            "value": ";".join(profile.get("workEmails"))
        },
        {
            "name": "emails",
            "value": ";".join(list(map(lambda x: x.get("email"),profile.get("emails"))))
        },
        {
            "name": "location",
            "value": profile.get("location")
        },
        {
            "name": "scrapped",
            "value": "scrapped"
        }
    ]