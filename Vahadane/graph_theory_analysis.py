import json
import pandas as pd
import os
import networkx as nx
import numpy as np
from scipy.spatial import distance_matrix
import matplotlib.pyplot as plt
from statistics import mean
from numpy import linalg
import pandas as pd
import argparse



def create_graph(df, max_nn_dist=102.4):
	df_pos = df[df['label'] == 1]
	df_coord = pd.DataFrame(df_pos, columns=['x', 'y'])
	dist_matrix = distance_matrix(df_coord.values, df_coord.values)
	weighted_adj_matrix = np.zeros((dist_matrix.shape[0], dist_matrix.shape[1]))
	for i_cell in range(dist_matrix.shape[0]):
	    c_cell = dist_matrix[i_cell,:]
	    index_sort = np.where(c_cell<max_nn_dist)[0].tolist() #np.argsort(c_cell)
	    index_sort.remove(i_cell)
	    if len(index_sort)> 0:
	        for ind in index_sort:
	            weighted_adj_matrix[i_cell,ind] = dist_matrix[i_cell,ind]
	G = nx.from_numpy_array(weighted_adj_matrix)
	return G

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Graph theory - compute global and local features on KI67 detected cells')
    parser.add_argument('--rootdir', type=str, '/home/mathiane/LNENWork/PathonetCombinedDataSet2/PredBreastLNENDataset2Epoch50', default=  help="rootdir where are the TNEXXXX_cells.csv")
    parser.add_argument('--sample', type=str,    help='Sample currently under analysis')
    args = parser.parse_args()

    folder_name = args['sample']
	sample_name = folder_name.split('.')[0]
	root = args['rootdir']
	# Read df of detected cells
	df = pd.read_csv(f'{root}/{folder_name}/{sample_name}_cells.csv')

	for max_nn_dist in [102.4, 51.2, 150.6]:
		# 102.4 = 50 micron
		# 51.2 = 25 micron 
		# 150.6 = 75_micron
		# maxnn in micron
		if max_nn_dist == 102.4:
			max_nn_micron = '50_micron'
		elif  max_nn_dist == 51.2:
			max_nn_micron = '25_micron'
		else :
			max_nn_micron = '75_micron'
		G = create_graph(df, max_nn_dist=max_nn_dist)
		# Global feature
		global_features = {}
		global_features['nb_nodes'] = G.number_of_nodes() # Number of nodes
		global_features['nb_edges'] = G.number_of_edges() # Number of edges
		global_features['poucent_unconnected_nodes'] =  (len(list(nx.isolates(G))) / 
		                                G.number_of_nodes()) *100 # Pourcentage of unconnected nodes
		degrees = dict(nx.degree(G))
		global_features['poucent_end_nodes'] = (len([n for n in degrees if degrees[n]  ==  1]) /
		 G.number_of_nodes()) *100 # Pourcentage of end nodes
		global_features['size_largest_cc'] = len(max(nx.connected_components(G), 
		                                             key=len)) # Size of the largest connected component
		CG = nx.connected_components(G)
		global_features['avg_size_cc_norm_nb_nodes'] =  mean([len(g) for g in CG])/ G.number_of_nodes() # Connected components average siz normalized by the number of nodes
		global_features['global_efficiency'] =  nx.global_efficiency(G)
		json_global_feature_fname = f'{root}/{folder_name}/{sample_name}_graph_{max_nn_micron}_global_features.json'
		with open(json_global_feature_fname, 'w+') as f:
		    json.dump(global_features, f)
		# Local Features
		xdict = {}
		ydict = {}
		for i in range(df_coord.shape[0]):
		    xdict[i] = df_coord.iloc[i,0]
		    ydict[i] = df_coord.iloc[i,1]
		nx.set_node_attributes(G, xdict, "x_coord")
		nx.set_node_attributes(G, ydict, "y_coord")

		degrees = dict(nx.degree(G))
		closeness_centrality =  dict(nx.closeness_centrality(G))
		weighted_closeness_centrality = dict(nx.closeness_centrality(G, distance='weight'))
		weighted_betweenness_centrality =  dict(nx.betweenness_centrality(G,weight= 'weight'))
		pagerank_centrality = dict(nx.pagerank(G, weight= 'weight'))
		eigenvector_centrality = dict(nx.eigenvector_centrality(G))
		clustering_coeff = dict(nx.clustering(G))
		weighted_clustering_coeff = dict(nx.clustering(G, weight='weight'))

		# Df of local features
		local_feature = pd.DataFrame()
		local_feature['x_coord'] = list(xdict.values())
		local_feature['y_coord'] = list(ydict.values())
		local_feature['degrees'] = list(degrees.values())
		local_feature['closeness_centrality'] = list(closeness_centrality.values())
		local_feature['weighted_closeness_centrality'] = list(weighted_closeness_centrality.values())
		local_feature['weighted_betweenness_centrality'] = list(weighted_betweenness_centrality.values())
		local_feature['pagerank_centrality']  = list(pagerank_centrality.values())
		local_feature['eigenvector_centrality'] = list(eigenvector_centrality.values())
		local_feature['clustering_coeff'] = list(clustering_coeff.values())
		local_feature['weighted_clustering_coeff'] = list(weighted_clustering_coeff.values())

		csv_local_feature_fname = f'{root}/{folder_name}/{sample_name}_graph_{max_nn_micron}_local_features.csv'
		local_feature.to_csv(csv_local_feature_fname,index=False)