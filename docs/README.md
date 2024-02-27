# Github Copilot Master Class Docs

# Notes:

## SSL Issue:
A common error with SSL in the Python examples is:
```
URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self-signed certificate in certificate chain (_ssl.c:1000)>
```
### Fix
Add the following to your Python Script:
```t
# Create an unverified SSL context
ssl._create_default_https_context = ssl._create_unverified_context
```


---

#### [../back](../README.md)
