import pandas as pd
import numpy as np
from TestDataPrepKit import DataPrepKit

def test_read_data():
    # Test reading a CSV file
    df_csv = DataPrepKit.read_data('path/to/file.csv', 'csv')
    assert isinstance(df_csv, pd.DataFrame)

    # Test reading an Excel file
    df_excel = DataPrepKit.read_data('path/to/file.xlsx', 'excel', sheet_name='Sheet1')
    assert isinstance(df_excel, pd.DataFrame)

    # Test reading a JSON file
    df_json = DataPrepKit.read_data('path/to/file.json', 'json')
    assert isinstance(df_json, pd.DataFrame)

    # Test invalid file format
    with pytest.raises(ValueError):
        DataPrepKit.read_data('path/to/file.txt', 'txt')

def test_data_summary():
    # Create a sample DataFrame
    data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    
    # Test data summary
    DataPrepKit.data_summary(data)

    # Add appropriate assertions based on your expected output

def test_missing_values():
    # Create a sample DataFrame
    data = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, np.nan, 6]})
    
    # Test removing missing values
    strategy_remove = DataPrepKit.missing_values(data, 'remove')
    assert strategy_remove.isnull().sum().sum() == 0

    # Test filling missing values with a specific value
    strategy_fill = DataPrepKit.missing_values(data, 'fill', fill_value=0)
    assert strategy_fill.isnull().sum().sum() == 0

    # Test filling missing values with mean
    strategy_mean = DataPrepKit.missing_values(data, 'mean')
    assert strategy_mean.isnull().sum().sum() == 0

    # Test filling missing values with median
    strategy_median = DataPrepKit.missing_values(data, 'median')
    assert strategy_median.isnull().sum().sum() == 0

    # Test invalid strategy
    with pytest.raises(ValueError):
        DataPrepKit.missing_values(data, 'invalid_strategy')

def test_encoding_data():
    # Create a sample DataFrame
    data = pd.DataFrame({'A': ['red', 'blue', 'green'], 'B': ['cat', 'dog', 'cat']})
    
    # Test encoding data using one-hot encoding
    encoded_data = DataPrepKit.encoding_data(data)
    
    # Add appropriate assertions based on your expected output

# Run the tests
if __name__ == "__main__":
    pytest.main()