import pandas as pd
Data = {
    "City" : ["Delhi", "Assam", "Mizoram"],

    "Population" :[5000,3300,2000] 
}

Table_Population = pd.DataFrame(Data)
print(Table_Population)