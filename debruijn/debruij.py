#!/usr/bin/env python3

#python3 debruij.py -i ../data/eva71_two_reads.fq -k 21 -o __init__.py

import sys
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
def cut_kmer (sequence, kmer_size):
	for i in range( len(sequence)- kmer_size + 1):
		yield sequence[i:i+kmer_size]

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
	for kmer, val in kmer_dic.items:
		G.add_edge(kmer[0:len(kmer)-1], kmer[1:len(kmer)], weight=val)
	return G

##### Parcours du graphe de de Bruijn #####

def get_starting_nodes(G):
	starting_nodes = []
	for node in G.nodes:
		if len(list(G.predecessor(node))) == FALSE:
			starting_nodes.append(node)
	return starting_nodes

def get_sink_nodes(G):
    sink_nodes = []
    for node in G.nodes:
		if len(list(G.successor(node))) == FALSE:
			sink_nodes.append(node)
	return sink_nodes

def get_contigs():
    pass

def save_contigs():
    pass

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
	kmer_dic = build_kmer_dict (args.i, args.k)
	G = build_graph(kmer_dic)
	starting_nodes = get_starting_nodes(G)
	sink_nodes = get_sink_nodes(G)

	
	


if __name__ == "__main__":
	main()
	
	
