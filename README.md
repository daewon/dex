# DEX util

```
python remove-dup.py {name_length} {target_dir} {sort_by: mtime, size} {do_delete: true, false}'
```


## Example
Group the files in the ./src folder with four digits in front of the file name and the extension, leaving only the one with the largest mtime file.

```
python remove_dup.py 4 ./src mtime false
```
