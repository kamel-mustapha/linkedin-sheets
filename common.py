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
    id_index = 0
    for index, url in enumerate(urls):
        if url == "in": id_index = index + 1
    return urls[id_index]

def get_cells_to_fill(profile):
    return [
        {
            "name": "id",
            "value": profile.get("id") if profile.get("id") else "/"
        },
        {
            "name": "first name",
            "value": profile.get("firstName") if profile.get("firstName") else "/"
        },
        {
            "name": "last name",
            "value": profile.get("lastName") if profile.get("lastName") else "/"
        },
        {
            "name": "company name",
            "value": profile.get("companyName") if profile.get("companyName") else "/"
        },
        {
            "name": "title",
            "value": profile.get("title") if profile.get("title") else "/"
        },
        {
            "name": "phones",
            "value": ";".join(profile.get("phones")).replace("+", "") if profile.get("phones") else "/"
        },
        {
            "name": "emails directs",
            "value": ";".join(profile.get("directEmails")) if profile.get("directEmails") else "/"
        },
        {
            "name": "work emails",
            "value": ";".join(profile.get("workEmails")) if profile.get("workEmails") else "/"
        },
        {
            "name": "emails",
            "value": ";".join(list(map(lambda x: x.get("email"),profile.get("emails")))) if profile.get("email") else "/"
        },
        {
            "name": "location",
            "value": profile.get("location") if profile.get("location") else "/"
        },
        {
            "name": "scrapped",
            "value": "scrapped"
        }
    ]