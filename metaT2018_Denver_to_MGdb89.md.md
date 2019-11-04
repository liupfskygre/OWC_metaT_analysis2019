## a mark down to mapping reads of metaT2018, CU_Denver to MGdb89 

#Ref 

# https://github.com/liupfskygre/OWC_metaG16_ana2019/blob/master/metaT2014_mapping_db89.md

#
cd /home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver

#quality check
```
screen -S fastqc

fastqc *.gz
```

#quality trimming
```
sickle pe -c ${rawread_loc}/${sample_name}/Raw_Data/tmp_reads.fastq  -t sanger -m ${rawread_loc}/${sample_name}/Raw_Data/${sample_name}_interleaved_trimmed.fastq  -s ${rawread_loc}/sample_name/Raw_Data/${sample_name}_trimmed.singles.fastq

for file in *.gz 
do 
zcat ${file} > "${file%%.*}"tmp.fastq
done

#Aug-M1-C1-D1-C
#AugM1C1D1C
D_S44_L004_R1_001.fastq.gz
D_S44_L004_R2_001.fastq.gz
sickle pe -f D_S44_L004_R1_001 -r D_S44_L004_R2_001 -o AugM1C1D1C_R1_trimmerd.fastq -p AugM1C1D1C_R2_trimmerd.fastq -s AugM1C1D1C_trimmed.singles.fastq

#Aug-M1-C1-D3-C
AugM1C1D5C

E_S45_L004_R1_001.fastq.gz
E_S45_L004_R2_001.fastq.gz
sickle pe -f E_S45_L004_R1_001 -r E_S45_L004_R2_001 -o AugM1C1D3C_R1_trimmerd.fastq -p AugM1C1D3C_R2_trimmerd.fastq -s AugM1C1D3C_trimmed.singles.fastq

#Aug-M1-C1-D5-C
AugM1C1D5C
F_S46_L004_R1_001.fastq.gz
F_S46_L004_R2_001.fastq.gz

sickle pe -f F_S46_L004_R1_001 -r F_S46_L004_R2_001 -o AugM1C1D5C_R1_trimmerd.fastq -p AugM1C1D5C_R2_trimmerd.fastq -s AugM1C1D5C_trimmed.singles.fastq
```

#do mapping
#check /Users/pengfeiliu/A_Wrighton_lab/Computational_servers/summit_workspace_sh/run_bbmap_summit_MetaT2014_Methanogens_db.sh
```


```
