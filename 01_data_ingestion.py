# dataset can be obtained via https://zenodo.org/record/4596345#.Yk2flG5Bz0o
# folder containing one or more sub-folders 
# sub-folders are publications
# within each sub-folder, collection of text files that each constitute a document
# for now, supported naming pattern for text files is as such: '/sn86069873/1900-01-05/'
# LCCN title information and publication date (yyyy-mm-dd)
# users will need to provide publication names that match title information, or to use the metadata file


# indicate name of the folder containing data for ex 'data_tm_workflow'
folder_path = '/Users/mariellacc/Documents/TM/CI_newspaper_subcorpora'

import os
import pandas as pd
import re
import duckdb

publications_list = os.listdir(folder_path)

# remove DS_store files for mac OS
publications_list = [ file for file in publications_list if '.DS_Store' not in file ]

files_list = []

for pub in publications_list:
    files = os.listdir(f"{folder_path}/{pub}/")
    files = [ f"/{pub}/{file}" for file in files ]
    files_list.append(files)


# var files_list is alist of lists and needs to be transformed into one list
files_list_flat = [item for sublist in files_list for item in sublist]

#insert file names into a df
sources = pd.DataFrame(files_list_flat, columns=['file_name'])

# order of refs and names needs to match
pub_refs = ["2012271201","sn85054967","sn93053873","sn85066408","sn85055164","sn84037024","sn84037025","sn84020351","sn86092310","sn92051386"]
pub_names = ["Cronaca_Sovversiva","Il_Patriota","L'Indipendente","L'Italia","La_Libera_Parola","La_Ragione","La_Rassegna","La_Sentinella","La_Sentinella_del_West","La_Tribuna_del_Connecticut"]

# get publication reference from file name
def get_ref(file):
  ref_match = re.findall(r'(\w+\d+)_\d{4}-\d{2}-\d{2}_',file)
  return ref_match[0]

# get date from file name
def get_date(file):
  date_match = re.findall(r'_(\d{4}-\d{2}-\d{2})_',file)
  return date_match[0]

sources['date'] = sources['file_name'].apply(lambda x: get_date(x))
sources['publication_ref'] = sources['file_name'].apply(lambda x: get_ref(x))
sources["date"] = pd.to_datetime(sources["date"])

sources['publication_name'] = sources['publication_ref'].replace(pub_refs, pub_names)

# Start from 06.06.1903 and finish 01.05.1919
date_ref_1 = "1903-6-6"
date_ref_2 = "1919-5-1"

query = f"SELECT * FROM sources WHERE date <= DATE '{date_ref_2}' AND date > DATE '{date_ref_1}'"

subset_df = duckdb.query(query).df()

# read the content of the text files
def readTxtContent(fileName):
  with open(folder_path + fileName, 'r') as file:
    return ' ' + file.read().replace('\n', ' ') + ' '
  


# we are now using the subset to continue working
# add a column to the dataframe containing file content
subset_df['file_content'] = subset_df['file_name'].apply(lambda x: readTxtContent(x))
subset_df['chars_count'] = subset_df['file_content'].apply(lambda x: len(x))
subset_df['words_count'] = subset_df['file_content'].apply(lambda x: len(x.split()))

subset_df.to_csv('subset.csv')

