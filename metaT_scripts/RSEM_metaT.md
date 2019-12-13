## this shows how to use RSEM to pipeline to do mapping and reads counts 

**RSEM**
```
https://github.com/deweylab/RSEM


#start from mapping

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

summarize RSME data

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


#header of output
```
#*.genes.results
gene_id	transcript_id(s)	length	effective_length	expected_count	TPM	FPKM

```

**bowtie2 settings when using RSEM **

**This rate can be set by option '--bowtie2-mismatch-rate'??**

#/opt/bowtie2-2.3.5

```
https://github.com/deweylab/RSEM/blob/master/rsem-calculate-expression

default setting
my $bowtie2 = 0;
my $bowtie2_path = "";
my $bowtie2_mismatch_rate = 0.1;
my $bowtie2_k = 200;
my $bowtie2_sensitivity_level = "sensitive"; # must be one of "very_fast", "fast", "sensitive", "very_sensitive"


"bowtie2" => \$bowtie2,
	   "bowtie2-path=s" => \$bowtie2_path,
	   "bowtie2-mismatch-rate=f" => \$bowtie2_mismatch_rate,
	   "bowtie2-k=i" => \$bowtie2_k,
	   "bowtie2-sensitivity-level=s" => \$bowtie2_sensitivity_level,

#Use Bowtie 2 instead of Bowtie to align reads. Since currently RSEM does not handle indel, local and discordant alignments, the Bowtie2 parameters are set in a way to avoid those alignments. In particular, we use options '--sensitive --dpad 0 --gbar 99999999 --mp 1,1 --np 1 --score-min L,0,-0.1' by default. The last parameter of '--score-min', '-0.1', is the negative of maximum mismatch rate. This rate can be set by option '--bowtie2-mismatch-rate'. If reads are paired-end, we additionally use options '--no-mixed' and '--no-discordant'. (Default: off)


```
