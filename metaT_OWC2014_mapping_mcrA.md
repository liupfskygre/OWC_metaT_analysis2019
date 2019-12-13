#
#path on zenith: /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads
# Notes there on how the reads were generated.

**option 1, scripts used by Kayla, bowtie2 for mapping**
```
#/home/projects/NIH_methylamines/Huttenhower2018_MetaT/quick_transcriptome_script.py
#written by mike
```


**option2, bbmap to sam/bam and FPKM, also coverage**
```
#cd /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads

cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage/
#OWC2014_trimmed_transcript_reads.txt
sed -e 's/\.R1\.fq//g' OWC2014_trimmed_transcript_reads.txt>OWC2014_trimmed_transcript_reads_prefix.txt
sed -i -e 's/\.R2\.fq//g' OWC2014_trimmed_transcript_reads_prefix.txt
sed -i -e 's/\.SR\.fq//g' OWC2014_trimmed_transcript_reads_prefix.txt
cat OWC2014_trimmed_transcript_reads_prefix.txt|sort|uniq >OWC2014_trimmed_transcript_reads_prefix_uniq.txt

mkdir OWC2014_trimmed_transcript_mcrA

#do mapping

#cd /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads

screen -S OWC2014_trimmed_transcript_mcrA

cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage/OWC2014_trimmed_transcript_mcrA

for prefix in $(cat ../OWC2014_trimmed_transcript_reads_prefix_uniq.txt)
do
bbmap.sh ref=../OWC_seqs_id_2014_2018_mcrA_LA.fna in=/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R1.fq in2=/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R2.fq xmtag=t ambiguous=random outm=./${prefix}_mcrA.bam threads=20 -Xmx150g &>./${prefix}_mcrA.log
done

#outm only kept mapped reads, ok for TPM cal?

for file in *.bam
do
samtools sort -@ 8 ${file} > ${file}.sorted
done
screen -S mcrA_megahit_metaG16_depth
jgi_summarize_bam_contig_depths --outputDepth mcrA_metaT2014_mapping_depth.txt *.bam.sorted
```

**option 2A, bbmap to sam/bam and FPKM, also coverage**

#this includes all mcrA from all methanogens MAGs and OWC-2013-2018, megahit>600bp

```
#cd /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads

cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage/
#OWC2014_trimmed_transcript_reads.txt
sed -e 's/\.R1\.fq//g' OWC2014_trimmed_transcript_reads.txt>OWC2014_trimmed_transcript_reads_prefix.txt
sed -i -e 's/\.R2\.fq//g' OWC2014_trimmed_transcript_reads_prefix.txt
sed -i -e 's/\.SR\.fq//g' OWC2014_trimmed_transcript_reads_prefix.txt
cat OWC2014_trimmed_transcript_reads_prefix.txt|sort|uniq >OWC2014_trimmed_transcript_reads_prefix_uniq.txt

#prepare references
# move file from mac to zenith
# OWC_Archaea_AN_MAGs_2014_2015.mcrA_all.fna (25 sequences)
cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage
cat OWC_Archaea_AN_MAGs_2014_2015.mcrA_all.fna OWC_seqs_id_2014_2018_mcrA_LA.fna >OWC_seqs_id_2014_2018_mcrA_ALL7June19.fna

#578 seqs

##
mkdir OWC2014_trimmed_transcript_mcrA_ALL7June19

#do mapping

#cd /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads
cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage/OWC2014_trimmed_transcript_mcrA_ALL7June19

screen -S OWC2014_trimmed_transcript_mcrA_2A


for prefix in $(cat ../OWC2014_trimmed_transcript_reads_prefix_uniq.txt)
do
bbmap.sh ref=../OWC_seqs_id_2014_2018_mcrA_ALL7June19.fna in=/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R1.fq in2=/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R2.fq xmtag=t ambiguous=random outm=./${prefix}_mcrA_2A.bam threads=12 -Xmx150g &>./${prefix}_mcrA_2A.log
samtools sort -@ 8 ${prefix}_mcrA_2A.bam > ${prefix}_mcrA_2A.bam.sorted
done

#outm only kept mapped reads, ok for TPM cal?

jgi_summarize_bam_contig_depths --outputDepth mcrA_metaT2014_mapping_depth_2A.txt *.bam.sorted
```

**option 3, any mapp tools, RSEM tools to generate TPM valuse**

**not pass through yet, trouble with bam file from outside**

**better from the beginning**

#Ref: https://github.com/liupfskygre/RSEM_tutorial
#https://statquest.org/2015/07/09/rpkm-fpkm-and-tpm-clearly-explained/
#http://www.arrayserver.com/wiki/index.php?title=TPM

#This measure can be used directly as a value between zero and one or can be multiplied by 106 to obtain a measure in terms of transcripts per million (TPM). The transcript fraction measure is preferred over the popular RPKM [18] and FPKM [6] measures because it is independent of the mean expressed transcript length and is thus more comparable across samples and species [7]. (Li and Dewey et al., 2011)

#sam or bam files can from different aligners
```
cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage/OWC2014_trimmed_transcript_mcrA
#1, rsem-prepare-reference -h
rsem-prepare-reference ../OWC_seqs_id_2014_2018_mcrA_LA.fna  OWC_seqs_id_2014_2018_mcrA_LA
rsem-calculate-expression --num-threads 4 --alignments --paired-end Mud_11_14_A.L20.Q20_mcrA.bam  Mud_9_15_A.L20.Q20_mcrA.bam  Plant_11_14_A.L20.Q20_mcrA.bam  Plant_9_15_A.L20.Q20_mcrA.bam  PlantDeep_9_15_A.L20.Q20_mcrA.bam Mud_11_14_B.L20.Q20_mcrA.bam  Mud_9_15_B.L20.Q20_mcrA.bam  Plant_11_14_B.L20.Q20_mcrA.bam  Plant_9_15_B.L20.Q20_mcrA.bam  PlantDeep_9_15_B.L20.Q20_mcrA.bam Mud_11_14_C.L20.Q20_mcrA.bam  Mud_9_15_C.L20.Q20_mcrA.bam  Plant_11_14_C.L20.Q20_mcrA.bam  Plant_9_15_C.L20.Q20_mcrA.bam  PlantDeep_9_15_C.L20.Q20_mcrA.bam OWC_seqs_id_2014_2018_mcrA_LA mcrA

# rsem-sam-validator 
rsem-sam-validator PlantDeep_9_15_B.L20.Q20_mcrA.bam #validate
#invalid

#convert-sam-for-rsem, convert-sam-for-rsem input.sam input_for_rsem
for file in *.bam
do 
convert-sam-for-rsem "${file%.*}".bam "${file%.*}"_for_rsem
done
#bam from bbmap is not valid even after this coersion, better to start from mapping!
```

**RSEM**

#start from mapping
```
#prepare reference
cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage
mkdir OWC2014_trimmed_transcript_mcrA_ALL7June19_RSEM

../OWC_seqs_id_2014_2018_mcrA_ALL7June19.fna
rsem-prepare-reference ../OWC_seqs_id_2014_2018_mcrA_ALL7June19.fna --bowtie2 OWC_seqs_id_2014_2018_mcrA_ALL7June19
#--star 

screen -S OWC_seqs_id_2014_2018_mcrA_RSEM
for prefix in $(cat ../OWC2014_trimmed_transcript_reads_prefix_uniq.txt)
do

echo "/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R1.fq" 
echo "/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R2.fq"
rsem-calculate-expression --bowtie2 -p 14 --num-threads 12 --paired-end /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R1.fq /home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R2.fq OWC_seqs_id_2014_2018_mcrA_ALL7June19 ${prefix}_mcrA14_18_RSEM &>${prefix}_mcrA14_18_RSEM.log

for prefix in $(cat ../OWC2014_trimmed_transcript_reads_prefix_uniq.txt)
do
echo "/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R1.fq" 
echo "/home/projects/Wetlands/2014-2015_sampling/MetaT/sickled_transcript_reads/${prefix}.R2.fq"
done

```
**summarize RSME data**
```
cd /home/projects/Wetlands/2018_sampling/OWC_metaG_megahit/OWC_megahit_mcrA_coverage/OWC2014_trimmed_transcript_mcrA_ALL7June19_RSEM

for file in *.genes.results
do 
echo "${file%%.*}"
cut -f1,6-7 -d$'\t' $file > "${file%%.*}"_RSEM.txt
sed -i -e "s/TPM/${file%%.*}_TPM/g" "${file%%.*}"_RSEM.txt
sed -i -e "s/FPKM/${file%%.*}_FPKM/g" "${file%%.*}"_RSEM.txt
done
#Mud_11_14_A.L20.Q20_mcrA14_18_RSEM.genes.results

#copy all data to MAC "${file%%.*}"_RSEM.txt
#merge dataset in R

#multmerge function
setwd("~/A_Wrighton_lab/Wetland_project/OWC_metaG_2014_2018/metaT_mapping_OWC2018megahit_mcrA/RSEM_TPM_FPKM")

multmerge = function(mypath){
  filenames=list.files(path=mypath, full.names=TRUE)
  datalist = lapply(filenames, function(x){read.delim(file=x,header=T,check.names = FALSE)})
  Reduce(function(x,y) {merge(x,y,all = TRUE,by.x="gene_id", by.y="gene_id")}, datalist)
}

metaT2014_full_data = multmerge("~/A_Wrighton_lab/Wetland_project/OWC_metaG_2014_2018/metaT_mapping_OWC2018megahit_mcrA/RSEM_TPM_FPKM")


metaT2014_full_data_TPM <- metaT2014_full_data %>% select(gene_id,ends_with("TPM"))
metaT2014_full_data_FPKM <- metaT2014_full_data %>% select(gene_id,ends_with("FPKM"))
```



**manual calculation**
```
#average coverage, Rn, reads mapped to a gene, Rl, seqs reads length (150bp)
#AC=Rl(bp)*Rn/Gl(bp) -->Gl(kb)=Rl(bp)*Rn/(AC*1000)

#Divide the read counts by the length of each gene in kilobases. This gives you reads per kilobase (RPK).
#RPK = Rn/Gl(kp)-->Gl(kb)=Rn/RPK

#so, Rn/RPK=Rl(bp)*Rn/(AC*1000) -->RPK = AC*1000/Rl(bp)

AC is already known in the jgi summarize. 
```
