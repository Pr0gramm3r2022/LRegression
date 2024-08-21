import numpy as np
import matplotlib as plt
import polars as pl
import pandas as pd

housingDf = pl.read_csv("california_housing_test.csv")
#MooreDF = pl.read_csv("! head transistor_data.csv") need to download the csv for the transistors

#function represented as Moore's Law
A_M = np.log(2) / 2
B_M = np.log(2250) - A_M * 1971
Moores_law =lambda year: np.exp(B_M) * np.exp(A_M * year)

ML_1971 = Moores_law(1971)
ML_1973 = Moores_law(1973)
print("In 1973, G. Moore expects {:0f} transistors on Intel's chips".format(ML_1973))
print("This is x{:.2f} more transistors than 1971".format(ML_1973 / ML_1971))

m = 4000 #test variable. need a way to convert the MooreDf to a csv for the regression

#MooreDf = pl.write_csv()
#attempting to turn this into an f string
#dataset is not on kaggle. need to find the csv or make this into a csv.
'''MooreDf = pl.to_csv("Processor,MOS transistor count,Date of Introduction,Designer,MOSprocess,Area
Intel 4004 (4-bit  16-pin),2250,1971,Intel,10,000 nm,12 mm²
Intel 8008 (8-bit  18-pin),3500,1972,Intel,10,000 nm,14 mm²
NEC μCOM-4 (4-bit  42-pin),2500,1973,NEC,7,500 nm,?
Intel 4040 (4-bit  16-pin),3000,1974,Intel,10,000 nm,12 mm²
Motorola 6800 (8-bit  40-pin),4100,1974,Motorola,6,000 nm,16 mm²
Intel 8080 (8-bit  40-pin),6000,1974,Intel,6,000 nm,20 mm²
TMS 1000 (4-bit  28-pin),8000,1974,Texas Instruments,8000 nm,11 mm²
MOS Technology 6502 (8-bit  40-pin),4528,1975,MOS Technology,8000 nm,21 mm²
Intersil IM6100 (12-bit  40-pin; clone of PDP-8),4000,1975,Intersil,,")
data = np.loadtxt("transistor_data.csv", delimiter=",", usecols=[1, 2], skiprows=1)
'''




