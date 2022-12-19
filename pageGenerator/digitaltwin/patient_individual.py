# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 10:38:12 2022

@author: 20212238
"""

#format for patient data: [BMI,ADS,CDS,RMSSD,pNN50,LF/HF]

patient_data = [28,23,12,1,1,1]

def category(factor,v1,v2,v3,v4,s0 = 0,s1 = 1,s2 = 2,s3 = 3,s4 = 4):
    if factor < v1:
        score = s0
    elif factor < v2:
        score = s1
    elif factor < v3:
        score = s2
    elif factor < v4:
        score = s3
    elif factor >= v4:
        score = s4
    return score
        
#print(category(25,18.5,25,30,35,1,0))

def patient_score(parameter_list):
    
    information = []
    BMI_score = category(parameter_list[0],18.5,25,30,35,1,0)*1.03
    ADS_score = category(parameter_list[1],1,14,22,31)*1.23
    CDS_score = category(parameter_list[2],1,14,22,31)*0.55
        
    RMSSD_score = parameter_list[3]*1.036
    pNN50_score = parameter_list[4]*1.057
    LF_HF_score = parameter_list[5]*0.509
        
    PPG_score = (RMSSD_score + pNN50_score + LF_HF_score)*0.5/2.602
    lifestyle_score = (BMI_score + ADS_score + CDS_score)*0.5/11.24
    
    information.append(BMI_score)
    information.append(ADS_score)
    information.append(CDS_score)
    information.append(RMSSD_score)
    information.append(pNN50_score)
    information.append(LF_HF_score)
    information.append(PPG_score)
    information.append(lifestyle_score)
    
    if PPG_score == 0.5:    #feedback in case all three PPG-parameter values are too high
        risk_score = 100
        information.append(risk_score)
        
    else:                   #feedback in case not all PPG-parameter values are too high
        risk_score = (PPG_score + lifestyle_score)*100
        information.append(risk_score)
        
    return information
    