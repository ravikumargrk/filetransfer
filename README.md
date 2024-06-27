# filetransfer

## Upload file

Note add `--ssl-no-revoke` at the end if SSL check if needed.

```
curl URL -H "Authorization: <token>" -H "filename: filecopy.ext" --data-binary "@file.ext" 
```

## Download file
Note add `--ssl-no-revoke` at the end if SSL check if needed.

```
curl URL -H "Authorization: <token>" -H "filename: filecopy.ext" > file.ext
```
