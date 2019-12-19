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
curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=xxx' -c cookies > /dev/null

#check the dataset to, get the path of your data
#curl 'https://genome.jgi.doe.gov/portal/ext-api/downloads/get-directory?organism=Frogenwetlasoils' -b cookies > Frogenwetlasoils.xml  #also work

#manual downloading xml ==>get-directory.xml


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
**note1**
```
#43 is avaliable, only 42 in the list, 
Aug_M1_C1_D1_A is missing
# Old Woman Creek Soil metatranscriptomes Aug_M1_C1_D1_A, missing 2018

#screen -r JGI_donwload_D1A
#download
curl 'https://signon.jgi.doe.gov/signon/create' --data-urlencode 'login=pengfei.liu@mpi-marburg.mpg.de' --data-urlencode 'password=xxx' -c cookies > /dev/null

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=/OldWomM1_C1_D1_A/download/_JAMO/5de62283e08d44553ef59910/52332.4.310648.TTACGGCT-AGCCGTAA.filter-MTF.fastq.gz" -b cookies > ./metaT2018JGI_reads_partI/Aug_M1_C1_D1_A.filter-MTF.fastq.gz

curl "https://genome.jgi.doe.gov/portal/ext-api/downloads/get_tape_file?blocking=true&url=/OldWomM1_C1_D1_A/download/_JAMO/5de62284e08d44553ef59913/52332.4.310648.TTACGGCT-AGCCGTAA.filtered-report.txt" -b cookies > ./Aug_M1_C1_D1_A.filtered-report.txt
```




## reads preparation

**check QC and QC filtering by sickle**
```
#
screen -r JGI_downloadI
cd /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI

for file in *.gz 
do 
zcat ${file} > "${file%%.*}"tmp.fastq 
sickle pe -c "${file%%.*}"tmp.fastq -t sanger -M "${file%%.*}"_trimmed.fastq
fq2fa --paired --filter "${file%%.*}"_trimmed.fastq "${file%%.*}"_trimmed.fa
rm "${file%%.*}"tmp.fastq
rm "${file%%.*}"_trimmed.fastq
done

#If you have one file with interleaved forward and reverse reads:
#Usage: sickle pe [options] -c <interleaved input file> -t <quality type> -M <interleaved trimmed paired-end output> 
#-m to go with -s <trimmed singles file>

#fq2fa --paired --filter  R1R2_All_trimmed.fastq R1R2_All_trimmed.fa
--paired                           if the reads are paired-end in one file
--merge                            if the reads are paired-end in two files
--filter                           filter out reads containing 'N'
```
## quaity summary of JGI data
```
grep 'Output' *filtered-report.txt > OWC_metaT2018_JGI_partI_summary.txt

#note, this is all rRNA filtered Pair-End data, with vary 2.6Giga bases to 21.2Gb; should be great;

```



## reference preparation
## mapping to references; keep bam file

1. owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
```
#https://github.com/liupfskygre/OWC_metaT_analysis2019/blob/master/metaT2018_Denver_to_MGdb89.md
/home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db
mkdir OWC_metaT2018_to_MG89
grep -c '>' OWC_methanogens_DB89_cat.fna
#23049

cd OWC_metaT2018_to_MG89
rsem-prepare-reference ../OWC_methanogens_DB89_cat.fna --bowtie2 OWC_methanogens_DB89_cat
#--star 
```

1. to owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
```
# reads: /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI 
ls -1 *.filter-MTF.fastq.gz > /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partI_list.txt


cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89

screen -S OWC_MG89_RSEM
#for sample in $(cat metaT2018JGI_reads_partI_list.txt)
#try one,  Aug_M1_C1_D1_A
for sample in Aug_M1_C1_D1_A

screen -r OWC_MG89_RSEM

for sample in $(cat metaT2018JGI_reads_partI_list.txt) #remove Aug_M1_C1_D1_A
do
echo ${sample}
reformat.sh in=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_trimmed.fa out1=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R1_trimmed.fa out2=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R2_trimmed.fa

rsem-calculate-expression --bowtie2 --no-qualities -p 20 --paired-end /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R1_trimmed.fa /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R2_trimmed.fa OWC_methanogens_DB89_cat ${sample}_MG89_RSEM &>${sample}_MG89_RSEM.log
done 
```

## keep only R1 and R2, remove fq.gz and interleaved.fa, 
#compress R1 and R2 to .gz file before rsem, rsem could take gz file
```
for sample in $(cat metaT2018JGI_reads_partI_list.txt) 
do
gzip ${sample}_R1_trimmed.fa
gzip ${sample}_R1_trimmed.fa
rm ${sample}_trimmed.fa
rm ${sample}.filter-MTF.fastq.gz
done
```


2. DRAM annotated genes (==>gene/pathway expression)

```
#wkdir
/home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/Methanogens_cleanDB_26Spet2019_dRep/dereplicated_genomes/DRAM_MGdb89_25k_annotations
#grep -c '>' genes.fna; 141317
#grep -c 'grade' genes.fna; 141317

sed -e 's/ grade.*$//g' genes.fna > MG89_DRAM_genes_hf.fna
MG89_DRAM_genes_hf.fna

mkdir metaT2018JGI_to_MG89_DRAM_genes
cd metaT2018JGI_to_MG89_DRAM_genes

cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/Methanogens_cleanDB_26Spet2019_dRep/dereplicated_genomes/DRAM_MGdb89_25k_annotations/metaT2018JGI_to_MG89_DRAM_genes

#creat ref for bowtie2
rsem-prepare-reference ../MG89_DRAM_genes_hf.fna --bowtie2 MG89_DRAM_genes_hf

screen -S MG89_DRAM_genes_hf

for sample in $(cat metaT2018JGI_reads_partI_list.txt) 
do
echo ${sample}

rsem-calculate-expression --bowtie2 --no-qualities -p 30 --paired-end /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R1_trimmed.fa /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R2_trimmed.fa MG89_DRAM_genes_hf ${sample}_mcrA_RSEM &>${sample}_genes_RSEM.log
done 

```
3. to all dereplicated OWC  mcrA (from contigs,==>transcripts to mcrA/methanogens )
```
#wkdir 
cd /home/projects/Wetlands/OWC_mcrA_from_assemblies
OWC_mcrA_all_clean_dedup_w_nt.faa
OWC_mcrA_all_clean_dedup.fna 
#987
#further checked with eggnog and hmmsearch CD blast

mkdir metaT2018JGI_to_mcrA_all
#creat ref for bowtie2
rsem-prepare-reference ../OWC_mcrA_all_clean_dedup.fna --bowtie2 OWC_mcrA_all_clean_dedup

cd /home/projects/Wetlands/OWC_mcrA_from_assemblies/metaT2018JGI_to_mcrA_all
cp /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partI_list.txt ./

screen -S OWC_mcrA_all_clean_dedup

for sample in $(cat metaT2018JGI_reads_partI_list.txt) 
do
echo ${sample}

rsem-calculate-expression --bowtie2 --no-qualities -p 10 --paired-end /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R1_trimmed.fa /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/${sample}_R2_trimmed.fa OWC_mcrA_all_clean_dedup ${sample}_mcrA_RSEM &>${sample}_mcrA_RSEM.log
done 
```


#==>to discuss
**bowtie2 or bbmap**
==> use bowtie2 and RESM default setting

#==>to discuss
**parameter setting and filtering (mismatch)**
==> could be filtering later on



## gff based Counting mapped reads per gene??
```


```


## expected output

```
TPM for each Methanogen genomes, genes and each mcrA
```

## clean 
```

```

**compare bbmap mapping (JGI summary) and pileup.sh using correlation on FPKM**
```
#pileup summary of rpkm, to compare the FPKM from RSEM with the same bam file
pileup.sh in=Aug_M1_C1_D1_C_MG89_RSEM.transcript.bam rpkm=Aug_M1_C1_D1_C_MG89_RSEM.pileup.rpkm.txt 32bit=t
#RSEM use effective_length_i to calculate FPKM from TPM, R2=0.833 between pileup and RSEM FPKM

#bbmap to generate bam file
screen -S bbmap

screen -r bbmap

#D1_C
bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/Aug_M1_C1_D1_C_R1_trimmed.fa in2=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/Aug_M1_C1_D1_C_R2_trimmed.fa ambiguous=random outm=Aug_M1_C1_D1_C_MGdb89_bbmap.bam t=10 -Xmx112g
==>95M bam, 2.5G for 

#D3_C
bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/Aug_M1_C1_D3_C_R1_trimmed.fa in2=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/Aug_M1_C1_D3_C_R2_trimmed.fa ambiguous=random outm=Aug_M1_C1_D3_C_MGdb89_bbmap.bam t=10 -Xmx112g &>Aug_M1_C1_D3_C_MGdb89_bbmap.log

#D5_C
bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/Aug_M1_C1_D5_C_R1_trimmed.fa in2=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partI/Aug_M1_C1_D5_C_R2_trimmed.fa ambiguous=random outm=Aug_M1_C1_D5_C_MGdb89_bbmap.bam t=10 -Xmx112g&>Aug_M1_C1_D5_C_MGdb89_bbmap.log

#also compare to data from UC denver 

pileup.sh in=Aug_M1_C1_D1_C_MGdb89_bbmap.bam rpkm=Aug_M1_C1_D1_C_MG89_bbmap.pileup.rpkm.txt 32bit=t
pileup.sh in=Aug_M1_C1_D3_C_MGdb89_bbmap.bam rpkm=Aug_M1_C1_D3_C_MG89_bbmap.pileup.rpkm.txt 32bit=t
pileup.sh in=Aug_M1_C1_D5_C_MGdb89_bbmap.bam rpkm=Aug_M1_C1_D5_C_MG89_bbmap.pileup.rpkm.txt 32bit=t

#notes: with FPKM from UCdenver and JGI, the correlation gives similar trends but not great
# RSEM and bbmap gives much more similar trends compared with using the same mapping on different dataset (JGI&Denver)
# effects from different seq center>>than different bioinformatic pipeline

```
