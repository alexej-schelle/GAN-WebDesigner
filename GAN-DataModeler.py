###################################################################################################################################################
#                                                                                                                                                 #
#   Autor: Dr. A. Schelle (alexej.schelle.ext@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt       #
#   Autor: Peronnik Unverzagt (peronnik.unverzagt@iu.org). Copyright : IU Internationale Hochschule GmbH, Juri-Gagarin-Ring 152, D-99084 Erfurt   #                                                                                                                                           #
#                                                                                                                                                 #
###################################################################################################################################################

# PYTHON ROUTINE zur Modellierung von Daten durch GAN-Netzwerke #

import os
import sys
import statistics
import math
import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from functools import reduce

def Generator(ID, length):

    output_key = [0]*length
    output_key[0] = ID

    for k in range(0, length):

        if (k == 1):

                        # TO DOs: Teste Genauigkeit für Gaußverteilte Daten (verwende anstatt 'random.randint(10, 100)' --> 'random.gauss(mu, sigma)' - Mittelwert mu || standard abweichung --> sigma -> math.sqrt(variance) mit mu und sigma aus Python statements in Pandas
                        # df['Key'].copy() projiziert den Datensatz auf den reduzierten Datensatz mit Tabellenspalten Key 
                        # df['Key'].mean() definiert den Mittelwert und df['Key'].std() definiert die Standardabweichung

            output_key[1] = random.randint(10, 100) # Alter im Bereich von zehr bis Hundert Jahre

        if (k == 2):

            choose_gender = random.randint(0,1)

            if (choose_gender == 0):

                output_key[2] = 'Male' 
            
            if (choose_gender == 1):

                output_key[2] = 'Female' 

        if (k == 3):

            choose_headset_type = random.randint(0,2)

            if (choose_headset_type == 0):

                output_key[3] = 'Oculus Rift' 
            
            if (choose_headset_type == 1):

                output_key[3] = 'HTC Vive' 

            if (choose_headset_type == 2):

                output_key[3] = 'PlayStation VR' 

        if (k == 4):

            # TO DOs: Teste die Modellierung mit Gaußverteilung

            output_key[4] = random.uniform(df['Duration'].min(),df['Duration'].max())

        if (k == 5):

            # TO DOs: Teste die Modellierung mit Gaußverteilung

            output_key[5] = random.randint(df['MotionSickness'].min(),df['MotionSickness'].max())

        if (k == 6):

            # TO DOs: Teste die Modellierung mit Gaußverteilung

            output_key[6] = random.randint(df['ImmersionLevel'].min(),df['ImmersionLevel'].max())


    return(output_key)


def Differentiator(df, data_1, data_2, data_3, data_4, data_5, data_6, data_7, accuracy):

    similarity_measure = 0 

    if ((df.iloc[j]['Age']-data_2)/data_2*100.0 < (100.0 -  accuracy) and (df.iloc[j]['Duration']-data_5)/data_5*100.0 < (100.0 -  accuracy) and (df.iloc[j]['MotionSickness']-data_6)/data_6*100.0 < (100.0 -  accuracy) and (df.iloc[j]['ImmersionLevel']-data_7)/data_7*100.0 < (100.0 -  accuracy)):

        similarity_measure = 1

    return similarity_measure

# Replace 'your_file.csv' with the path to your CSV file
df = pd.read_csv('/Users/krealix/Desktop/IU_Internationale_Hochschule/SoSe2024/DSUE042301_VC_SoSe_2024/PythonSource/UserExperienceData.csv')

# Code for printing to a file
sample = open('ModelData.csv', 'w')

# Code for printing to a file
sample_realistic = open('RealisticModelData.csv', 'w')

data = []
index = 0
sample_size = 5000
number_of_similar_data_maps = 3
data_dimension = 7
data_similarity = 80.0

print(','.join(['UserID', 'Age', 'Gender', 'VRHeadset', 'Duration', 'MotionSickness', 'ImmersionLevel']), file=sample)

for i in range(1, sample_size):

    writer_var = Generator(i, data_dimension)
    print(writer_var[0], ',', writer_var[1], ',', writer_var[2], ',', writer_var[3], ',', writer_var[4], ',', writer_var[5], ',', writer_var[6], file = sample)

print(','.join(['UserID', 'Age', 'Gender', 'VRHeadset', 'Duration', 'MotionSickness', 'ImmersionLevel']), file=sample_realistic)

for j in range(0, number_of_similar_data_maps):

    print(j)

    for i in range(1, 1002):

        similarity = 0

        while(1==1):

            writer_var = Generator(i, data_dimension)

# TO DOs: Teste die Genauigkeit nochmals mit Gaußverteilten Daten und mit neuen data_similarity Definition
    
    # if ((df.iloc[j]['Age']-writer_var[1])/writer_var[1]*100.0 < (100.0 - data_similarity) and (df.iloc[j]['Duration']-writer_var[4])/writer_var[4]*100.0 < (100.0 - data_similarity) and (df.iloc[j]['MotionSickness']-writer_var[5])/writer_var[5]*100.0 < (100.0 - data_similarity) and (df.iloc[j]['ImmersionLevel']-writer_var[6])/writer_var[6]*100.0 < (100.0 - data_similarity)):

            similarity = Differentiator(df, writer_var[0], writer_var[1], writer_var[2], writer_var[3], writer_var[4], writer_var[5], writer_var[6], data_similarity)
                 
            if (similarity == 1):

                print(index,',',writer_var[1], ',', writer_var[2], ',', writer_var[3], ',', writer_var[4], ',', writer_var[5], ',', writer_var[6], file = sample_realistic)    
                index = index + 1

            if (similarity == 1): 
            
                break    

# TO DOs: Finde eine Möglichkeit die Daten auch in den externen Files ohne Blanks darzustellen
# TO DOs: Modellierung für unterschiedliche Datengenauigkeiten bei der Abbildung von Originaldaten zu synthetischen Daten und Zusammenfassung in einer Tabelle
# Versuche den Unterschied zwischen dem SVM-Modell und einem Modell wie Decision Tree anhand der Ergebnisse und der Modell-Definitionen zu verstehen