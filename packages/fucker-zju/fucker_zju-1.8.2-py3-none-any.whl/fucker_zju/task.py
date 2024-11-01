import os
import subprocess
import pandas as pd
from .util_post_process import get_final_smi_score , get_final_ligand_poses
import sys


def read_smiles_from_file(text_file):
    molecules_dict = {}
    
    with open(text_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            molecule_info = line.split()
            molecule_name = molecule_info[1]
            molecule_smiles = molecule_info[0]
            molecules_dict[molecule_name] = molecule_smiles 
    return molecules_dict


def process_karmadock_prediction_files(text_file, csv_file,karmadock_score_top_smile_txt , topN=50):
    
    df = pd.read_csv(csv_file)
    sorted_df = df.sort_values(by='karma_score', ascending=False).iloc[:topN,:]
    smile_ids = list(sorted_df['pdb_id'])

    name2smile = read_smiles_from_file(text_file)
    
    
    top_smiles = []
    for i in smile_ids:
        top_smiles.append(name2smile[i])
    
    print(top_smiles)
    
    with open(karmadock_score_top_smile_txt, 'w') as outfile:
        for smiles in top_smiles:
            outfile.write(smiles + '\n')
            
    sorted_df = df.sort_values(by='karma_score', ascending=False)
    sorted_df.insert(loc=1, column='smiles', value=[name2smile[i] for i in sorted_df['pdb_id']])
    sorted_df.rename(columns={'pdb_id': 'molecule_id'}, inplace=True)
    return sorted_df
    # sorted_df.to_csv(os.path.join(os.path.dirname(text_file) , 'karmadock_prediction_dealt.csv') , index=False)
    

def karmadock_prediction(protein_file , crystal_ligand_file , ligand_smi, out_dir,cuda_number):
        print('--shm-size="8g"')
        cmd = 'docker run -it --rm -v ./:/app  --shm-size="8g" docking_carsidock:rtx40_v4_0818 /bin/bash -c \
                "source activate && conda activate karmadock && cd /app/Models/KarmaDock/utils  && unset LD_LIBRARY_PATH && export LD_LIBRARY_PATH=/opt/conda/envs/karmadock/lib:$LD_LIBRARY_PATH  && \
                CUDA_VISIBLE_DEVICES=%s python -u virtual_screening.py \
                --ligand_smi %s \
                --protein_file %s \
                --crystal_ligand_file %s \
                --out_dir %s \
                --score_threshold 0 \
                --batch_size 64 \
                --random_seed 2023 "' % (cuda_number, ligand_smi, protein_file, crystal_ligand_file, out_dir)
        subprocess.call(cmd, shell=True)


def carsidock_prediction(protein_file , crystal_ligand_file , ligand_sdf, out_dir , cuda_number):
        cmd = 'docker run -it --rm -v ./:/app --shm-size="8g" docking_carsidock:rtx40_v4_0818 /bin/bash -c \
                "cd /app/Models/CarsiDock && CUDA_VISIBLE_DEVICES=%s python -u run_screening.py \
                --cuda_convert \
                --pdb_file %s \
                --reflig %s \
                --ligands %s \
                --output_dir %s"' %(cuda_number, protein_file , crystal_ligand_file , ligand_sdf,out_dir)
        subprocess.call(cmd, shell=True)
    

def change_path(old_path, old_substring='/app', new_substring='.'):
    if old_path.startswith(old_substring):
        new_path = old_path.replace(old_substring, new_substring, 1)
        return new_path
    else:
        return "原始路径不包含指定子字符串"
    
def change_path_reverse(old_path, old_substring='.', new_substring='/app'):
    if old_path.startswith(old_substring):
        new_path = old_path.replace(old_substring, new_substring, 1)
        return new_path
    else:
        return "原始路径不包含指定子字符串"
    
          
def hierarchical_prediction(protein_file_docker , crystal_ligand_file_docker , ligand_smi_docker, out_dir_docker, topN=50, Poses_keep = False):

    try:
        cuda_number = 0 
         
        karmadock_prediction(protein_file_docker , crystal_ligand_file_docker , ligand_smi_docker, out_dir_docker,cuda_number)
        os.rename(os.path.join(change_path(out_dir_docker) , 'score.csv') , os.path.join(change_path(out_dir_docker) , 'karmadock_prediction.csv'))
        karmadock_prediction_file = os.path.join(change_path(out_dir_docker) , 'karmadock_prediction.csv')
        
        ligand_smi_local = change_path(ligand_smi_docker)
        karmadock_score_top_smile_txt = os.path.join(out_dir_docker , 'karmadock_score_top%s_smile.txt'%topN)
        
        data_dealt = process_karmadock_prediction_files(ligand_smi_local, karmadock_prediction_file,  change_path(karmadock_score_top_smile_txt)  ,topN)
        data_dealt.to_csv(os.path.join(os.path.dirname(change_path(karmadock_score_top_smile_txt)) , 'karmadock_prediction_dealt.csv') , index=False)
        
        
       
        carsidock_prediction(protein_file_docker , crystal_ligand_file_docker , karmadock_score_top_smile_txt, out_dir_docker,cuda_number)
               
        carsidock_prediction_file = change_path(os.path.join(out_dir_docker , 'score.dat'))
        karmadock_score_top_smile_txt_local = change_path(os.path.join(out_dir_docker , 'karmadock_score_top%s_smile.txt'%topN))
        get_final_smi_score(carsidock_prediction_file , karmadock_score_top_smile_txt_local)
              
        protein_file_name = os.path.basename(protein_file_docker)
        get_final_ligand_poses(carsidock_prediction_file , protein_file_name , change_path(protein_file_docker))
        
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'carsidock_prediction.csv')):
            os.rename(os.path.join(change_path(out_dir_docker), 'carsidock_prediction.csv')   , os.path.join(change_path(out_dir_docker), 'rtmscore_prediction.csv'))
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'inchiKey2smi.csv')):
            os.remove(os.path.join(change_path(out_dir_docker), 'inchiKey2smi.csv'))
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'karmadock_prediction.csv')):
            os.remove(os.path.join(change_path(out_dir_docker), 'karmadock_prediction.csv'))
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'karmadock_prediction_dealt.csv')):
            os.rename(os.path.join(change_path(out_dir_docker), 'karmadock_prediction_dealt.csv') , os.path.join(change_path(out_dir_docker), 'karmadock_prediction.csv'))
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'score.dat')):
            os.remove(os.path.join(change_path(out_dir_docker), 'score.dat'))
            
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'karmadock_score_top%s_smile.txt'%topN)):
            os.remove(os.path.join(change_path(out_dir_docker), 'karmadock_score_top%s_smile.txt'%topN))
            
        if os.path.exists(os.path.join(change_path(out_dir_docker), 'top10_poses_interaction')):
            os.system('rm -rf %s'%os.path.join(change_path(out_dir_docker), 'top10_poses_interaction'))
        if not Poses_keep:
            os.remove(os.path.join(change_path(out_dir_docker), 'ligand_poses.zip'))
         
            
    except Exception as e:
    
        print("发生错误:", e)
        sys.exit(1)



def test():
    print('test')




# ligand_smi = './example/active_decoys.smi'
# protein_file = './example/6PYR_optimal_pocket.pdb'
# crystal_ligand_file = './example/crystal_ligand.mol2'
# out_dir = './out_dir'
# topN=10
# Poses_keep = True
# hierarchical_prediction(change_path_reverse(protein_file) , change_path_reverse(crystal_ligand_file), change_path_reverse(ligand_smi), change_path_reverse(out_dir), topN=topN, Poses_keep = Poses_keep)




