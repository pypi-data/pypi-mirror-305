import sys
import csv
import oddt
from oddt import fingerprints
import numpy as np
from oddt import interactions
import os,traceback
# from pymol import cmd


# def compose_protein_and_ligand(path_protein, path_ligand, path_output):
#     cmd.reinitialize()
#     cmd.load(path_protein, 'protein')
#     cmd.load(path_ligand, 'ligand')
#     cmd.create("complex", "protein or ligand" )
#     cmd.save(os.path.join(path_output , 'complex.pdb'), "complex")

def cal_ifp(path_protein, path_ligand, path_output , i):
    
    protein_name  = os.path.basename(path_protein)
    ligand_name =  os.path.basename(path_ligand)
    os.system('cp %s %s'%(path_ligand , path_output))
    os.rename(os.path.join(path_output , ligand_name) ,   os.path.join(path_output , 'top%s.sdf'%i) )
    
    if os.path.exists(path_ligand):
        try:
            protein = next(oddt.toolkit.readfile('pdb' , path_protein))
            protein.protein = True
            ligand = next(oddt.toolkit.readfile('sdf' , path_ligand))
            new0 = open(os.path.join(path_output , 'interaction.csv'), 'w', newline='')
            mycsv0 = csv.writer(new0)
            mycsv0.writerow(
                ['protein_name', 'ligand_name', 'type','res_name' ,'res_chain', 'res_idx_PDB', 'res_idx', 'atom_type1', 
                 'isacceptor', 'x', 'y', 'z', 'atom_type3', 'x2', 'y2', 'z2','strict/parallel','perpendicular']
            )

            # 氢键
            a, b ,strict = interactions.hbonds(protein,ligand)
            if a.__len__() != 0:
                new = open(os.path.join(path_output , 'hbond.csv'), 'w', newline='')
                mycsv = csv.writer(new)
                for i in range(len(a)):
                    # protein
                    atom = protein.atoms[a[i][0]]
                    residue = protein.residues[int(a[i][9])]
                    res_name = a[i][11]
                    res_idx = a[i][9]
                    res_idx_PDB = a[i][10]

                    res_chain = residue.chain
                    atom_type1 = a[i][5]

                    isacceptor = a[i][13]
                    x = a[i][1][0]
                    y = a[i][1][1]
                    z =a[i][1][2]

                    # ligand
                    atom_type3 = b[i][5]
                    x2 = b[i][1][0]
                    y2 = b[i][1][1]
                    z2 = b[i][1][2]

                    st = strict[i]

                    # 排除那部分与反应氨基酸形成的相互作用

                    mycsv.writerow(
                        [protein_name,ligand_name,'hbond',res_name,res_chain,res_idx_PDB,res_idx,atom_type1,isacceptor,x,y,z,atom_type3,x2,y2,z2,st]
                    )
                    mycsv0.writerow(
                        [protein_name, ligand_name, 'hbond', res_name, res_chain, res_idx_PDB, res_idx, atom_type1, isacceptor, x, y, z, atom_type3, x2, y2, z2, st]
                    )

            # hbond = a.__len__()

            # 卤素键
            a, b, strict = interactions.halogenbonds(protein, ligand)
            if a.__len__() != 0:
                new = open(os.path.join(path_output , 'halo.csv'), 'w', newline='')
                mycsv = csv.writer(new)
                for i in range(len(a)):
                    # protein
                    atom = protein.atoms[a[i][0]]
                    residue = protein.residues[int(a[i][9])]
                    res_name = a[i][11]
                    res_idx = a[i][9]
                    res_idx_PDB = a[i][10]

                    res_chain = residue.chain
                    atom_type1 = a[i][5]

                    isacceptor = a[i][13]
                    x = a[i][1][0]
                    y = a[i][1][1]
                    z = a[i][1][2]

                    # ligand
                    atom_type3 = b[i][5]
                    x2 = b[i][1][0]
                    y2 = b[i][1][1]
                    z2 = b[i][1][2]

                    st = strict[i]

                    mycsv.writerow(
                        [protein_name, ligand_name, 'halo',res_name, res_chain, res_idx_PDB, res_idx, atom_type1,
                         isacceptor, x, y, z, atom_type3, x2, y2, z2, st]
                    )
                    mycsv0.writerow(
                        [protein_name, ligand_name, 'halo', res_name, res_chain, res_idx_PDB, res_idx, atom_type1, 
                         isacceptor, x, y, z, atom_type3, x2, y2, z2, st]
                    )
            # halo = a.__len__()

            # pi-pi
            a,b ,c,d = interactions.pi_stacking(protein,ligand)
            if a.__len__() != 0:
                new = open(os.path.join(path_output , 'pipi.csv'), 'w', newline='')
                mycsv = csv.writer(new)
                for i in range(len(a)):
                    # protein
                    x = a[i][0][0]
                    y = a[i][0][1]
                    z = a[i][0][2]
                    residue = protein.residues[int(a[i][2])]
                    res_idx = a[i][2]
                    res_idx_PDB = a[i][3]
                    res_name = a[i][4]
                    res_chain = residue.chain
                    atom_type1 = '!'


                    isacceptor = '!'

                    # ligand
                    atom_type3 = '!'
                    x2 = b[i][0][0]
                    y2 = b[i][0][1]
                    z2 = b[i][0][2]

                    parallel = c[i]
                    perpendicular = d[i]

                    mycsv.writerow(
                        [protein_name, ligand_name, 'pipi',res_name, res_chain, res_idx_PDB, res_idx,atom_type1, isacceptor,x, y, z, atom_type3,x2, y2, z2, parallel,perpendicular]
                    )
                    mycsv0.writerow(
                        [protein_name, ligand_name, 'pipi', res_name, res_chain, res_idx_PDB, res_idx, atom_type1, isacceptor, x, y, z, atom_type3, x2, y2, z2, parallel, perpendicular]
                    )

            # pi_pi = a.__len__()

            # pi_cation
            a, b, c = interactions.pi_cation(protein, ligand)
            if a.__len__() != 0:
                new = open(os.path.join(path_output , 'pi-cation.csv'), 'w', newline='')
                mycsv = csv.writer(new)
                for i in range(len(a)):
                    if a[i][4] == '':
                        # 环在配体上
                        # ring
                        x2 = a[i][0][0]
                        y2 = a[i][0][1]
                        z2 = a[i][0][2]
                        atom_type3 = '!'
                        isacceptor = '!'
                        # cation
                        x = b[i][1][0]
                        y = b[i][1][1]
                        z = b[i][1][2]

                        atom = protein.atoms[b[i][0]]
                        residue = protein.residues[int(b[i][9])]
                        res_name = b[i][11]
                        res_idx = b[i][9]
                        res_idx_PDB = b[i][10]

                        res_chain = residue.chain
                        atom_type1 = b[i][5]


                    else:
                        # 环在蛋白上
                        x = a[i][0][0]
                        y = a[i][0][1]
                        z = a[i][0][2]
                        residue = protein.residues[int(a[i][2])]
                        res_idx = a[i][2]
                        res_idx_PDB = a[i][3]
                        res_name = a[i][4]
                        res_chain = residue.chain
                        atom_type1 = '!'


                        isacceptor = '!'

                        # cation
                        atom_type3 = b[i][5]
                        x2 = b[i][1][0]
                        y2 = b[i][1][1]
                        z2 = b[i][1][2]


                    st = c[i]

                    mycsv.writerow(
                        [protein_name, ligand_name, 'pi_cation',res_name, res_chain, res_idx_PDB, res_idx, atom_type1, 
                         isacceptor, x, y, z, atom_type3, x2, y2, z2, st]
                    )
                    mycsv0.writerow(
                        [protein_name, ligand_name, 'pi_cation', res_name, res_chain, res_idx_PDB, res_idx, atom_type1,
                         isacceptor, x, y, z, atom_type3, x2, y2, z2, st]
                    )

            # pi_cation = a.__len__()

            # 盐桥
            a, b, = interactions.salt_bridges(protein, ligand)
            if a.__len__() != 0:
                new = open(os.path.join(path_output , 'salt_bridge.csv'), 'w', newline='')
                mycsv = csv.writer(new)
                for i in range(len(a)):
                    # protein
                    atom = protein.atoms[a[i][0]]
                    residue = protein.residues[int(a[i][9])]
                    res_name = a[i][11]
                    res_idx = a[i][9]
                    res_idx_PDB = a[i][10]

                    res_chain = residue.chain
                    atom_type1 = a[i][5]

                    isacceptor = a[i][13]
                    x = a[i][1][0]
                    y = a[i][1][1]
                    z = a[i][1][2]

                    # ligand
                    atom_type3 = b[i][5]
                    x2 = b[i][1][0]
                    y2 = b[i][1][1]
                    z2 = b[i][1][2]

                    mycsv.writerow(
                        [protein_name, ligand_name,'salt_bridge', res_name, res_chain, res_idx_PDB, res_idx, atom_type1, 
                         isacceptor, x, y, z, atom_type3, x2, y2, z2]
                    )
                    mycsv0.writerow(
                        [protein_name, ligand_name, 'salt_bridge', res_name, res_chain, res_idx_PDB, res_idx, atom_type1, 
                         isacceptor, x, y, z, atom_type3, x2, y2, z2]
                    )
            # bridge = a.__len__()

            # 疏水
            a, b = interactions.hydrophobic_contacts(protein, ligand)
            if a.__len__() != 0:
                new = open(os.path.join(path_output , 'hydrophobic.csv'), 'w', newline='')
                mycsv = csv.writer(new)
                for i in range(len(a)):
                    # protein
                    atom = protein.atoms[a[i][0]]
                    residue = protein.residues[int(a[i][9])]
                    res_name = a[i][11]
                    res_idx = a[i][9]
                    res_idx_PDB = a[i][10]

                    res_chain = residue.chain
                    atom_type1 = a[i][5]
                    isacceptor = a[i][13]
                    x = a[i][1][0]
                    y = a[i][1][1]
                    z = a[i][1][2]

                    # ligand
                    atom_type3 = b[i][5]
                    x2 = b[i][1][0]
                    y2 = b[i][1][1]
                    z2 = b[i][1][2]

                    mycsv.writerow(
                        [protein_name, ligand_name, 'hydrophobic',res_name, res_chain, res_idx_PDB, res_idx, atom_type1, 
                         isacceptor, x, y, z, atom_type3, x2, y2, z2]
                    )
                    mycsv0.writerow(
                        [protein_name, ligand_name, 'hydrophobic', res_name, res_chain, res_idx_PDB, res_idx, atom_type1,
                         isacceptor, x, y, z, atom_type3, x2, y2, z2]
                    )
            new0.close()
        except:
            traceback.print_exc()

         # hydro = a.__len__()
         
