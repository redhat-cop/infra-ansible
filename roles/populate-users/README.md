#CREATE IDENTITIES IN AN EXISTING IDM 

An ansible role that will consume a google sheet and insert that data into and existing IDM (IPA). the format of the sheet should include a header row

```
user_name, first_name, last_name, email, expiration_date, group
```

Only expiration_date is not required. If expiration_date is not provide the user's account will never expire (no lockout). The format for expiration date is ISO 8601. A valid example is ```2018-11-30T22:38:40.326Z```

A google service account is needed to download the sheet. See this [Google document](https://developers.google.com/identity/protocols/OAuth2ServiceAccount) for information about creating a service account

