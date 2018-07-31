#using align.sh

novoalignRef=/home/pontikos/d/human_reference_sequence/human_g1k_v37.fasta.k15.s2.novoindex
ncores=35
memory2=20

code=CL100072051
f1=CL100072051_L2_B5GHUMskzRAAAAAAA_1.fq.gz
f2=CL100072051_L2_B5GHUMskzRAAAAAAA_2.fq.gz

# Aligns to b37 of human genome using novoalign and extracts discordant reads with samblaster
novoalign -c ${ncores} -o SAM "@RG\tID:${code}\tSM:${code}\tLB:${code}\tPL:BGI" --rOQ --hdrhd 3 -H -k -a -o Soft -t 320 -F STDFQ -f $f1 $f2 -d ${novoalignRef} | samblaster -e -d ${code}_disc.sam  | samtools view -Sb - > ${code}.bam

# Sorts and converts discordant read sam file to bam file
samtools view -Sb ${code}_disc.sam | novosort - -t . -c ${ncores} -m ${memory2}G -i -o ${code}_disc_sorted.bam

# Sorts the WGS bam
novosort -t . -c ${ncores} -m ${memory2}G -i -o ${code}_sorted_unique.bam ${code}.bam 
