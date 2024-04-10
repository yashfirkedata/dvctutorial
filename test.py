import pandas as pd

Data = [
    {"name": "Yash", "age": 20},
    {"name": "Vijay", "age": 50},
    {"name": "Firke", "age": 70},
]

Data = pd.DataFrame(Data)
Data.to_csv("data/data.csv", index=False)