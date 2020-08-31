# python-mdbtools
example of using python to deal with mdb files on unix

#### mdbtools
Tools to facilitate the use of Microsoft Access databases


##### [GutHub source](https://github.com/brianb/mdbtools/)

##### [Install from](https://formulae.brew.sh/formula/mdbtools)

---
#### Prerequisites:

```brew install mdbtools```


#### How to use?
- get help
```shell script
python read_mdb.py --help
```
```shell script
usage: read_mdb.py [-h] [--file [FILE [FILE ...]]]
                   [--table [TABLE [TABLE ...]]] [--csv]

optional arguments:
  -h, --help            show this help message and exit
  --file [FILE [FILE ...]], -f [FILE [FILE ...]]
                        path to the file
  --table [TABLE [TABLE ...]], -t [TABLE [TABLE ...]]
                        table name to display
  --csv                 export table to csv file
```
- We expect you have file with the extension `file_name.mdb` and need to explore or extract its data

#### Example
##### --file
This command will print list of tables names inside the file
```shell script
python read_mdb.py --file file_name.mdb
```
##### --table
This command will print sample of the content of the table
```shell script
python read_mdb.py --file file_name.mdb --table table_name
```

##### --csv
This command will export all tables to csv files
```shell script
python read_mdb.py --file file_name.mdb --csv
```

##### --table --csv
This command will export specific table content to csv file
```shell script
python read_mdb.py --file file_name.mdb --table table_name --csv
```


