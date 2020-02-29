## calculate the TPM for transcripts mapping to MAGs, 

#TPM for MAGs, from cov ==> reads#==> TPM of MAGs
```
MG89_I_II_depth53.txt

#https://github.com/liupfskygre/OWC_metaT_analysis2019/blob/master/metaT2014_mapping_db89.md
#metaT_mapping_OWC2018megahit_mcrA.Rmd
#https://github.com/liupfskygre/OWC_metaG16_ana2019/blob/master/MG_db_relative_abundance.md
#metaT2014_MGdb89_TMP.Rmd
#ReAb_OWC_methanogens_db88.Rmd
```


#TPM for genes 
```
#paste all/merge all _RSEM.genes.results files

Aug_N3_C1_D5_A_MG89_RSEM.genes.results 

for file in $(cat metaT2018JGI_reads_partI_II_list53.txt)
do 
#sed -i -e "s/TPM/TPM_$file/g" ${file}_MG89_RSEM.genes.results 
echo "${file}"
paste "${file}"_MG89_RSEM.genes.results tmp.txt>tmp.txt
done
paste *_MG89_RSEM.genes.results >tmp.txt

paste PS42_S_cout.out PS43_S_cout.out PS44_S_cout.out PS46_S_cout.out phz2_S_cout.out phz3_S_cout.out phz4_S_cout.out phz5_S_cout.out | awk -F "\t" '{print $1"\t"$2"\t"$4"\t"$6"\t"$8"\t"$10"\t"$12"\t"$14"\t"$16}' > PSI_htseqcounts.txt

```
