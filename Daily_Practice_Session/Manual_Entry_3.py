import pandas as pd
Data = {
    "Product" : ["Suitcase", "Mobile", "Shampoo"],
    "Price" : [5000, 30000, 200],
    "Quantity" : [1,1,5]
}
Table_Data = pd.DataFrame(Data)
print(Table_Data)