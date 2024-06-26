# filetransfer

## Upload file

Note add `--ssl-no-revoke` at the end if SSL check if needed.

```
curl URL --data-binary "@file.ext" -H "Authorization: <token>" -H "filename: file.ext"
```

## Download file
Note add `--ssl-no-revoke` at the end if SSL check if needed.

```
curl URL -H "Authorization: <token>" -H "filename: file.ext" > file.ext --ssl-no-revoke
```
