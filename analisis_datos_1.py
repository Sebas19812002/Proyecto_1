import matplotlib.pyplot as plt
import pandas as pd

datos= pd.read_csv("Datos.data")
datos.head()

for i in range (0,len(datos)):
    if datos["Ca"][i]=="?":
        datos.drop(i, axis=0, inplace=True)
    elif datos["Thal"][i]=="?":
        datos.drop(i, axis=0, inplace=True)

datos[["Ca","Thal"]]=datos[["Ca","Thal"]].apply(pd.to_numeric)

scores=["Age","Trestbps", "Chol","Thalach","Oldpeak","Ca","Num"]