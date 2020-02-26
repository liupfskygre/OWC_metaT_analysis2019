#update 2020-Feb-26

#additional 10 samples avaliable 
```
cd /home/ORG-Data-2/metaT2018JGI_reads


```

#on mac, download url for all

```
cd /Users/pengfeiliu/A_Wrighton_lab/Wetland_project/OWC_metaT2018/JGI_metaT/OWC_metaT2018_part_II

grep -E 'Old\ Woman\ Creek\ 2018\ metatranscriptomes|Old\ Woman\ Creek\ Soil\ metatranscriptomes' get-directory.xml > get-directory_metaT2018partII.xml
#

sed -e 's/.* \(label=.*\) filename=.* \(url=.*\) project=.*$/\1\t\2/g' get-directory_metaT2018partII.xml >get-directory_metaT2018partII_link.xml

sed -i -e 's/.*metatranscriptomes \(.*\)".*url=.*\(url=.*\)"$/\1\t\2/g' get-directory_metaT2018partII_link.xml
sed -i -e 's/url=//g' get-directory_metaT2018partII_link.xml

```

## download filtering report
```
#on mac
grep 'filtered-report' get-directory_metaT2018partII_link.xml >get-directory_metaT2018partII_link.report
sed -i -e 's/\t/;/g' get-directory_metaT2018partII_link.report
grep -w -f JGI_updatelist26March2020.txt get-directory_metaT2018partII_link.report > get-directory_metaT2018partII_link10.report

#transfer to zenith and download

for line in $(cat get-directory_metaT2018partII_link10.report)
do
echo "${line}" # '\t' cause problem
v1="$(echo "${line}"|cut -f2 -d';')"
echo "${v1}"
v2="$(echo "${line}"|cut -f1 -d$';')"
echo "${v2}"

curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=newlifesky19870720' -c cookies > /dev/null

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=${v1}" -b cookies > "${v2}".filtered-report.txt
done
```

## download metaT, QC Filtered Raw Data (check the filterd report)

#with suffix: MTF.fastq.gz
#
```
#download on zenith
grep 'filter-MTF.fastq.gz' get-directory_metaT2018partII_link.xml >get-directory_metaT2018partII_link.mRNA
sed -i -e 's/\t/;/g' get-directory_metaT2018partII_link.mRNA
#53 (right)
grep -w -f JGI_updatelist26March2020.txt get-directory_metaT2018partII_link.mRNA > JGI_updatelist26March2020.mRNA
#10 

##
cd /home/ORG-Data-2/metaT2018JGI_reads

screen -r JGI_downloadI
  for line in $(cat JGI_updatelist26March2020.mRNA)
  do
  echo "${line}" # '\t' cause problem
  v1="$(echo "${line}"|cut -f2 -d';')"
  echo "${v1}"
  v2="$(echo "${line}"|cut -f1 -d$';')"
  echo "${v2}"

  curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=newlifesky19870720' -c cookies > /dev/null

  curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=${v1}" -b cookies > ./"${v2}".filter-MTF.fastq.gz
  done

#use "" if you want to have variable inside curl
```

## 
```

for file in *.gz 
do 
zcat ${file} > "${file%%.*}"tmp.fastq 
sickle pe -c "${file%%.*}"tmp.fastq -t sanger -M "${file%%.*}"_trimmed.fastq
fq2fa --paired --filter "${file%%.*}"_trimmed.fastq "${file%%.*}"_trimmed.fa
rm "${file%%.*}"tmp.fastq
rm "${file%%.*}"_trimmed.fastq
done

```

## assemblied mRNA contigs
```
grep 'assembly.contigs.fasta' get-directory_metaT2018partII_link.xml >get-directory_metaT2018partII_link.assembly.contigs
sed -i -e 's/Annotation\t//g' get-directory_metaT2018partII_link.assembly.contigs
sed -i -e 's/ /;/g' get-directory_metaT2018partII_link.assembly.contigs

#52 

```

