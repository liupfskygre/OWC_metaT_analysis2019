#!/usr/bin/env python2.7

#from /home/projects/NIH_methylamines/Huttenhower2018_MetaT
# quick_transcriptome_script.py forward_reads reverse_reads map_to mismatches threads output

import argparse
import subprocess
from os import path, mkdir


def main(forward_reads, reverse_reads, map_to, mismatches, threads=20, output='.'):
    if not path.exists(output):
        mkdir(output)
    # step 1 align reads
    sam_loc = path.join(output, 'aligned_reads.sam')
    subprocess.check_output(['bowtie2', '-D', '10', '-R', '2', '-N', '1', '-L', '22', '-i', 'S,0,2.50', '-a', '-p', str(threads),
                    '-x', map_to, '-1', forward_reads, '-2', reverse_reads, '-S', sam_loc], stderr=subprocess.STDOUT)
    # step 2 filter alignment for n number of mismatches
    filtered_sam_loc = path.join(output, 'aligned_reads.mm%s.sam' % mismatches)
    subprocess.check_output(['python2', '/ORG-Data/scripts/sam_file.py', '-i', sam_loc, '-v', str(mismatches), '-o', filtered_sam_loc])
    # step 3 convert sam to bam and sort
    sorted_bam_loc = path.join(output, 'aligned_reads.mm%s.sorted.bam' % mismatches)
    subprocess.check_output(['samtools', 'sort', '-@', str(threads), '-T', 'intermediate_file.bam', '-o', sorted_bam_loc, filtered_sam_loc])
    # step 4 cufflinks
    cufflinks_results_loc = path.join(output, 'cufflinks_results')
    subprocess.check_output(['/home2/opt/Cufflinks/cufflinks-2.2.1.Linux_x86_64/cufflinks', '-u', '-o', cufflinks_results_loc, sorted_bam_loc])


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--forward_reads', help='forward reads')
    parser.add_argument('--reverse_reads', help='reverse reads')
    parser.add_argument('--map_to', help='fasta file to be mapped to')
    parser.add_argument('--mismatches', type=int, default=5, help='mismatches to allow')
    parser.add_argument('--threads', type=int, default=20, help='number of threads')
    parser.add_argument('--output', help='Name of output dir', default='.')


    args = parser.parse_args()
    main(args.forward_reads, args.reverse_reads, args.map_to, args.mismatches, args.threads, args.output)
