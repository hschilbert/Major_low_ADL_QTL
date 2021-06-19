__usage__ = """
					assign_read_to_chr.py
					--read
					--refA
					--refC
					--out
					
					optional:
					--k <KMER_SIZE>
					"""

import sys, os
import matplotlib.pyplot as plt

# --- end of imports --- #


def load_sequences( fasta_file ):
	"""! @brief load candidate gene IDs from file """
	
	sequences = {}
	with open( fasta_file ) as f:
		header = f.readline()[1:].strip()
		seq = []
		line = f.readline()
		while line:
			if line[0] == '>':
					sequences.update( { header: "".join( seq ) } )
					header = line.strip()[1:]
					seq = []
			else:
				seq.append( line.strip() )
			line = f.readline()
		sequences.update( { header: "".join( seq ) } )	
	return sequences


def main( arguments ):
	"""! @brief match read k-mers to reference """
	
	input_read_file = arguments[ arguments.index('--read')+1 ]
	chrA_file = arguments[ arguments.index('--refA')+1 ]
	chrC_file = arguments[ arguments.index('--refC')+1 ]
	output_folder = arguments[ arguments.index('--out')+1 ]
	
	if '--k' in arguments:
		n = int( arguments[ arguments.index('--k')+1 ] )
	else:
		n = 15
	
	if output_folder[-1] != "/":
		output_folder += "/"
	
	if not os.path.exists( output_folder ):
		os.makedirs( output_folder )
	
	fig_file = output_folder + "read_unique_kmer_hist.pdf"
	unique_kmers_file = output_folder + "unique_kmers.fasta"

	read = load_sequences( input_read_file ).values()[0].upper()
	chrA = load_sequences( chrA_file ).values()[0].upper()
	chrC = load_sequences( chrC_file ).values()[0].upper()

	k_mers = [ read[i:i+n] for i in range(0, len(read), n) ]
	print len( k_mers )


	A = []
	C = []
	with open( unique_kmers_file, "w" ) as out:
		for i, k in enumerate( k_mers ):
			xa = chrA.find( k )
			xc = chrC.find( k )
			if xc > 0 and xa == -1:
				C.append( i*n )
				out.write( str( i*n ) + "\t" + k + '\t' + "C\n" )
			if xa > 0 and xc == -1:
				A.append( i*n )
				out.write( str( i*n ) + "\t" + k + '\t' + "A\n" )


	# --- generate figure --- #
	fig, ax = plt.subplots()

	ax.hist( A, bins=1000, color="green", alpha=0.5, label="A" )
	ax.hist( C, bins=1000, color="blue", alpha=0.5, label="C" )

	ax.set_ylabel( "number of unique k-mers" )
	ax.set_xlabel( "position in read [bp]" )

	ax.legend()
	ax.set_xlim( 0, len( read ) )

	fig.savefig( fig_file, dpi=300 )


if '--read' in sys.argv and '--refA' in sys.argv and '--refC' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
