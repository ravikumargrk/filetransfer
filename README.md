# filetransfer
* Add `--ssl-no-revoke` at the end of every command if needed.

## Upload file
```
curl URL -H "Authorization: <token>" -H "filename: filecopy.ext" --data-binary "@file.ext" 
```

## List files
```
curl URL -H "Authorization: <token>"
```

## Download file
```
curl URL -H "Authorization: <token>" -H "filename: filecopy.ext" > file.ext
```
