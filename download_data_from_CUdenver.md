#CU-denver
```
1) 'cd' to the destination directory on zenith where you want the files
2) Type:  sftp rdaly173@140.226.123.30
3) enter password  # "c9u!r-BOP"
You will now get a prompt that looks like this:
    sftp>
4) 'ls' to see directories available - you should have been given directory names by Ted
5) 'cd' into the directory with the files you want
6) use the 'get' command to copy the files you want  
    i.e. get [file name or names]
    
7) when finished type 'bye' to exit the sftp session

```

#
```
#/ORG-Data is full
#use here
cd /home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver
screen -S transfer
get *.gz

#move data from Salmonella to here
/home/ORG-Data-2/metaT_CU_denver2019/Salmonella_CU_denver_metaT2019
A, B, C, and Daly_
#

```

# redo rename; 
```
#path: /home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT2018_CU_Denver

#Aug_M1_C1_D1_C
#D_S44_L004_R1_001.fastq.gz
#D_S44_L004_R2_001.fastq.gz
mv D_S44_L004_R1_001.fastq.gz Aug_M1_C1_D1_C_D_S44_L004_R1_001.fastq.gz
mv D_S44_L004_R2_001.fastq.gz Aug_M1_C1_D1_C_D_S44_L004_R2_001.fastq.gz

#Aug_M1_C1_D3_C
#E_S45_L004_R1_001.fastq.gz
#E_S45_L004_R2_001.fastq.gz
mv E_S45_L004_R1_001.fastq.gz Aug_M1_C1_D3_C_E_S45_L004_R1_001.fastq.gz
mv E_S45_L004_R2_001.fastq.gz Aug_M1_C1_D3_C_E_S45_L004_R2_001.fastq.gz


#Aug_M1_C1_D5_C
#F_S46_L004_R1_001.fastq.gz
#F_S46_L004_R2_001.fastq.gz
mv F_S46_L004_R1_001.fastq.gz Aug_M1_C1_D5_C_F_S46_L004_R1_001.fastq.gz
mv F_S46_L004_R2_001.fastq.gz Aug_M1_C1_D5_C_F_S46_L004_R2_001.fastq.gz
```



## another two redos
```
#downloaded and renamed by Adrienne
/home/ORG-Data-2/metaT_CU_denver2019/OWC_metaT_2018_redos_16Mar2020

-rw-rw-r--. 1 anarrowe orgdata2 4.3K Mar 16 09:02 200305_A00405_0215_AH55K3DSXY_Daly_demux.csv
-rw-rw-r--. 1 anarrowe orgdata2  12G Mar 16 09:11 Aug_M1_C2_D5_DALY16_S63_L002_R1_001.fastq.gz
-rw-rw-r--. 1 anarrowe orgdata2  12G Mar 16 09:14 Aug_M1_C2_D5_DALY16_S63_L002_R2_001.fastq.gz
-rw-rw-r--. 1 anarrowe orgdata2  92M Apr 28 18:27 Aug_M1_C2_D5_SR.fa.gz
-rw-rw-r--. 1 anarrowe orgdata2 9.6G Apr 28 18:27 Aug_M1_C2_D5_trimmed.R1.fa.gz
-rw-rw-r--. 1 anarrowe orgdata2 9.7G Apr 28 18:27 Aug_M1_C2_D5_trimmed.R2.fa.gz
-rw-rw-r--. 1 anarrowe orgdata2 9.5G Mar 16 09:06 Aug_OW2_C1_D5_A_DALY15_S62_L002_R1_001.fastq.gz
-rw-rw-r--. 1 anarrowe orgdata2  11G Mar 16 09:08 Aug_OW2_C1_D5_A_DALY15_S62_L002_R2_001.fastq.gz
-rw-rw-r--. 1 anarrowe orgdata2  61M Apr 28 21:11 Aug_OW2_C1_D5_A_SR.fa.gz
-rw-rw-r--. 1 anarrowe orgdata2 7.4G Apr 28 21:11 Aug_OW2_C1_D5_A_trimmed.R1.fa.gz
-rw-rw-r--. 1 anarrowe orgdata2 7.1G Apr 28 21:11 Aug_OW2_C1_D5_A_trimmed.R2.fa.gz
-rw-rw-r--. 1 anarrowe orgdata2  215 Apr 28 14:33 fileslist
-rwxrw-r--. 1 anarrowe orgdata2  466 Apr 28 14:38 run_sickle.sh
-rw-rw-r--. 1 anarrowe orgdata2 4.3K Apr 28 14:37 slurm-3751.out
-rw-rw-r--. 1 anarrowe orgdata2  440 Apr 28 18:27 slurm-3752.out

fastqc Aug_M1_C2_D5_DALY16_S63_L002_R1_001.fastq.gz
fastqc Aug_M1_C2_D5_DALY16_S63_L002_R2_001.fastq.gz

fastqc Aug_OW2_C1_D5_A_DALY15_S62_L002_R1_001.fastq.gz
fastqc Aug_OW2_C1_D5_A_DALY15_S62_L002_R2_001.fastq.gz
```
