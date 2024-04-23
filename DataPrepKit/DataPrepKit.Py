
import pandas as PD
import numpy as NP

class DataPrepKit:
    
   
    
    def read_data(file_path, file_format, sheet_name=None):
        if file_format == 'csv':
            return PD.read_csv(file_path)
        elif file_format == 'excel':
            return PD.read_excel(file_path, sheet_name=sheet_name)
        elif file_format == 'json':
            return PD.read_json(file_path)
        else:
            raise ValueError("Invalid file format. Supported formats: 'csv', 'excel', 'json'")

    dt=read_data('scr\DataPrepKit\CSVFile.csv','csv')

    print(dt)
    

    def data_summary(data):
    
        print("\n-------------- Data Summary: -------------- \n")
        print("Shape:", data.shape)
        print("Columns:", data.columns.tolist())
        print("\n--------------Data Statistics: -------------- \n")
        print("Count:\n", data.count())

        print("\nMean:\n")
        for column in data.columns:
            print(column + ":")
            if PD.to_numeric(data[column], errors='coerce').notnull().all():
                print(data[column].mean())
                print("\n")
            else:
                 print("Non-numerical data \n")

        print("\nMedian: \n")
        for column in data.columns:
            if PD.to_numeric(data[column], errors='coerce').notnull().all():
                print(data[column].median())
            else:
                print("Non-numerical data")  

        print("\nMode: \n")
        for column in data.columns:
            if PD.to_numeric(data[column], errors='coerce').notnull().all():
                print(data[column].mode().tolist())
            else:
                print("Non-numerical data")

        print("")
        print("Minimum:\n", data.min())
        print("")
        print("Maximum:\n", data.max())
        print("")
        print("Most Frequent Values foe each column: \n")
        for column in data.columns:
            print(data[column].value_counts().head(10))
            print("")
            
    data_summary(dt)   

    def missing_values(data,strategy,fill_value=None):
       
            if strategy=='remove':
                print("\nremove:\n")
                return data.dropna()
            elif strategy == 'fill':
                return data.fillna(fill_value)
           
            if PD.to_numeric(data, errors='coerce').notnull().all():   

                if strategy=='mean':
                    print("\nMean:\n")
                    mean_data=data.mean()
                    return data.fillna(mean_data)
                
                elif strategy=='median':
                    print("\nMedian:\n")
                    median_data=data.median()
                    return data.fillna(median_data)
                else:
                        raise ValueError("Invalid strategy, Please choose one of 'remove', 'mean', 'median','fill'.")

            else:
                print("Non-numerical data \n")

    missing_values(dt,'fill',7)

    def encoding_data(data):

        print("\n-------------- Encoding Data use One-Hot Encoding: -------------- \n")
        print(PD.get_dummies(data,dtype=float))

    encoding_data(dt)



