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
# Histogramas relacionados a las variables
for i in scores:
    
    fig = plt.figure()
    x=datos[i]
    grafica=x.plot(kind="hist")
    grafica.set_title(i)
plt.show()
# Boxplots
for i in scores:
    fig = plt.figure()
    grafica=datos.boxplot(column= [str(i)])
    grafica.set_title(i)
plt.show()

# Estadisticas descriptivas
print(datos.min())
print(datos.mean())
print(datos.max())
print(datos.corr())
corr=datos.corr()
#Este codigo exporta a un xlsx el resultado corr.to_excel('correlaciones.xlsx')

for i in scores:
    for j in scores:
        fig, ax = plt.subplots()
        ax.scatter(datos[i],datos[j])
        ax.set_title (i + " VS " + j)
        plt.show()
