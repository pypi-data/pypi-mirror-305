import os
import rdkit
from rdkit import Chem
import pandas as pd
import shutil
import csv
from .cal_ifp_and_compose_pl import cal_ifp

def calInchiKey2smiFromTxt(smiles_txt_path):
    f = open(smiles_txt_path , 'r')
    smis = f.readlines()
    smis = [i[:-1] for i in smis]
    inchiKeys = [Chem.MolToInchiKey(Chem.MolFromSmiles(smi)) for smi in smis]
    inchiKey2smi = dict(zip(inchiKeys, smis))
    return inchiKey2smi
def remove_last_number_and_hyphen(elements):
    cleaned_elements = []

    for element in elements:
        # 找到最后一个 '-' 的位置
        last_hyphen_index = element.rfind('-')
        
        if last_hyphen_index != -1:
            # 去除最后的数字和前面的 '-'
            cleaned = element[:last_hyphen_index]
        else:
            cleaned = element  # 如果没有 '-', 返回原始元素
        
        cleaned_elements.append(cleaned)

    return cleaned_elements

def get_first_column_all_elements(file_path):
    first_column_elements = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            # 分割行，获取第一列元素
            first_column = line.split('\t')[0]  # 假设列之间用制表符分隔
            first_column_elements.append(first_column.strip())
    first_column_elements = first_column_elements[1:]
    return list(set(remove_last_number_and_hyphen(first_column_elements)))
def find_max_value_element(data):
    max_element = None
    max_value = float('-inf')

    for item in data:
        # 分割字符串，获取关键字和数值
        key, value_str = item.split('\t')
        value = float(value_str)  # 将数值字符串转换为浮点数

        # 更新最大值和对应元素
        if value > max_value:
            max_value = value
            max_element = item

    return max_element

def find_lines_with_biggestScore(file_path, search_string):
    matching_lines = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if search_string in line:
                matching_lines.append(line.strip())
    max_element = find_max_value_element(matching_lines)
    return max_element

def remove_last_number_and_hyphen_single(input_string):
    # 找到最后一个 '-' 的位置
    last_hyphen_index = input_string.rfind('-')
    
    if last_hyphen_index != -1:
        # 去除最后的数字和前面的 '-'
        cleaned_string = input_string[:last_hyphen_index]
    else:
        cleaned_string = input_string  # 如果没有 '-', 返回原始字符串
    
    return cleaned_string
def find_lines_with_min_num(file_path, search_string):
    matching_lines = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if search_string in line:
                matching_lines.append(line.strip())
    nums = min([int(get_last_number(i.split('\t')[0])) for i in matching_lines])
    # print(matching_lines)
    return nums
def get_last_number(input_string):
    # 找到最后一个 '-' 的位置
    last_hyphen_index = input_string.rfind('-')
    
    if last_hyphen_index != -1:
        # 提取最后一个 '-' 之后的部分
        last_part = input_string[last_hyphen_index + 1:]
        # 返回最后部分的数字
        return last_part
    else:
        return None  
    
def write_dict_to_csv(data_dict, csv_filename):
    # 打开或创建 CSV 文件
    with open(csv_filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        
        # 写入标题
        writer.writerow(['InchiKey', 'Smiles'])
        
        # 写入字典的键值对
        for key, value in data_dict.items():
            writer.writerow([key, value])

def get_final_smi_score(carsidock_prediction_file , smiles_txt_path):
    all_elements = get_first_column_all_elements(carsidock_prediction_file)
    inchiKey2smi =calInchiKey2smiFromTxt(smiles_txt_path)
    write_dict_to_csv(inchiKey2smi , os.path.join(os.path.dirname(carsidock_prediction_file) , 'inchiKey2smi.csv'))
    final_smiles = []
    final_scores = []
    for element in all_elements:
        # print(element)
        biggestScore = find_lines_with_biggestScore(carsidock_prediction_file , element)
        final_smile = inchiKey2smi[remove_last_number_and_hyphen_single(biggestScore.split('\t')[0])]
        final_smiles.append(final_smile)
        final_score = float(remove_last_number_and_hyphen_single(biggestScore.split('\t')[1]))
        final_scores.append(round(final_score,4))
    data = pd.DataFrame()
    data['smiles'] = final_smiles
    data['scores'] = final_scores
    data = data.sort_values(by='scores',ascending=False)
    data.to_csv(os.path.join(os.path.dirname(carsidock_prediction_file) , 'carsidock_prediction.csv') , index=False)


def get_final_ligand_poses(carsidock_prediction_file , protein_file_name , input_protein):
    all_elements = get_first_column_all_elements(carsidock_prediction_file)
    if not os.path.exists(os.path.join(os.path.dirname(carsidock_prediction_file) , 'ligand_poses')):
        os.mkdir(os.path.join(os.path.dirname(carsidock_prediction_file) , 'ligand_poses'))
    if not os.path.exists(os.path.join(os.path.dirname(carsidock_prediction_file) , 'top10_poses_interaction')):
        os.mkdir(os.path.join(os.path.dirname(carsidock_prediction_file) , 'top10_poses_interaction'))
        
    for element in all_elements:
        biggestScore = find_lines_with_biggestScore(carsidock_prediction_file , element)
        num = int(get_last_number(biggestScore.split('\t')[0]))
        num_min = find_lines_with_min_num(carsidock_prediction_file , element)
        index_num = num-num_min
        sdf_file = os.path.join(os.path.dirname(carsidock_prediction_file) , '%s.sdf'%element)
        output_file = os.path.join(os.path.dirname(carsidock_prediction_file) ,'ligand_poses', '%s.sdf'%element)
        suppl = Chem.SDMolSupplier(sdf_file)
        os.remove(sdf_file)
        mol = suppl[index_num]
        writer = Chem.SDWriter(output_file)
        writer.write(mol)
        writer.close()
    
    data_carsidock_prediction = pd.read_csv(os.path.join(os.path.dirname(carsidock_prediction_file) , 'carsidock_prediction.csv'))
    top10_smiles = list(data_carsidock_prediction['smiles'])[:10]
    data_map = pd.read_csv(os.path.join(os.path.dirname(carsidock_prediction_file) , 'inchiKey2smi.csv'))
    smi2inchikey = dict(zip(list(data_map['Smiles']), list(data_map['InchiKey'])))
    top10_inchikey = [smi2inchikey[i] for i in top10_smiles]
    top10_poses_path = os.path.join(os.path.dirname(carsidock_prediction_file) , 'top10_poses_interaction')
    protein_path = os.path.join(os.path.dirname(input_protein) , protein_file_name)
    for i in range(len(top10_inchikey)):
        tmp_inchikey = top10_inchikey[i]
        ligand_path = os.path.join(os.path.dirname(carsidock_prediction_file) , 'ligand_poses', '%s.sdf'%tmp_inchikey)
        top10_poses_path_tmp = os.path.join(top10_poses_path , 'top%s'%i)
        if not os.path.exists(top10_poses_path_tmp):
            os.mkdir(top10_poses_path_tmp)
        path_output = top10_poses_path_tmp
       # compose_protein_and_ligand(protein_path , ligand_path , path_output )
        cal_ifp(protein_path , ligand_path , path_output , i)
    
    compress_folder(os.path.join(os.path.dirname(carsidock_prediction_file) , 'ligand_poses'), os.path.join(os.path.dirname(carsidock_prediction_file) , 'ligand_poses'))
    compress_folder(os.path.join(os.path.dirname(carsidock_prediction_file) , 'top10_poses_interaction'), os.path.join(os.path.dirname(carsidock_prediction_file) , 'top10_poses_interaction'))
    os.system('rm -rf %s'%os.path.join(os.path.dirname(carsidock_prediction_file) , 'ligand_poses'))

def compress_folder(input_path, output_path):
    # 检查输入路径是否存在
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"The input path '{input_path}' does not exist.")
    
    # 压缩文件夹
    try:
        # Create a zip file from the input folder
        shutil.make_archive(os.path.splitext(output_path)[0], 'zip', input_path)
        print(f"Successfully compressed '{input_path}' into '{output_path}.zip'.")
    except Exception as e:
        print(f"An error occurred during compression: {e}")