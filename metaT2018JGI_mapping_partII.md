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

#53

```

## quality summary of JGI data
```
grep 'Output' *filtered-report.txt > OWC_metaT2018_JGI_partI_summary.txt

#note, this is all rRNA filtered Pair-End data, with vary 2.6Giga bases to 21.2Gb; should be great;
```

## reference preparation (done in part I)
```
mapping to references; keep bam file
owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
#https://github.com/liupfskygre/OWC_metaT_analysis2019/blob/master/metaT2018_Denver_to_MGdb89.md

mkdir OWC_metaT2018_to_MG89
grep -c '>' OWC_methanogens_DB89_cat.fna
#23049

cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89
#rsem-prepare-reference ../OWC_methanogens_DB89_cat.fna --bowtie2 OWC_methanogens_DB89_cat
(done)
```

##to owc deRep 89 Methanogens MAGs (==>transcripts recruit to genomes)
```
# reads: cd /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII
ls -1 *.filter-MTF.fastq.gz > /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partII_list.txt

sed -i -e 's/\.filter-MTF\.fastq\.gz//g' metaT2018JGI_reads_partII_list.txt

cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89

screen -r OWC_MG89_RSEM

for sample in $(cat metaT2018JGI_reads_partII_list.txt) 
do
echo ${sample}
reformat.sh in=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_trimmed.fa out1=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R1_trimmed.fa out2=/home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R2_trimmed.fa

rsem-calculate-expression --bowtie2 --no-qualities -p 12 --paired-end /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R1_trimmed.fa /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R2_trimmed.fa OWC_methanogens_DB89_cat ${sample}_MG89_RSEM &>${sample}_MG89_RSEM.log
done 
```

## DRAM annotated genes (==>gene/pathway expression)
```
#wkdir
cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/Methanogens_cleanDB_26Spet2019_dRep/dereplicated_genomes/DRAM_MGdb89_25k_annotations
#grep -c '>' genes.fna; 141317
#grep -c 'grade' genes.fna; 141317
#sed -e 's/ grade.*$//g' genes.fna > MG89_DRAM_genes_hf.fna
#MG89_DRAM_genes_hf.fna

cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/Methanogens_cleanDB_26Spet2019_dRep/dereplicated_genomes/DRAM_MGdb89_25k_annotations/metaT2018JGI_to_MG89_DRAM_genes


#creat ref for bowtie2
#rsem-prepare-reference ../MG89_DRAM_genes_hf.fna --bowtie2 MG89_DRAM_genes_hf

screen -r MG89_DRAM_genes_hf
for sample in $(cat /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partII_list.txt) 
do
echo ${sample}
rsem-calculate-expression --bowtie2 --no-qualities -p 12 --paired-end /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R1_trimmed.fa /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R2_trimmed.fa MG89_DRAM_genes_hf ${sample}_gene_RSEM &>${sample}_genes_RSEM.log
done 
```

## to all dereplicated OWC mcrA (from contigs,==>transcripts to mcrA/methanogens )
#wkdir 
```
cd /home/projects/Wetlands/OWC_mcrA_from_assemblies
OWC_mcrA_all_clean_dedup_w_nt.faa
OWC_mcrA_all_clean_dedup.fna 
#987

#creat ref for bowtie2
#rsem-prepare-reference ../OWC_mcrA_all_clean_dedup.fna --bowtie2 OWC_mcrA_all_clean_dedup

cd /home/projects/Wetlands/OWC_mcrA_from_assemblies/metaT2018JGI_to_mcrA_all

screen -r OWC_mcrA_all_clean_dedup

for sample in $(cat /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partII_list.txt) 
do
echo ${sample}

rsem-calculate-expression --bowtie2 --no-qualities -p 12 --paired-end /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R1_trimmed.fa /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII/${sample}_R2_trimmed.fa OWC_mcrA_all_clean_dedup ${sample}_mcrA_RSEM &>${sample}_mcrA_RSEM.log
done 
```

## keep only R1 and R2, remove fq.gz and interleaved.fa,
```
#compress R1 and R2 to .gz file before rsem, rsem could take gz file

#Dec-20-2019, clean sever on partII data
cd /home/ORG-Data-2/metaT2018JGI_reads/metaT2018JGI_reads_partII 

cp /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partII_list.txt ./

rm *filter-MTF.fastq.gz

screen -r gzip
for sample in $(cat /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partII_list.txt) 
do
gzip ${sample}_R1_trimmed.fa
gzip ${sample}_R2_trimmed.fa
rm ${sample}_trimmed.fa
done
```

## JGI coverage summary 

**MG89**
#metaT2018JGI_reads_partI_II_list.txt, partI and partII (53 samples)

```
cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89

cat metaT2018JGI_reads_partI_list.txt metaT2018JGI_reads_partII_list.txt >metaT2018JGI_reads_partI_II_list53.txt

screen -S samtools_sorting
for sample in $(cat metaT2018JGI_reads_partI_II_list53.txt)
do 
echo "${sample}"
samtools sort -@ 12 "${sample}"_MG89_RSEM.transcript.bam > "${sample}"_MG89_RSEM.transcript.bam.sorted
done
#Aug_M1_C3_D3_MG89_RSEM.transcript.bam

jgi_summarize_bam_contig_depths --outputDepth MG89_I_II_depth53.txt *bam.sorted

#10^5

#fix the header and formate
.bam.sorted ==> //
contigName ==> MAGs.fa_Scaffold
.fa_==> \t
_MG89_RSEM.transcript ==> //

sed -e 's/\.bam\.sorted//g' MG89_I_II_depth53.txt > MG89_I_II_depth53_reformat.txt
sed -i -e 's/contigName/MAGs.fa_Scaffold/g' MG89_I_II_depth53_reformat.txt
sed -i -e 's/\.fa_/\t/g' MG89_I_II_depth53_reformat.txt
sed -i -e 's/_MG89_RSEM\.transcript//g' MG89_I_II_depth53_reformat.txt


```

**MCRA**
```
cd /home/projects/Wetlands/OWC_mcrA_from_assemblies/metaT2018JGI_to_mcrA_all
cp /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partI_II_list53.txt ./

screen -S samtools_sorting2
for sample in $(cat metaT2018JGI_reads_partI_II_list53.txt)
do 
echo "${sample}"
samtools sort -@ 12 "${sample}"_mcrA_RSEM.transcript.bam > "${sample}"_mcrA_RSEM.transcript.bam.sorted
done

jgi_summarize_bam_contig_depths --outputDepth MG89_mcrA_I_II_depth53.txt *bam.sorted

#10^3
```

**GENEs**
```
cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/Methanogens_cleanDB_26Spet2019_dRep/dereplicated_genomes/DRAM_MGdb89_25k_annotations/metaT2018JGI_to_MG89_DRAM_genes

cp /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/OWC_metaT2018_to_MG89/metaT2018JGI_reads_partI_II_list53.txt ./

screen -S samtools_sorting3
for sample in $(cat metaT2018JGI_reads_partI_II_list53.txt)
do 
echo "${sample}"
samtools sort -@ 12 "${sample}"_gene_RSEM.transcript.bam > "${sample}"_gene_RSEM.transcript.bam.sorted
done

#Aug_M1_C1_D1_A_gene_RSEM.transcript.bam
samtools sort -@ 12 Aug_M1_C1_D1_A_gene_RSEM.transcript.bam > Aug_M1_C1_D1_A_gene_RSEM.transcript.bam.sorted

jgi_summarize_bam_contig_depths --outputDepth MG89_genes_I_II_depth53.txt *bam.sorted

#10^4, ~ 1/10 of reads mapped to genome?
```

##
```
for file in cat (*_RSEM.genes.results
paste PS42_S_cout.out PS43_S_cout.out PS44_S_cout.out PS46_S_cout.out phz2_S_cout.out phz3_S_cout.out phz4_S_cout.out phz5_S_cout.out | awk -F "\t" '{print $1"\t"$2"\t"$4"\t"$6"\t"$8"\t"$10"\t"$12"\t"$14"\t"$16}' > PSI_htseqcounts.txt

```
