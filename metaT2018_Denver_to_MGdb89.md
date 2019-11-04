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
bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=AugM1C1D1C_R1_trimmerd.fastq in2=AugM1C1D1C_R2_trimmerd.fastq ambiguous=random outm=AugM1C1D1C_metaT2018_CUD_MGdb89.bam t=24 -Xmx112g

bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=AugM1C1D3C_R1_trimmerd.fastq in2=AugM1C1D3C_R2_trimmerd.fastq ambiguous=random outm=AugM1C1D3C_metaT2018_CUD_MGdb89.bam t=24 -Xmx112g

bbmap.sh ref=../OWC_methanogens_DB89_cat.fna in=AugM1C1D5C_R1_trimmerd.fastq in2=AugM1C1D5C_R2_trimmerd.fastq ambiguous=random outm=AugM1C1D5C_metaT2018_CUD_MGdb89.bam t=24 -Xmx112g

#

```
