import pandas as pd
file_path = "team.json"
df = pd.read_json(file_path)

print("DataFrame from json: ")
print(df)

data = {
    "Duration":{
        "0": 60,
        "1": 59,
        "2": 60,
        "3": 45,
    }, 
    
    "Pulse":{
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
    },  
    
    "Maxpulse":{
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 174,
    }, 
    
    "Calogies":{
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
    }, 
}

df = pd.DataFrame(data)
print(df)