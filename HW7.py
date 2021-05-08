from numpy.core.fromnumeric import mean
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as pyplot 
import statistics as sts
def draw_histogram():
     data = pd.read_csv("DataDJ.csv")

#DJFRANCES 
    #  DJFranses = data["Return_DJFranses"] 

    #  bins = np.arange(-0.2, 0.2, 0.0005) 
    #  pyplot.hist(DJFranses, bins = bins, edgecolor = "#04DE71", log = True)
    #  mean_JF = np.mean(np.array(DJFranses)) 
    #  variance_JF = sts.variance(np.array(DJFranses)) 

    #  pyplot.axvline(mean_JF, color = 'red', label = "DJFrances Mean")
    #  pyplot.axvline(variance_JF, color = 'Black', label = "DJFrances Variance")
     
    #  print("Mean_DJFranses= " + str(mean_JF))
    #  print("Variance_DJFranses = " + str(variance_JF))
    #  pyplot.title("DJFrances Histogram")
    #  pyplot.show() 

#DJIA
     DJIA = data["Return_DJIA"]
     bins = np.arange(-0.1, 0.1, 0.0001) 
     pyplot.hist(DJIA, bins = bins, edgecolor = "#04DE71", log = True)
     mean_DJIA = np.mean(np.array(DJIA)) 
     variance_DJIA = sts.variance(np.array(DJIA)) 

     pyplot.axvline(mean_DJIA, color = 'red', label = "DJIA Mean")
     pyplot.axvline(variance_DJIA, color = 'Black', label = "DJIA Variance")
     
     print("Mean_DJIA = " + str(mean_DJIA))
     print("Variance_DJIA = " + str(variance_DJIA))
     pyplot.title("DJIA Histogram")
     pyplot.show() 