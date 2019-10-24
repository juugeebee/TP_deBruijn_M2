#!/usr/bin/env python3

#pytest --cov=debruijn
#pylint debruijn.py

import sys
import os
import argparse
import networkx as nx

##### Parcours du graphe de de Bruijn #####

	### Identification des k-mer unique ###

#Lecture du fastq
def read_fastq(fastq):
	fq = open (fastq,'r')
	for line in fq:
		yield next(fq).strip()
		next(fq)
		next(fq)

#Identification des k-mer unique
def cut_kmer(seq, kmer_size):
    for i in range(len(seq)-kmer_size+1):
        yield seq[i:i+kmer_size]

#Création d'un dictionnaire de k-mer
def build_kmer_dict (fastq, kmer_size):
	kmer_dic = {}
	for i in read_fastq(fastq):
		for kmer in cut_kmer(i, kmer_size):
			if not kmer in kmer_dic:
				kmer_dic[kmer] = 1
			else:
				kmer_dic[kmer] += 1
	return kmer_dic


	### Construction de l’arbre de de Bruijn ###
def build_graph(kmer_dic):
	G = nx.DiGraph()	
	for kmer, val in kmer_dic.items():
		G.add_edge(kmer[0:len(kmer)-1], kmer[1:len(kmer)], weight=val)
	return G

##### Parcours du graphe de de Bruijn #####

	### get_starting_nodes prend en entrée un graphe et retourne une liste de noeuds
d’entrée
def get_starting_nodes(G):
	starting_nodes = []
	for node in G.nodes:
		if len(list(G.predecessors(node))) == 0:
			starting_nodes.append(node)
	return starting_nodes

	### get_sink_nodes​ prend en entrée un graphe et retourne une liste de noeuds de sortie
def get_sink_nodes(G):
	sink_nodes = []
	for node in G.nodes:
		if len(list(G.successors(node))) == 0:
			sink_nodes.append(node)
	return sink_nodes

	### get_contigs prend un graphe, une liste de noeuds d’entrée et une liste de sortie et retourne une liste de tuple
def get_contigs(network_graph,input_graph_network, output_graph_network):
    """
    Méthode qui retourne une liste de tuple (contig, taille du contig)
    """
    contigs = []
    for noeud_depart in input_graph_network:
        for noeud_fin in output_graph_network:
            for path in nx.all_simple_paths(network_graph, source = noeud_depart, target = noeud_fin):
                prep_contig = path
                contig_ecrit = []
                contig_ecrit.append(prep_contig[0])
                for i in range(1, len(prep_contig)):
                    contig_ecrit.append(prep_contig[i][-1:])
                contig_ecrit = "".join(contig_ecrit)
                contigs.append((contig_ecrit, len(contig_ecrit)))
    return contigs

	### formatage	
def fill(text, width=80):
    """Split text with a line return to respect fasta format"""
    return (os.linesep.join(text[i:i+width] for i in range(0, len(text), width)))	
    
    
	### save_contigs prend un tuple, un nom de fichier de sortie et écrit un fichier de sortie contenant les contigs selon le format:
def save_contigs(contigs_tupple, fillout):
	file = open("../data/"+fillout,'w+')
	for i in range(len(contigs_tupple)):
		file.write('>Contig numero ' + str(i) + ' len=' + str(contigs_tupple[i][1]) + '\n' + str(fill(contigs_tupple[i][0])) + '\n')
        

##### Simplification du graphe de de Bruijn #####

	### Résolution des bulles ###
	
def std():
    pass	

def path_average_weight():
    pass

def remove_paths():
    pass

def select_best_path():
    pass

def solve_bubble():
    pass

def simplify_bubbles():
    pass

	### Détection des pointes (tips) ###

def solve_entry_tips():
    pass

def solve_out_tips():
    pass



##### MAIN #####
def main():

#Récupération des arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", help="fichier fastq single end")
	parser.add_argument("-k", help="taille des kmer", default=21)
	parser.add_argument("-o", help= "fichier config")
	args = parser.parse_args()

#Lancement des fonctions	
	
	kmer_dic = build_kmer_dict (args.i, int(args.k))
	G = build_graph (kmer_dic)
	starting_nodes = get_starting_nodes(G)
	sink_nodes = get_sink_nodes(G)
	contigs_tuple = get_contigs(G, starting_nodes, sink_nodes)
	save_contigs(contigs_tuple, 'exit.txt')
	
	
if __name__ == "__main__":
	main()
	
	
