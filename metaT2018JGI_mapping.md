# this is a markdown file for the mapping of OWC-metaT2018 from JGI to references

1. to owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
2. to DRAM annotated genes (==>gene/pathway expression)
3. to all dereplicated OWC  mcrA (from contigs,==>transcripts to mcrA/methanogens )

## download metaT from JGI, 109 samples

#https://github.com/liupfskygre/OWC_wetland_metaG_testing/blob/master/JGI_downloading.md

**download url for all**
```
name="Frogenwetlasoils

#login and download cookies
curl 'https://signon-old.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=xxx' -c cookies > /dev/null

#check the dataset to, get the path of your data
curl 'https://genome.jgi.doe.gov/portal/ext-api/downloads/get-directory?organism=Frogenwetlasoils' -b cookies > Frogenwetlasoils.xml

```
**get file url**
```
#grep 'Old\ Woman\ Creek\ 2018\ metatranscriptomes' download.xml > download_OWC_metaT.xml

#list of url download like this
#/OldWomW2_C1_D2_A/download/_JAMO/5de68af8e08d44553ef59c77/52332.4.310648.CTGAAGCT-AGCTTCAG.filter-MTF.fastq.gz
#??OldWomW2_C1_D2_A

#mRNA file download from JGI
grep 'Old\ Woman\ Creek\ 2018\ metatranscriptomes' Frogenwetlasoils.xml  > Frogenwetlasoils_metaT.xml 

sed -e 's/.*url=\(.*\) project=.*/\1/g' Frogenwetlasoils_metaT.xml> Frogenwetlasoils_metaT_link.xml

sed -i -e 's/\"$//g' Frogenwetlasoils_metaT.xml> Frogenwetlasoils_metaT_link.txt

#Frogenwetlasoils_metaT_link.txt


```

**download metaT**
```

#download on zenith
cd /home/projects/Wetlands/2018_sampling/JGI_assemblies
mkdir OWC_JGI_metaspades_sam
cd /home/projects/Wetlands/2018_sampling/JGI_assemblies/OWC_JGI_metaspades_sam

screen -S JGI_sam_download

for line in $(cat Frogenwetlasoils_metaT_link.txt)
do
echo "${line}"
v1="${line}"
echo "${v1}"
v2="$(echo "${line}"|cut -f2 -d'/')" ##change to file name, JGI gave bad name 
echo "${v2}"

curl 'https://signon-old.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=newlifesky19870720' -c cookies > /dev/null

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=${v1}" -b cookies > "${v2}".sam.gz

done
#use "" if you want to have variable inside curl
```

## reads preparation

**QC filtering by sickle**
```

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

**bowtie2 or bbmap**

**parameter setting and filtering**

1. to owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
```

```

2. to DRAM annotated genes (==>gene/pathway expression)
```

```

3. to all dereplicated OWC  mcrA (from contigs,==>transcripts to mcrA/methanogens )
```


```



