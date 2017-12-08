set-timezone role
==========

This role can be used to set the timezone of your system.  
Available timezones can be captured via `timedatectl list-timezones`

## Requirements

This role need to be executed by a user with `beome` privileges

Below is an example inventory for the timezone:

```
timezone: America/Denver
```

### Note
If the value is not set the role is skipped

