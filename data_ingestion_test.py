import os
import pandas as pd

# TESTS FOR 01_data_ingestion.py

def test_data_ingestion_subset():
    #test if the subset_df was created:
    if not os.path.exists('subset.csv'):
        raise ImportError('subset.csv do not exist')

# Now that we verified the subset.csv file exists, we can load it into a dataframe to test if it has the expected columns
subset = pd.read_csv('subset.csv')

def test_dataframe_columns():
    # Check if it has the expected columns
    expected_columns = ['file_name', 'date', 'publication_ref', 'publication_name', 'file_content', 'chars_count', 'words_count']
    assert all(col in subset.columns for col in expected_columns)
    # Check that each specified column is not empty
    for column in expected_columns:
        assert not subset[column].empty, f"{column} column is empty"