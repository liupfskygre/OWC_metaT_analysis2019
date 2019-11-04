#CU-denver
```
1) 'cd' to the destination directory on zenith where you want the files
2) Type:  sftp rdaly173@140.226.123.30
3) enter password  # "c9u!r-BOP"
You will now get a prompt that looks like this:
    sftp>
4) 'ls' to see directories available - you should have been given directory names by Ted
5) 'cd' into the directory with the files you want
6) use the 'get' command to copy the files you want  
    i.e. get [file name or names]
    
7) when finished type 'bye' to exit the sftp session

```

#
```
#/ORG-Data is full
#use here
cd /home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver
screen -S transfer
get *.gz

#move data from Salmonella to here
/home/ORG-Data-2/metaT_CU_denver2019/Salmonella_CU_denver_metaT2019
A, B, C, and Daly_
#

```
