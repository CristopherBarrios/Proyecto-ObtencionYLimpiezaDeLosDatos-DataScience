import pandas as pd
import numpy as np

AltaVerapaz = pd.read_csv('data/csv/AltaVerapaz.csv', encoding='latin1')
BajaVerapaz = pd.read_csv('data/csv/BajaVerapaz.csv', encoding='latin1')
Chimaltenango = pd.read_csv('data/csv/Chimaltenango.csv', encoding='latin1')
Chiquimula = pd.read_csv('data/csv/Chiquimula.csv', encoding='latin1')
CiudadCapital = pd.read_csv('data/csv/CiudadCapital.csv', encoding='latin1')
ElProgreso = pd.read_csv('data/csv/ElProgreso.csv', encoding='latin1')
Escuintla = pd.read_csv('data/csv/Escuintla.csv', encoding='latin1')
Guatemala = pd.read_csv('data/csv/Guatemala.csv', encoding='latin1')
Huehuetenango = pd.read_csv('data/csv/Huehuetenango.csv', encoding='latin1')
Izabal = pd.read_csv('data/csv/Izabal.csv', encoding='latin1')
Jalapa = pd.read_csv("data/csv/Jalapa.csv", encoding='latin1')
Jutiapa = pd.read_csv("data/csv/Jutiapa.csv", encoding='latin1')
Peten = pd.read_csv("data/csv/Peten.csv", encoding='latin1')
Quetzaltenango = pd.read_csv("data/csv/Quetzaltenango.csv", encoding='latin1')
Quiche = pd.read_csv("data/csv/Quiche.csv", encoding='latin1')
Retalhuleu = pd.read_csv("data/csv/Retalhuleu.csv", encoding='latin1')
Sacatepequez = pd.read_csv("data/csv/Sacatepequez.csv", encoding='latin1')
SanMarcos = pd.read_csv("data/csv/SanMarcos.csv", encoding='latin1')
SantaRosa = pd.read_csv("data/csv/SantaRosa.csv", encoding='latin1')
Solola = pd.read_csv("data/csv/Solola.csv", encoding='latin1') 
Suchitepequez = pd.read_csv("data/csv/Suchitepequez.csv", encoding='latin1')
Totonicapan = pd.read_csv("data/csv/Totonicapan.csv", encoding='latin1')
Zacapa = pd.read_csv("data/csv/Zacapa.csv", encoding='latin1')

#unimos los datasets
departamentos = [AltaVerapaz, BajaVerapaz, Chimaltenango, Chiquimula, CiudadCapital, ElProgreso, Escuintla, Guatemala, Huehuetenango, Izabal,
                 Jalapa, Jutiapa, Peten, Quetzaltenango, Quiche, Retalhuleu, Sacatepequez, SanMarcos, SantaRosa, Solola, 
                 Suchitepequez, Totonicapan, Zacapa]

PaisGuatemala = pd.concat(departamentos, join='inner')
titulos = PaisGuatemala.iloc[0]
PaisGuatemala = PaisGuatemala[1:]
PaisGuatemala.columns = titulos
PaisGuatemala.rename(columns=PaisGuatemala.iloc[0])
print(PaisGuatemala.head())