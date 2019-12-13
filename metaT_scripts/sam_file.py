#!/usr/bin/python

#PYTHON SCRIPT 
#written by: Richard Wolfe
#
#to run type: python sam_file_analize_reads.py -i <inputfile> 
#         or: ./ongest_sequence.py -i <inputfile> 
#
#   if error: /usr/bin/python^M: bad interpreter: No such file or directory
#      -there is a windows endl after shebang
#      -open in vi 
#         once in vi type:
#           :set ff=unix<return>
#           :x<return>
#
#
#
# goes through the sam file and analyze how the reads mapped
# 
#
#   -i <sam file> (required) file to extract sequences from
#   -p --pull_mapped prefix for _1.fastq and _2.fastq files of reads that both reads mapped 
#         
#   stats are printed to the screen


import sys      #for exit command and maxint
import argparse #to get command line args 
                #needed to install argparse module because using python 2.6
                #and argparse comes with python 2.7
                #  sudo easy_install argparse
#import glob     #for * in file name
import toolbox


def test_method():
	#This method just changes the flag to no alignment if the number of 
	#  mismatches > args.max_mismatch
	#
	# Note: reads are not r1,r1,multi map
	# they are r1, multi r1,r2, multi r2

	print "max mismatch = ",args.max_mismatch
	print "output file = ",args.output.name

	#sys.exit(0)

	args.output = open(args.output.name, "w")

	input_lines = 0
	header_lines = 0
	data_lines = 0
	read_groups = 0

	alignments = 0
	non_alignments = 0	
	second_alignments = 0

	output_lines = 0

	xm_value_not_found = 0
	too_many_mismatches = 0
	discard_second_alignments = 0

	#read first line 
	line = args.input.readline()

	while line:
		#input_lines += 1

		

		#if input_lines % 100000 == 0 or (input_lines - 1) % 100000 == 0:
		#	print "Reading line ",input_lines

		if line.startswith( '@' ): #it is a header
       			header_lines += 1
			input_lines += 1
			args.output.write(line)
			output_lines += 1
			line = args.input.readline()
			continue

		#this is a read
		#r1 = line.rstrip()
		#r2 = args.input.readline().rstrip()
		#input_lines += 1
		mult_reads = []

		mult_reads.append(line)

		line = args.input.readline()
		while line:
			if line.split("\t")[0] != mult_reads[0].split("\t")[0]:
				#print "Not the same id"
				break
			else:
				#this is same read id
				mult_reads.append(line)
				line = args.input.readline()

		if len(mult_reads) == 1:
			print "Error ... only 1 read"
			sys.exit(1)

		data_lines = data_lines + len(mult_reads)
		input_lines = input_lines + len(mult_reads)
		read_groups += 1

		#remove endline and count multiassigns
		i = 0
		while i < len(mult_reads):
			mult_reads[i] = mult_reads[i].rstrip()
			flags = int(mult_reads[i].split("\t")[1])
			if flags & 256: #This read has a second alignment
				second_alignments += 1
			i += 1

		#see if multi_reads[0] is always mate1
		flags = int(mult_reads[0].split("\t")[1])
		if not flags & 64: #if read is not the first segment
			print "read is not marked as first read"
			print mult_reads[0]
			sys.exit(1)
		if flags & 256: #if marked as secondary align
			print "First read is marked as secondary alignment"
			print mult_reads[0]
			sys.exit(1)
		
		
		#process the reads in this set
		#if len(mult_reads) > 0:
		#	read_groups += 1
		#	print r1
		#	print r2
		#	for item in mult_reads:
		#		print item
		#
		#	sys.exit(0)

		
		

		"""
		else: #this is a read
			data_lines += 1
		
			line = line.rstrip()

			cols1 = line.split("\t")  #split on tabs
			
			flags1 = int(cols1[1])

			#see if  aligns
			if not flags1 & 4: #this read aligns
				alignments += 1
				
				if flags1 & 256: #This read has a second alignment
					second_alignments += 1

				#check the number of mismatches this read has
				#print line
				#sys.exit(0)
				#fields 12+ have the extra
				c = 11
				while not cols1[c].startswith("XM:i:"):
				#while not cols1[c].startswith("NM:i:"):
					c += 1
					if c >= len(cols1): #XM:i: value not found 
						xm_value_not_found += 1
						print line
						print "Error ... xm value not found"
						sys.exit(1)
						#break

				
				#cols1[c] will be the number of mismatches in alignment
				#parse the number of mismatches 
				mm = int(cols1[c].split(":")[2])
				#print line
				#print mm

				if mm > args.max_mismatch:
					#This alignment has more mismatches and needs edited
					too_many_mismatches += 1

					#if this is a scecondary alignment then discard the read and dont write to file
					if flags1 & 256: #This read has a second alignment
						discard_second_alignments += 1
						line = args.input.readline()
						continue
						

					new_flag = flags1 ^ 4 #changes only the 4 bit to its compliment
					cols1[1] = str(new_flag)
					#print line
					#print "orig flag = ",flags1
					#print "new flag = ",new_flag
					#sys.exit(0)

					#print the first 11 columns with new flag
					i = 0
					while i < 10:
						args.output.write(cols1[i] + "\t")
						i += 1
					args.output.write(cols1[10] + "\n")
					output_lines += 1
					#sys.exit(0)

				else:
					args.output.write(line + "\n")
					output_lines += 1
				
				
				

			else:	#This read does not align
				non_alignments += 1
				
				args.output.write(line + "\n")
				output_lines += 1

			

		#read next line
		line = args.input.readline()
		"""

		#sys.exit(0)


	
	#print analysis to screen
	print "Lines read from sam file = ", input_lines
	print "Number of header lines = ", header_lines
	print "Number of data lines = ", data_lines
	print " "
	
	print "Number of alignments = ",alignments
	print "number of non alignments = ", non_alignments
	print "number of secondary alignments = ",second_alignments
	print ""
	reads_aligned = alignments - second_alignments
	print "The number of reads that aligned, (alignments - second_alignments) = ",reads_aligned
	print ""
	print "The number of reads that aligned and no XM value = ",xm_value_not_found
	print ""
	print "Number of lines wrote to output file = ",output_lines
	print ""
	print "Number of reads with too many mismatches = ",too_many_mismatches
	print ""
	print "Number of secondary alignments discarded = ",discard_second_alignments
	print ""
	print "Number of read groups = ",read_groups

	print ""
	print "Script finished..."
	
	sys.exit(0)

def make_mismatch_table():
	#make a mismatch table for all sam files in this directory

	
	#make a list of all the .sam files in this folder
	sam_files = []
	mismatches = []
	counts = [] #this will be a list of lists for each sam file

	line = args.sam_list.readline()
	while line:
		line = line.rstrip()
		sam_files.append(line)

		line = args.sam_list.readline()

	for item in sam_files:
		print item
		
		#count the mismatches in this file
		cmd = "python /ORG-Data/scripts/sam_file.py -i " + item + " -c T"
		toolbox.run_system(cmd)

		#results will be in the file args.input.name + _mismatches.txt
		f = open(item + "_mismatches.txt", "rU")

		temp = []
		for i in mismatches:
			temp.append("0")

		line = f.readline()
		while line:
			line = line.rstrip()
			
			if line.split()[0] in mismatches: #if XM:i:11 in list
				index = mismatches.index(line.split()[0])
				temp[index] = line.split()[1]
			else:
				mismatches.append(line.split()[0])
				for i in counts:
					i.append("0")

				temp.append(line.split()[1])
			
			line = f.readline()
		
		counts.append(temp)
		f.close()

		#sys.exit(0)

	#print table to output file
	args.make_mismatch_table.write("mismatches")
	for i in sam_files:
		args.make_mismatch_table.write("\t" + i)
	args.make_mismatch_table.write("\n")

	i = 0
	while i < len(mismatches):
		args.make_mismatch_table.write(mismatches[i])
		for item in counts:
			args.make_mismatch_table.write("\t" + item[i])
		args.make_mismatch_table.write("\n")

		i += 1


	print ""
	print "Number of sam file in this directory = ", len(sam_files)
	print ""
	print "Script finished..."
	
	sys.exit(0)

def mult_alignment():
	#there are multiple alignments for the reads
	#the reads are not read 1 then read 2 in the sam file
	#There can be an odd number of read entries in the sam file

	input_lines = 0
	header_lines = 0
	data_lines = 0
	
	alignments = 0
	non_alignments = 0	
	second_alignments = 0

	#read first line 
	line = args.input.readline()

	#if the file is not empty keep reading one at a time
	while line:
		input_lines += 1
		if input_lines % 100000 == 0 or (input_lines - 1) % 100000 == 0:
			print "Reading line ",input_lines

		if line.startswith( '@' ):
       			header_lines += 1

		else: #this is a data line
			#print line
			data_lines += 1

			cols1 = line.split()
			
			flags1 = int(cols1[1])
			
			#see if  aligns
			if not flags1 & 4:
				alignments += 1
			else:
				non_alignments += 1

			if flags1 & 256:
				second_alignments += 1

		line = args.input.readline()	

	#close the file
	args.input.close()


	#print analysis to screen
	print "Lines read from sam file = ", input_lines
	print "Number of header lines = ", header_lines
	print "Number of data lines = ", data_lines
	print " "
	
	print "Number of alignments = ",alignments
	print "number of non alignments = ", non_alignments
	print "number of secondary alignments = ",second_alignments
	print ""
	reads_aligned = alignments - second_alignments
	print "The number of reads that aligned, (alignments - second_alignments) = ",reads_aligned
	print ""
	print "Script finished..."
	
	sys.exit(0)




def count_mismatches():

	input_lines = 0
	header_lines = 0
	data_lines = 0
	
	alignments = 0
	non_alignments = 0	
	second_alignments = 0

	xm_value_not_found = 0

	mismatches = []
	qty = []

	prefixes = []
	prefix_qty = [] #will be a list of qty for each prefix
	if args.prefixes:
		prefixes = args.prefixes.split(",")
	for item in prefixes:
		temp = []
		prefix_qty.append(temp)

	#read first line 
	line = args.input.readline()

	#if the file is not empty keep reading one at a time
	while line:
		input_lines += 1
		if input_lines % 100000 == 0 or (input_lines - 1) % 100000 == 0:
			print "Reading line ",input_lines

		if line.startswith( '@' ):
       			header_lines += 1

		else: #this is a data line
			#print line
			data_lines += 1

			line = line.rstrip() #remove endline
			cols1 = line.split("\t")  #split on tabs
			
			flags1 = int(cols1[1])
			
			#see if  aligns
			if not flags1 & 4: #this read aligns
				alignments += 1
				
				if flags1 & 256: #This read has a second alignment
					second_alignments += 1

				#check the number of mismatches this read has
				#print line
				#sys.exit(0)
				#fields 12+ have the extra
				c = 11
				while not cols1[c].startswith("XM:i:"):
					c += 1
					if c >= len(cols1): #XM:i: value not found 
						xm_value_not_found += 1
						break

				if c >= len(cols1): #XM:i: value not found
					line = args.input.readline()
					continue  #get next read
				
				#cols1[c] will be the number of mismatches in alignment
				if cols1[c] in mismatches:
					index = mismatches.index(cols1[c])
					qty[index] += 1
			
					#if we have prefixes then we need to increment the prefix qty
					if len(prefixes) > 0:
						scaff = cols1[2]
						pre_index = -1
						i = 0
 						while i < len(prefixes):
							if scaff.startswith(prefixes[i]):
								pre_index = i
        						i += 1
						if i == -1:
							print "Error ... prefix not found " + scaff
							sys.exit(1)

						prefix_qty[pre_index][index] += 1
							
						

				else:
					mismatches.append(cols1[c])
					qty.append(1)

					#if we have prefixes then we need to add to the prefix qty
					if len(prefixes) > 0:
						scaff = cols1[2]
						pre_index = -1
						i = 0
 						while i < len(prefixes):
							if scaff.startswith(prefixes[i]):
								pre_index = i
								prefix_qty[i].append(1)
							else:
								prefix_qty[i].append(0)
        						i += 1
						if i == -1:
							print "Error ... prefix not found " + scaff
							sys.exit(1)				
				
				

			else:	#This read does not align
				non_alignments += 1

			

		line = args.input.readline()	

	#close the file
	args.input.close()

	#put into numerical order
	#find highest value all are XM:i:0 .... XM:i:23 ...
	highest = 0
	i = 0
	while i < len(mismatches):
		val = int(mismatches[i].split(":")[-1])
		if val > highest:
			highest = val
		i += 1

	#make a new array of the mismatch values
	
	new_mismatches = []
	new_qty = []
	new_prefix_qty = [] #will be a list of qty for each prefix
	for item in prefixes:
		temp = []
		new_prefix_qty.append(temp)

	i = 0
	while i <= highest:
		new_mismatches.append(i)
		new_qty.append(0)
		j = 0
		while j < len(prefixes):
			new_prefix_qty[j].append(0)
			j += 1
		i += 1

	#transfer the quantities into new array
	i = 0
	while i < len(mismatches):
		val = int(mismatches[i].split(":")[-1]) 
		new_qty[val] = qty[i]
		j = 0
		while j < len(prefixes):
			new_prefix_qty[j][val] = prefix_qty[j][i]
			j += 1
		i += 1

	#print the mismatches to an output file
	f = open(args.input.name + "_mismatches.txt","w")
	i = 0
	tot_reads = 0
	tot_prefixes = []
	for item in prefixes:
		tot_prefixes.append(0)

	f.write("Reads_mapped\tTotal")
	for item in prefixes:
		f.write("\t" + item)
	f.write("\n")

	while i < len(new_mismatches):
		if args.total_reads == "F":
			f.write(str(new_mismatches[i]) + "_mismatches\t" + str(new_qty[i]))# + "\n")
			for item in new_prefix_qty:
				f.write("\t" + str(item[i]))
			f.write("\n")
			
		else: #if args.total_reads != "T":
			tot_reads = tot_reads + new_qty[i]
			f.write(str(new_mismatches[i]) + "_mismatches_or_less\t" + str(tot_reads) ) #+ "\n")
			j = 0
			while j < len(prefixes):
				tot_prefixes[j] = tot_prefixes[j] + new_prefix_qty[j][i]
				f.write("\t" + str(tot_prefixes[j]))
				j += 1
			f.write("\n")
			
		i += 1


	#print analysis to screen
	print "Lines read from sam file = ", input_lines
	print "Number of header lines = ", header_lines
	print "Number of data lines = ", data_lines
	print " "
	
	print "Number of alignments = ",alignments
	print "number of non alignments = ", non_alignments
	print "number of secondary alignments = ",second_alignments
	print ""
	reads_aligned = alignments - second_alignments
	print "The number of reads that aligned, (alignments - second_alignments) = ",reads_aligned
	print ""
	print "The number of reads that aligned and no XM value = ",xm_value_not_found
	print ""
	
	print ""
	print "Script finished..."

	sys.exit(0)

def count_mismatches_bt1():

	input_lines = 0
	header_lines = 0
	data_lines = 0
	
	alignments = 0
	non_alignments = 0	
	second_alignments = 0

	xm_value_not_found = 0
	

	

	#read first line 
	line = args.input.readline()

	#if the file is not empty keep reading one at a time
	while line:
		input_lines += 1
		if input_lines % 100000 == 0 or (input_lines - 1) % 100000 == 0:
			print "Reading line ",input_lines

		if line.startswith( '@' ):
       			header_lines += 1

		else: #this is a data line
			#print line
			data_lines += 1

			line = line.rstrip() #remove endline
			cols1 = line.split("\t")  #split on tabs
			
			flags1 = int(cols1[1])
			
			#see if  aligns
			if not flags1 & 4: #this read aligns
				alignments += 1
				
				if flags1 & 256: #This read has a second alignment
					second_alignments += 1

				#check the number of mismatches this read has
				#print line
				#sys.exit(0)
				#fields 12+ have the extra
				c = 11
				#while not cols1[c].startswith("XM:i:"):
				while not cols1[c].startswith("NM:i:"):
					c += 1
					if c >= len(cols1): #XM:i: value not found 
						xm_value_not_found += 1
						break

				if c >= len(cols1): #XM:i: value not found
					line = args.input.readline()
					continue  #get next read
				
				#cols1[c] will be the number of mismatches in alignment
				if cols1[c] in mismatches:
					index = mismatches.index(cols1[c])
					qty[index] += 1

				else:
					mismatches.append(cols1[c])
					qty.append(1)
				
				

			else:	#This read does not align
				non_alignments += 1

			

		line = args.input.readline()	

	#close the file
	args.input.close()

	#print the mismatches to an output file
	f = open("mismatches.txt","w")
	i = 0
	while i < len(mismatches):
		f.write(mismatches[i] + "\t" + str(qty[i]) + "\n")

		i += 1


	#print analysis to screen
	print "Lines read from sam file = ", input_lines
	print "Number of header lines = ", header_lines
	print "Number of data lines = ", data_lines
	print " "
	
	print "Number of alignments = ",alignments
	print "number of non alignments = ", non_alignments
	print "number of secondary alignments = ",second_alignments
	print ""
	reads_aligned = alignments - second_alignments
	print "The number of reads that aligned, (alignments - second_alignments) = ",reads_aligned
	print ""
	print "The number of reads that aligned and no XM value = ",xm_value_not_found
	print ""
	
	
	print ""
	print "Script finished..."

	sys.exit(0)


def max_mismatch():
	#This method just changes the flag to no alignment if the number of 
	#  mismatches > args.max_mismatch

	print "max mismatch = ",args.max_mismatch
	print "output file = ",args.output.name

	#sys.exit(0)

	if not args.percent_read == None: #because int  
		print "percent_read variable is included"
 		#sys.exit(0)

	args.output = open(args.output.name, "w")

	input_lines = 0
	header_lines = 0
	data_lines = 0

	alignments = 0
	non_alignments = 0	
	second_alignments = 0

	output_lines = 0

	xm_value_not_found = 0
	too_many_mismatches = 0
	discard_second_alignments = 0

	#read first line 
	line = args.input.readline()

	while line:
		input_lines += 1

		if input_lines % 100000 == 0 or (input_lines - 1) % 100000 == 0:
			print "Reading line ",input_lines

		if line.startswith( '@' ): #it is a heade
       			header_lines += 1
			args.output.write(line)
			output_lines += 1
			line = args.input.readline()
			continue

		else: #this is a read
			data_lines += 1
		
			line = line.rstrip()

			cols1 = line.split("\t")  #split on tabs
			
			flags1 = int(cols1[1])

			#see if  aligns
			if not flags1 & 4: #this read aligns
				alignments += 1
				
				if flags1 & 256: #This read has a second alignment
					second_alignments += 1

				#check the number of mismatches this read has
				#print line
				#sys.exit(0)
				#fields 12+ have the extra
				c = 11
				while not cols1[c].startswith("XM:i:"):
				#while not cols1[c].startswith("NM:i:"):
					c += 1
					if c >= len(cols1): #XM:i: value not found 
						xm_value_not_found += 1
						print line
						print "Error ... xm value not found"
						sys.exit(1)
						#break

				
				#cols1[c] will be the number of mismatches in alignment
				#parse the number of mismatches 
				mm = int(cols1[c].split(":")[2])
				#print line
				#print mm
				
				#if we are changing on mismatches
				if args.percent_read == None: #because int
					if mm > args.max_mismatch:
						#This alignment has more mismatches and needs edited
						too_many_mismatches += 1

						#if this is a scecondary alignment then discard the read and dont write to file
						if flags1 & 256: #This read has a second alignment
							discard_second_alignments += 1
							line = args.input.readline()
							continue
						

						new_flag = flags1 ^ 4 #changes only the 4 bit to its compliment
						cols1[1] = str(new_flag)
						#print line
						#print "orig flag = ",flags1
						#print "new flag = ",new_flag
						#sys.exit(0)

						#print the first 11 columns with new flag
						i = 0
						while i < 10:
							args.output.write(cols1[i] + "\t")
							i += 1
						args.output.write(cols1[10] + "\n")
						output_lines += 1
						#sys.exit(0)

					else:
						args.output.write(line + "\n")
						output_lines += 1

				else: #we are using percent reads to change
					# mm = number of mismatches
					#  args.percent_read = 90 --percent if under this then we mark as not mapped
					#  length_read - number_mismatches / length_read = pct_read_mismatches
					pcent = (args.percent_read * 1.0) / 100.0
					read_len = len(cols1[9])
					calc = ((read_len - mm) * 1.0) / (read_len * 1.0)
					if calc < pcent: #we change to not mapped
						#This alignment has more mismatches and needs edited
						too_many_mismatches += 1

						#if this is a scecondary alignment then discard the read and dont write to file
						if flags1 & 256: #This read has a second alignment
							discard_second_alignments += 1
							line = args.input.readline()
							continue
						

						new_flag = flags1 ^ 4 #changes only the 4 bit to its compliment
						cols1[1] = str(new_flag)
						#print line
						#print "orig flag = ",flags1
						#print "new flag = ",new_flag
						#sys.exit(0)

						#print the first 11 columns with new flag
						i = 0
						while i < 10:
							args.output.write(cols1[i] + "\t")
							i += 1
						args.output.write(cols1[10] + "\n")
						output_lines += 1
						#sys.exit(0)
					else:
						args.output.write(line + "\n")
						output_lines += 1	

			else:	#This read does not align
				non_alignments += 1
				
				args.output.write(line + "\n")
				output_lines += 1

			

		#read next line
		line = args.input.readline()

		#sys.exit(0)


	
	#print analysis to screen
	print "Lines read from sam file = ", input_lines
	print "Number of header lines = ", header_lines
	print "Number of data lines = ", data_lines
	print " "
	
	print "Number of alignments = ",alignments
	print "number of non alignments = ", non_alignments
	print "number of secondary alignments = ",second_alignments
	print ""
	reads_aligned = alignments - second_alignments
	print "The number of reads that aligned, (alignments - second_alignments) = ",reads_aligned
	print ""
	print "The number of reads that aligned and no XM value = ",xm_value_not_found
	print ""
	print "Number of lines wrote to output file = ",output_lines
	print ""
	print "Number of reads with too many mismatches = ",too_many_mismatches
	print ""
	print "Number of secondary alignments discarded = ",discard_second_alignments

	print ""
	print "Script finished..."

	sys.exit(0)



#create an argument parser object
#description will be printed when help is used
parser = argparse.ArgumentParser(description='A script to analyze how the reads mapped')

#add the available arguments -h and --help are aqdded by default
#if the input file does not exist then program will exit
#if output file does not exit it will be created
# args.input is the input file Note: cant write to this file because read only
# args.output is the output file
# args.m is the minimum seq length
parser.add_argument('-i', '--input', type=argparse.FileType('rU'), help='Input file name')#required=True
parser.add_argument('-o', '--output', type=argparse.FileType('w'), help='Output file name')
parser.add_argument('-p', '--pull_mapped', help='prefix for _1.fastq and _2.fastq files of reads that both reads mapped')
parser.add_argument('-m', '--mult_align', help='T or F if sam file is multiple alignment',default="F")
parser.add_argument('-c', '--count_mismatches', help='T or F count mismatches',default="F")
parser.add_argument('-b', '--count_mismatches_bt1', help='T or F count mismatches in bowtie1 file',default="F")
parser.add_argument('-v', '--max_mismatch', type=int, help='max number of mismatches')
parser.add_argument('--make_mismatch_table',type=argparse.FileType('w'), help='make mismatch table for all sam files in list')
parser.add_argument('--sam_list',type=argparse.FileType('rU'), help='list of sam files to make a table')
parser.add_argument('--test', help='to run test method')
parser.add_argument('--total_reads', help='T or F total reads with mismatches less than ',default="F")
parser.add_argument('--prefixes', help='a comma seperated list of prefixes') #only used in count_mismatches

parser.add_argument('--percent_read', type=int, help='percent of (read_length - mismatches)/read_length to keep EX: 90')  #optional should use -m 5000


#get the args
args = parser.parse_args()

if args.total_reads != "T":
	if args.total_reads != "F":
		print "Error ... --total_reads must be T or F"
		sys.exit(1)

if args.prefixes:
	print args.prefixes
else:
	print "No prefixes"
#sys.exit()

if args.test:
	test_method()



if args.make_mismatch_table:
	if args.sam_list:
		make_mismatch_table()
	else:
		print "Error ... You must supply a sam file list --sam_list"
		sys.exit(1)
else:
	#if not making a table then make sure input file is required
	if args.input == None:
		print "Error ... -i is required"
		sys.exit(1)

if not args.max_mismatch == None: #because it is an int 


	if args.max_mismatch < 0:
		print "Error ... -v must be greater than 0"
		sys.exit(1)
	else:
		try:
			args.output.close()
		except:
			#if cant open the files because no arg
			print "Error ... you must specify an output file -o"
			sys.exit(1)

		max_mismatch()

print "No args max_mismatch"
#sys.exit(0)

if args.mult_align != "T":
	if args.mult_align != "F":
		print "Error ... -m must be T or F"
		sys.exit(1)

if args.count_mismatches != "T":
	if args.count_mismatches != "F":
		print "Error ... -c must be T or F"
		sys.exit(1)

if args.count_mismatches_bt1 != "T":
	if args.count_mismatches_bt1 != "F":
		print "Error ... -c must be T or F"
		sys.exit(1)

if args.count_mismatches_bt1 == "T" and args.count_mismatches == "T":
	print "Error ... -c and -b cant both = T"
	sys.exit(1)


#if args.pull_mapped then we want to open 2 output files
try:
	r1_out = open(args.pull_mapped + "_1.fastq", "w")
	r2_out = open(args.pull_mapped + "_2.fastq", "w")
except:
	#if cant open the files because no arg
	print "No output files will be made"



#Test print the args
#print args

input_lines = 0
output_lines = 0
header_lines = 0
data_lines = 0

r1_lines = 0
r2_lines = 0

paired_reads = 0

both_align = 0
at_least_one_align = 0
neither_align = 0

first_read_maps = 0
second_read_maps = 0 

first_not_first = 0
second_not_second = 0

first_reversed = 0
second_reversed = 0

proper_align = 0
first_proper_align = 0
second_proper_align = 0



if args.mult_align == "T":
	mult_alignment()

if args.count_mismatches == "T":
	count_mismatches()

if args.count_mismatches_bt1 == "T":
	count_mismatches_bt1()

#read first line 
line = args.input.readline()

#if the file is not empty keep reading one at a time
while line:

	input_lines += 1
	if input_lines % 100000 == 0 or (input_lines - 1) % 100000 == 0:
		print "Reading line ",input_lines

	if line.startswith( '@' ):
       		header_lines += 1

	else: #this is a data line
		#print line
		data_lines += 1

		#this is paired data so make sure next line is read
		line2 = args.input.readline()
		input_lines += 1
		data_lines += 1

		if line2.startswith( '@' ):
			print "Error .. line starts with @ and should be a read line"
			print line
			sys.exit(1)

		cols1 = line.split()
		cols2 = line2.split()

		flags1 = int(cols1[1])
		flags2 = int(cols2[1])

		#make sure paired read flag is set in both lines
		if not flags1 & 1 or not flags2 & 1:  #if paired bit not set
			print "Error ... read is not part of a pair"
			sys.exit(1)
		paired_reads += 1

		#see if both pairs align
		if not flags1 & 4 and not flags2 & 4:
			both_align += 2

			#if both reads map and args.pull_mapped then write these sequences to the output files
		     	if args.pull_mapped:
				seq1 = ""
				qual1 = ""
				seq2 = ""
				qual2 = ""
				head1 = ""
				head2 = ""
				#see if in order mate1 and mate2
				if flags1 & 64: #if line is mate 1
					if flags1 & 16: #if to reverse
						seq1 = toolbox.reverse_compliment(cols1[9])
						qual1 = cols1[10][::-1] #trick to reverse the string
					else:
						seq1 = cols1[9]
						qual1 = cols1[10]
					if flags2 & 16: #if to reverse
						seq2 = toolbox.reverse_compliment(cols2[9])
						qual2 = cols2[10][::-1] #trick to reverse the string
					else:
						seq2 = cols2[9]
						qual2 = cols2[10]
					head1 = cols1[0] + "/1"
					head2 = cols2[0] + "/2"
	
				else: #lines not in order
					if flags2 & 16: #if to reverse
						seq1 = toolbox.reverse_compliment(cols2[9])
						qual1 = cols2[10][::-1] #trick to reverse the string
					else:
						seq1 = cols2[9]
						qual1 = cols2[10]
					if flags1 & 16: #if to reverse
						seq2 = toolbox.reverse_compliment(cols1[9])
						qual2 = cols1[10][::-1] #trick to reverse the string
					else:
						seq2 = cols1[9]
						qual2 = cols1[10]
					head1 = cols2[0] + "/1"
					head2 = cols1[0] + "/2"

				#print the reads to the output files
				r1_out.write("@" + head1 + "\n")
				r1_out.write(seq1 + "\n")
				r1_out.write("+" + "\n")
				r1_out.write(qual1 + "\n")
				r2_out.write("@" + head2 + "\n")
				r2_out.write(seq2 + "\n")
				r2_out.write("+" + "\n")
				r2_out.write(qual2 + "\n")
				r1_lines += 4
				r2_lines += 4

		if not flags1 & 4 or not flags2 & 4: #if seq1 aligns or seq2 aligns
			at_least_one_align += 2
		

		if flags1 & 4 and flags2 & 4:
			neither_align += 2

		if not flags1 & 4:
			first_read_maps += 1

		if not flags2 & 4:
			second_read_maps += 1

		#check if these reads are in order line = mate1 and line2 = mate2
		if not flags1 & 64:
			first_not_first += 1

		if not flags2 & 128:
			second_not_second += 1
			#print line
			#print line2
			#sys.exit(0)

		#check if read is reversed
		if flags1 & 16:
			first_reversed += 1
		if flags2 & 16:
			second_reversed += 1

		#check if read is a proper alignment
		if not flags1 & 4 and flags1 & 2:
			proper_align +=1
		if  not flags2 & 4 and flags2 & 2:
			proper_align +=1
 		if flags1 & 2:
			first_proper_align += 1
		if flags2 & 2:
			second_proper_align += 1

		
			

	line = args.input.readline()	

#close the file
args.input.close()






#print analysis to screen
print "Lines read from sam file = ", input_lines
print "Number of header lines = ", header_lines
print "Number of data lines = ", data_lines
print " "
print "Number of paired reads = ", paired_reads
print ""
print "Number of reads where both reads align = ",both_align
print "Number of reads at least one read aligns = ", at_least_one_align
print "Number of reads neither align = ", neither_align
print "Number of first reads that map = ", first_read_maps
print "Number of second reads that map = ", second_read_maps
print ""
print "Number of first reads not mate 1 = ", first_not_first
print "Number of second reads not mate 2 = ", second_not_second
print ""
print "Number of first reads reversed = ", first_reversed
print "Number of second reads reversed = ", second_reversed
print ""
print "Number of reads with a proper alignment = ", proper_align
print "Number of first reads with proper alignment = ", first_proper_align
print "Number of second reads with proper alignment = ", second_proper_align
print ""
print "Number of lines wrote to _1.fastq = ",r1_lines
print "Number of lines wrote to _2.fastq = ",r2_lines

print "Script finished..."
sys.exit(0)



