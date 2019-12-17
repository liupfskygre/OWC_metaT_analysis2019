# this is a markdown file for the mapping of OWC-metaT2018 from JGI to references

1. to owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
2. to DRAM annotated genes (==>gene/pathway expression)
3. to all dereplicated OWC  mcrA (from contigs,==>transcripts to mcrA/methanogens )

## download metaT from JGI, 109 samples

**ref**
```
##to do, change to this: curl 'https://signon.jgi.doe.gov/signon/create'
#https://github.com/liupfskygre/OWC_wetland_metaG_testing/blob/master/JGI_downloading.md
#https://genome.jgi.doe.gov/portal/help/download.jsf
```

**download url for all**
```
name="Frogenwetlasoils

#login and download cookies
curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=password=xx' -c cookies > /dev/null

#check the dataset to, get the path of your data
curl 'https://genome.jgi.doe.gov/portal/ext-api/downloads/get-directory?organism=Frogenwetlasoils' -b cookies > Frogenwetlasoils.xml #not working, manual downloading xml


```
**wkdir**
```
#mRNA reads download to
/home/ORG-Data-2/metaT2018JGI_reads

#mapping
/home/projects/Wetlands/OWC_metaT2018_analysis



#reads from Denver
#/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver
```

**get file url**
```
grep 'Old\ Woman\ Creek\ 2018\ metatranscriptomes' get-directory.xml > get-directory_metaT2018partI.xml
#252

sed -e 's/.* \(label=.*\) filename=.* \(url=.*\) project=.*$/\1\t\2/g' get-directory_metaT2018partI.xml >get-directory_metaT2018partI_link.xml
sed -i -e 's/.*metatranscriptomes \(.*\)".*url=.*\(url=.*\)"$/\1\t\2/g' get-directory_metaT2018partI_link.xml
sed -i -e 's/url=//g' get-directory_metaT2018partI_link.xml


#list of url download like this
#todo ==> like this
Aug_OW2_C1_D2_A;/OldWomW2_C1_D2_A/download/_JAMO/5de68af8e08d44553ef59c77/52332.4.310648.CTGAAGCT-AGCTTCAG.filter-MTF.fastq.gz

##use this demo
/home/liupf
sed -e 's/.* \(label=.*\) filename=.* \(url=.*\) project=.*$/\1\t\2/g' example.xml >example_link.xml
sed -i -e 's/.*metatranscriptomes \(.*\)".*url=.*\(url=.*\)"$/\1\t\2/g' example_link.xml
#Aug_M1_C3_D2	url=/OldWomg_M1_C3_D2/download/_JAMO/5de66ef1e08d44553ef59ba2/52332.4.310648.GTGCCATA-TATGGCAC.filter-MTF.fastq.gz


#sed -e 's/.*url=\(.*\) project=.*/\1/g' Frogenwetlasoils_metaT.xml> Frogenwetlasoils_metaT_link.xml
#sed -i -e 's/\"$//g' Frogenwetlasoils_metaT.xml> Frogenwetlasoils_metaT_link.txt
#Frogenwetlasoils_metaT_link.txt
```


**download filtering report**
```
grep 'filtered-report' get-directory_metaT2018partI_link.xml >get-directory_metaT2018partI_link.report
sed -i -e 's/\t/;/g' get-directory_metaT2018partI_link.report

for line in $(cat get-directory_metaT2018partI_link.report)
do
echo "${line}" # '\t' cause problem
v1="$(echo "${line}"|cut -f2 -d';')"
echo "${v1}"
v2="$(echo "${line}"|cut -f1 -d$';')"
echo "${v2}"

curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=xx' -c cookies > /dev/null

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=${v1}" -b cookies > "${v2}".filtered-report.txt
done
mv *.filtered-report.txt metaT2018JGI_reads_partI
```


**download metaT**
```

#download on zenith
grep 'filter-MTF.fastq.gz' get-directory_metaT2018partI_link.xml >get-directory_metaT2018partI_link.mRNA
sed -i -e 's/\t/;/g' get-directory_metaT2018partI_link.mRNA

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

## reads preparation

**check QC and QC filtering by sickle**
```
sickle pe -f F_S46_L004_R1_001tmp.fastq -r F_S46_L004_R2_001tmp.fastq -o AugM1C1D5C_R1_trimmerd.fastq -p AugM1C1D5C_R2_trimmerd.fastq -s AugM1C1D5C_trimmed.singles.fastq -t sanger 

If you have one file with interleaved forward and reverse reads:
Usage: sickle pe [options] -c <interleaved input file> -t <quality type> -m <interleaved trimmed paired-end output> -s <trimmed singles file>

fq2fa --paired --filter  R1R2_All_trimmed.fastq R1R2_All_trimmed.fa
--paired                           if the reads are paired-end in one file
--merge                            if the reads are paired-end in two files
--filter                           filter out reads containing 'N'
```

## reference preparation

1. owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
```

```



2. DRAM annotated genes (==>gene/pathway expression)

```

```

3. all dereplicated OWC  mcrA (from contigs,==>transcripts to mcrA/methanogens )
```

```


## mapping to references; keep bam file

#==>to discuss
**bowtie2 or bbmap**

#==>to discuss
**parameter setting and filtering (mismatch)**

1. to owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
```

```

2. to DRAM annotated genes (==>gene/pathway expression)
```

```

3. to all dereplicated OWC  mcrA (from contigs,==>transcripts to mcrA/methanogens )
```


```



