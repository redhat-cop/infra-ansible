Google Service account instructions
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
