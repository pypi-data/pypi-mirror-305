#!/usr/bin/env python
# -*- coding: utf-8 -*-

# !/usr/bin/env python
# -*- coding: utf-8 -*-
#
#

from Bio import PDB
import numpy as np

import multiprocessing
import warnings
from Bio import BiopythonWarning

warnings.simplefilter('ignore', BiopythonWarning)
import random, string, os
random.seed(42)

letters = {'CYS': 'C', 'ASP': 'D', 'SER': 'S', 'GLN': 'Q', 'LYS': 'K', 'ASN': 'N', 'PRO': 'P', 'THR': 'T', 'PHE': 'F',
           'ALA': 'A', 'H1S': 'H', 'H2S': 'H', 'HIS': 'H', 'GLY': 'G', 'ILE': 'I', 'LEU': 'L', 'ARG': 'R', 'TRP': 'W',
           'VAL': 'V', 'GLU': 'E', 'TYR': 'Y', 'MET': 'M'}

def predict_structure(seqSubstring, temSubstring,temSequence, templatePDB,outFile,tmp_folder="foldX_tmp/",foldx_bin="foldx"):

    if not os.path.isfile(foldx_bin):
        raise ValueError('foldx binary not found. download it from https://foldxsuite.crg.eu/. The folder containing foldX 4 binary should also contain Rotabase.txt')
    if not os.path.isfile("/".join(foldx_bin.split("/")[:-1])+"/rotabase.txt"):
        raise ValueError('rotabase.txt not found in the same folder of FoldX binary. Download foldX 4 from https://foldxsuite.crg.eu/, extract it and make sure rotabase is there')

    remaining_residues,chain_list,outTemplate = write_pdb_template(seqSubstring, temSubstring,temSequence, templatePDB,tmp_folder)

    assert len(seqSubstring) == len(remaining_residues)
    mut_list = []
    for ch in chain_list:
        for k,pos in enumerate(remaining_residues):
            if seqSubstring[k]!=temSubstring[k]:
                mut_list+=[temSubstring[k]+ch+str(pos)+seqSubstring[k]]

    energy = run_foldx(mut_list,outTemplate,tmp_folder,outFile=outFile,foldx_bin=foldx_bin)

    return energy

def parse_buildmodel_energy(fil):

    for l in open(fil, "r").readlines():
        a = l.split("\t")
        if ".pdb" in a[0]:
            name = a[0].replace(".pdb", "").split("_")[-1]
            if a[0].replace(".pdb", "").split("_")[0] == "WT":
                continue
            res = float(a[1])
    return res
def write_pdb_template(seqSubstring, temSubstring,temSequence, templatePDB,tmp_folder):

    if not os.path.exists(tmp_folder):
        os.system("mkdir "+ tmp_folder)

    outTemplate = tmp_folder +''.join(random.choice(string.ascii_lowercase) for i in range(5))+".pdb"

    begin = temSequence.index(temSubstring)
    end = begin + len(temSubstring)

    residue_to_remove = [i for i in range(len(temSequence)) if not (i >= begin and i < end)]
    remaining_residues, chain_list = remove_residues_by_sequence(templatePDB, residue_to_remove, outTemplate)

    remaining_residues = [remaining_residues[chain_list[0]][i][0] for i in range(len(remaining_residues[chain_list[0]]))]

    return remaining_residues,chain_list,outTemplate

def remove_residues_by_sequence(pdb_file, residue_indices, output_pdb_file):

    parser = PDB.PDBParser(QUIET=True)
    structure = parser.get_structure('structure', pdb_file)


    io = PDB.PDBIO()

    remaining_residues = {}
    chain_list = []

    class ResidueSelect(PDB.Select):
        def accept_residue(self, residue):
            # Get the parent chain
            chain = residue.get_parent()
            chain_id = chain.id

            if chain_id not in remaining_residues:
                remaining_residues[chain_id] = []

            sequence_index = list(chain).index(residue)

            pdb_residue_number = residue.id[1]
            insertion_code = residue.id[2]

            if sequence_index in residue_indices:
                return False

            remaining_residues[chain_id].append((pdb_residue_number, insertion_code))
            return True

    io.set_structure(structure)
    io.save(output_pdb_file, ResidueSelect())

    for model in structure:
        for chain in model:
            chain_list.append(chain.id)

    return remaining_residues, chain_list
def run_foldx(mut_list,outTemplate,tmp_folder,outFile,foldx_bin):
    FOLDX_FOLDER = "/".join(foldx_bin.split("/")[:-1])+"/"
    name = outTemplate.split("/")[-1].replace(".pdb","")

    if '/' in outTemplate:
        pdb_name = outTemplate.split('/')[-1]
        pdb_fold = '/'.join(outTemplate.split('/')[:-1])
    else:
        pdb_fold = "./"
        pdb_name = outTemplate

    if mut_list!=[]:
        individual_list = open(tmp_folder+'individual_list_' + name + '.tmp',"w")
        individual_list.write(",".join(mut_list)+";")
        individual_list.close()

        if not os.path.exists( tmp_folder + name):
            os.system("mkdir "+  tmp_folder + name)

        os.system(foldx_bin + ' --pdb-dir=' + pdb_fold + ' --rotabaseLocation=' + FOLDX_FOLDER + 'rotabase.txt --pdb=' + pdb_name.lower() + ' -c BuildModel --mutant-file=' + tmp_folder + 'individual_list_' + name + '.tmp --output-dir=' + tmp_folder + name +" > /dev/null")

        try:
            energy = parse_buildmodel_energy(tmp_folder + name+"/"+"Dif_"+name+".fxout")
        except:
            raise(ValueError,"FoldX failed to run. Check if it runs correctly")
        os.system("mv "+ tmp_folder + name+"/"+name+"_1.pdb"+" "+outFile)
        os.system('rm -r ' + tmp_folder + name)
        os.system("rm "+tmp_folder+'individual_list_' + name + '.tmp')
    else:
        energy=0.0
        os.system("cp " + pdb_fold+"/"+pdb_name.lower() + " " + outFile)
    return energy

