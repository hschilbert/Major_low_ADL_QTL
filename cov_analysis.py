__usage__ = """
					python cov_analysis.py
					--cov <COVERAGE_FILE>
					--fig <OUTPUT_FIGURE_FILE>
					--chr <CHROMOSOME_OF_INTEREST>
					--start <START_POSITION>
					--end <END_POSITION>
					"""

import os, sys
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import matplotlib.patches as mpatches

# -- end of import --- #


def load_coverage( cov_file, chromosome ):
	"""! @brief load coverage from given file """
	
	with open( cov_file, "r" ) as f:
		line = f.readline()
		cov = []
		while line:
			parts = line.strip().split('\t')
			if parts[0] == chromosome:
				cov.append( float( parts[2] ) )
			line = f.readline()
	return cov


def construct_figure( ref_cov_values, sample_cov_values, figfile ):
	"""! @brief generate coverage figure """
	
	x_values = []
	y_values = []
	y2_values = []
	for i in range( 30 ):
		x_values.append( i )
		y_values.append( ref_cov_values.count( float( i ) )  )
		y2_values.append( sample_cov_values.count( float( i ) ) )
	
	fig, ax = plt.subplots()
	
	ax.plot( x_values, y_values, linestyle="--", marker="o", color="grey", label="whole chromosome" )
	ax2 = ax.twinx()
	ax2.plot( x_values, y2_values, linestyle="--", marker="o", color="green", label="region of interest" )
	
	ax.set_xlabel( "coverage per position" )
	ax.set_ylabel( "number of positions (reference)" )
	ax2.set_ylabel( "number of positions (sample)" )
	
	my_legend = [ 	mpatches.Patch(color='grey', label='whole chromosome'),
								mpatches.Patch(color='green', label='region of interest')
							]
	
	ax.legend( handles=my_legend )
	
	plt.subplots_adjust( left= 0.2, right=0.8 )
	
	fig.savefig( figfile, dpi=300 )


def main( arguments ):
	"""! @brief run everything """

	cov_file = arguments[ arguments.index('--cov')+1 ]
	cov_fig_file = arguments[ arguments.index('--fig')+1 ]

	chromosome = arguments[ arguments.index('--chr')+1 ]
	start = int( arguments[ arguments.index('--start')+1 ] )
	end = int( arguments[ arguments.index('--end')+1 ] )


	cov = load_coverage( cov_file, chromosome )
	construct_figure( cov, cov[ start:end ], cov_fig_file )

	print "average (mean): " + str( np.mean( cov ) )
	print "average (median): " + str( np.median( cov ) )
	print "average (mode): " + str( stats.mode( cov ) )
	

	print "average (mean): " + str( np.mean( cov[ start:end ] ) )
	print "average (median): " + str( np.median( cov[ start:end ] ) )
	print "average (mode): " + str( stats.mode( cov[ start:end ] ) )


if '--cov' in sys.argv and '--fig' in sys.argv and '--chr' in sys.argv and '--start' in sys.argv and '--end' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
