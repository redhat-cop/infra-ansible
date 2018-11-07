# Google Sheets Dynamic Inventory

## Google Service account instructions
-----------------------------------
1. Go to the [Google Developer Console](https://console.developers.google.com/project).
2. Go to the credentials page.
3. Press `Create Credentials` -> `Service account key`.
4. Select `New service account`.
5. Set the Role to `Project -> Editor`. Set the account name and account ID as desired.
6. Create the key with type `json`.
7. Save this .json file to your desired location (the path will need to be referenced later). Note: If storing with your code in a repo, add this file to the `.gitignore`.
8. In the credentials file, find the `client_email` key and copy the matching value. This email is the service account.
9. Add that service account email as an editor into your Google sheet.

## System pre-reqs
There are some Python libraries which need to be available on the system running this inventory. Alongside this library is a `requirements.txt` which can be installed with pip using:

`pip install -r requirements.txt`

## Testing that it work
This needs a Google Sheet to exist with the following format:

| user_name | first_name | last_name | email                 | expiration_date | role      |
|-----------|------------|-----------|-----------------------|-----------------|------------|
| brock.lee     | Brock      | Lee       | brock.lee@example.com |                 | admin |

To test that it works, run `python gsheets.py --list`
