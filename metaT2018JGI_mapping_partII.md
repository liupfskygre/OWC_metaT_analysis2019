#update 2020-Feb-26

#additional 10 samples avaliable 
```
cd /home/ORG-Data-2/metaT2018JGI_reads


```

#on mac, download url for all

```
cd /Users/pengfeiliu/A_Wrighton_lab/Wetland_project/OWC_metaT2018/JGI_metaT/OWC_metaT2018_part_II

grep 'Old\ Woman\ Creek\ 2018\ metatranscriptomes' get-directory.xml > get-directory_metaT2018partII.xml
#

sed -e 's/.* \(label=.*\) filename=.* \(url=.*\) project=.*$/\1\t\2/g' get-directory_metaT2018partII.xml >get-directory_metaT2018partII_link.xml

sed -i -e 's/.*metatranscriptomes \(.*\)".*url=.*\(url=.*\)"$/\1\t\2/g' get-directory_metaT2018partII_link.xml
sed -i -e 's/url=//g' get-directory_metaT2018partII_link.xml

```

## download filtering report
```

```

## download metaT, QC Filtered Raw Data (check the filterd report)
#
```
#download on zenith
grep 'filter-MTF.fastq.gz' get-directory_metaT2018partII_link.xml >get-directory_metaT2018partII_link.mRNA
sed -i -e 's/\t/;/g' get-directory_metaT2018partII_link.mRNA
#52 (right, all should be 53, see note 1 in partI)
grep -w -f JGI_updatelist26March2020.txt get-directory_metaT2018partII_link.mRNA > JGI_updatelist26March2020.mRNA


screen -S JGI_downloadI
for line in $(cat get-directory_metaT2018partI_link.mRNA)
do
echo "${line}" # '\t' cause problem
v1="$(echo "${line}"|cut -f2 -d';')"
echo "${v1}"
v2="$(echo "${line}"|cut -f1 -d$';')"
echo "${v2}"

curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=xxx' -c cookies > /dev/null

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=${v1}" -b cookies > ./metaT2018JGI_reads_partI/"${v2}".filter-MTF.fastq.gz
done

#use "" if you want to have variable inside curl
```


