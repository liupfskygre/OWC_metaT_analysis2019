## this is a markdown file for the the RNAseq data of Liu and Lu, 2018, Fron. in Micro

## overview
1.

2. 

3.

4. BWA mapping reads and HTseq counts reads number

5. DESeq2 analysis and FPKM calculation


```

```


## reference 
**part1**
```
https://github.com/EnvGen/metagenomics-workshop
#metagenomics-workshop/in-house/tpm_table.py / 
prokkagff2gtf.sh ~/mg-workshop/results/annotation/functional_annotation/prokka/$SAMPLE/PROKKA_${date}.gff > $SAMPLE.map.gtf
htseq-count -r pos -t CDS -f bam $SAMPLE.map.markdup.bam $SAMPLE.map.gtf > $SAMPLE.count
cut -f4,5,9 $SAMPLE.map.gtf | sed 's/gene_id //g' | gawk '{print $3,$2-$1+1}' | tr ' ' '\t' > $SAMPLE.genelengths
tpm_table.py -n $SAMPLE -c $SAMPLE.count -i <(echo -e "$SAMPLE\t100") -l $SAMPLE.genelengths > $SAMPLE.tpm
```
