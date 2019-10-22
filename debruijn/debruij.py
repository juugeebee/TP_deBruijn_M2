#!/usr/bin/env python3

#python3 debruij.py -i ../data/eva71_two_reads.fq -k 21 -o __init__.py

import sys
import argparse
import networkx
import pytest

#Lecture du fastq
def read_fastq(fastq):
	with open (fastq,'r') as fillin:
		for line in lines:
			yield next(lines)
			next(lines)
			next(lines)

#Identification des k-mer unique
def cut_kmer (sequence, kmer_size):
	for i in range(len(sequence)-kmer_size):
		yield s[i:i+kmer_size]

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
	
def build_graph(kmer_dic):
#	add_edge(node1, node2, weight=2)
	pass

def get_starting_nodes():
    pass


def std():
    pass


def get_sink_nodes():
    pass


def path_average_weight():
    pass


def remove_paths():
    pass


def select_best_path():
    pass


def save_contigs():
    pass


def get_contigs():
    pass


def solve_bubble():
    pass


def simplify_bubbles():
    pass


def solve_entry_tips():
    pass


def solve_out_tips():
    pass

def main():

#Récupération des arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("-i", help="fichier fastq single end")
	parser.add_argument("-k", help="taille des kmer", default=21)
	parser.add_argument("-o", help= "fichier config")
	args = parser.parse_args()
	





if __name__ == "__main__":
	main()
	
	
