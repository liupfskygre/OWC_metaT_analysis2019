## metaT2014 mapping to the methanogens db 89

#2019-OCt-2, Pengfei

#update 2019-Oct-04 DB89
```
#/scratch/summit/liupf@colostate.edu/raw_metaT2014_OWC


sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Mud_11_14_A.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Mud_11_14_B.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Mud_11_14_C.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Mud_9_15_A.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Mud_9_15_B.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Mud_9_15_C.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Plant_11_14_A.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Plant_11_14_B.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh PlantDeep_9_15_C.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Plant_11_14_C.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Plant_9_15_A.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Plant_9_15_B.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh Plant_9_15_C.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh PlantDeep_9_15_A.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh PlantDeep_9_15_B.L20.Q20

sbatch /projects/liupf@colostate.edu/workspace/run_bbmap_summit_MetaT2014_Methanogens_db.sh PlantDeep_9_15_C.L20.Q20

```

#tem
```
all done

```

#update OCT-7-2019, db88 to db 89
#transfer data to zenith, do summary
```
cd /home/projects/Wetlands/2018_sampling/Methanog_targeted_coassembly/Methanogens_final_dRep_clean_db/metaT2014_mapping_MGdb88

for file in *.sam
do
samtools view -S -b -@ 8 ${file} > "${file%.*}".bam
samtools sort -@ 8 "${file%.*}".bam > "${file%.*}".sorted.bam
done

#
screen -S metaT_mapping_MGdb88_depth
jgi_summarize_bam_contig_depths --outputDepth metaT_mapping_MGdb89_depth.txt *.sorted.bam

#use cut and R extract data we need

rm *.sam

mv *sorted.bam sorted_bam_backup/


```

#
```
cat metaT_mapping_MGdb89_depth.txt|cut -f1-4,6,8,10,12,14,16,18,20,22,24,26,28,30,32 -d$'\t' > metaT2014_MGdb89_depth_cut.txt

sed -i -e 's/\.L20\.Q20_metaT2014_MGdb89\.sorted\.bam//g' metaT2014_MGdb89_depth_cut.txt 
sed -i -e 's/contigName/MAGsName\.fa_contigName/g' metaT2014_MGdb89_depth_cut.txt 
sed -i -e 's/\.fa_/\t/g' metaT2014_MGdb89_depth_cut.txt 

#transfer data to MAc, using R to do cal

```

# pick the most active genomes and representative ones
```


```
