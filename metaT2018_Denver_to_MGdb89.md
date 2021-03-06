## a mark down to mapping reads of metaT2018, CU_Denver to MGdb89 

#Ref 

#https://github.com/liupfskygre/OWC_metaG16_ana2019/blob/master/metaT2014_mapping_db89.md
#https://github.com/liupfskygre/OWC_metaG16_ana2019/blob/master/MG_db_relative_abundance.md
#
cd /home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver

#quality check
```
screen -S fastqc

fastqc *.gz
```

#quality trimming
```
#path: /home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver

sickle pe -c ${rawread_loc}/${sample_name}/Raw_Data/tmp_reads.fastq  -t sanger -m ${rawread_loc}/${sample_name}/Raw_Data/${sample_name}_interleaved_trimmed.fastq  -s ${rawread_loc}/sample_name/Raw_Data/${sample_name}_trimmed.singles.fastq

for file in *.gz 
do 
zcat ${file} > "${file%%.*}"tmp.fastq
done

screen -S sickle

#Aug-M1-C1-D1-C
#AugM1C1D1C
#D_S44_L004_R1_001.fastq.gz
#D_S44_L004_R2_001.fastq.gz

sickle pe -f D_S44_L004_R1_001tmp.fastq -r D_S44_L004_R2_001tmp.fastq -o AugM1C1D1C_R1_trimmerd.fastq -p AugM1C1D1C_R2_trimmerd.fastq -s AugM1C1D1C_trimmed.singles.fastq -t sanger 
 
#Aug-M1-C1-D3-C
#AugM1C1D5C

#E_S45_L004_R1_001.fastq.gz
#E_S45_L004_R2_001.fastq.gz
sickle pe -f E_S45_L004_R1_001tmp.fastq -r E_S45_L004_R2_001tmp.fastq -o AugM1C1D3C_R1_trimmerd.fastq -p AugM1C1D3C_R2_trimmerd.fastq -s AugM1C1D3C_trimmed.singles.fastq -t sanger 

#Aug-M1-C1-D5-C
#AugM1C1D5C
#F_S46_L004_R1_001.fastq.gz
#F_S46_L004_R2_001.fastq.gz

sickle pe -f F_S46_L004_R1_001tmp.fastq -r F_S46_L004_R2_001tmp.fastq -o AugM1C1D5C_R1_trimmerd.fastq -p AugM1C1D5C_R2_trimmerd.fastq -s AugM1C1D5C_trimmed.singles.fastq -t sanger 


```

#do mapping
#check /Users/pengfeiliu/A_Wrighton_lab/Computational_servers/summit_workspace_sh/run_bbmap_summit_MetaT2014_Methanogens_db.sh
```
#
cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db
mkdir OWC_metaT2018_CU_Denver_to_MGdb89
screen -S OWC_metaT2018_CU_Denver_to_MGdb89
#ref
bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D1C_R1_trimmerd.fastq in2=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D1C_R2_trimmerd.fastq ambiguous=random outm=AugM1C1D1C_metaT2018_CUD_MGdb89.bam t=24 -Xmx112g

bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D3C_R1_trimmerd.fastq in2=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D3C_R2_trimmerd.fastq ambiguous=random outm=AugM1C1D3C_metaT2018_CUD_MGdb89.bam t=24 -Xmx112g

bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D5C_R1_trimmerd.fastq in2=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D5C_R2_trimmerd.fastq ambiguous=random outm=AugM1C1D5C_metaT2018_CUD_MGdb89.bam t=24 -Xmx112g

#

```

```
for file in *.bam
do
samtools sort -@ 8 ${file} > "${file%.*}".sorted.bam
done

#
jgi_summarize_bam_contig_depths --outputDepth metaT2018CUD_mapping_MGdb89_depth.txt *.sorted.bam


```

#
```
cat metaT2018CUD_mapping_MGdb89_depth.txt |cut -f1-4,6,8 -d$'\t' > metaT2018CUD_megahit_metaG16_depth_cut.txt

sed -i -e 's/\.sorted\.bam//g' metaT2018CUD_megahit_metaG16_depth_cut.txt

sed -i -e 's/_metaT2018_CUD_MGdb89//g' metaT2018CUD_megahit_metaG16_depth_cut.txt

sed -i -e 's/contigName/MAGsName\.fa_contigName/g' metaT2018CUD_megahit_metaG16_depth_cut.txt

sed -i -e 's/\.fa_/\t/g' metaT2018CUD_megahit_metaG16_depth_cut.txt 

```

**update 17-Dec-2019**
```
keep only fastq.gz
rm *.fastq
```

**FPKM using pileup.sh**
```
pileup.sh in=AugM1C1D1C_metaT2018_CUD_MGdb89.bam rpkm=AugM1C1D1C_metaT2018_CUD.pileup.rpkm.txt 32bit=t

pileup.sh in=AugM1C1D3C_metaT2018_CUD_MGdb89.bam rpkm=AugM1C1D3C_metaT2018_CUD.pileup.rpkm.txt 32bit=t

pileup.sh in=AugM1C1D5C_metaT2018_CUD_MGdb89.bam rpkm=AugM1C1D5C_metaT2018_CUD.pileup.rpkm.txt 32bit=t

#to compare with the data with from JGI

```
**RSEM**
#==>not do yet, trimmed reads removed
```
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

#/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D1C_R1_trimmerd.fastq in2=/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver/AugM1C1D1C_R2_trimmerd.fastq 
```



