'''
Created on May 12, 2017

@author: almasM
'''

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
from itertools import islice
import re 
import os

transList = []

def cleanJSON(mainDir):
    rawJSON = open(mainDir+"friends_season1.txt")
    
    cleanedJSON = mainDir+"S_1_json_clean.txt"
    try:
        fileJSON = open(cleanedJSON, 'w')
    except IOError:
        fileJSON = open(cleanedJSON, 'w')
    
    for line in rawJSON.readlines():
        if('\"season_id\":' in line):
            fileJSON.write(line)
        elif('\"episode_id\":' in line):
            fileJSON.write(line)
        elif('\"scene_id\":' in line):
            fileJSON.write(line)
        elif('\"speaker\":' in line):
            tempName = line.rstrip()
        elif('\"utterance_raw\":' in line):
            fileJSON.write(tempName + line)
            tempName = ""
            
    return cleanedJSON
            

def transcriptToList(fileTrans):
    transName = ""
    transSpeech = ""
    fileTrans = open(fileTrans)
    for line in fileTrans.readlines():
        lineS  = line.split()
#         print(lineS)
        for x, y in enumerate(lineS):
            if('\"season_id\":' in lineS):
                transSpeech = y.replace(',','')
                if(fuzz.partial_ratio(y, '\"season_id\":') > 80):
                    transName = y
            elif('\"episode_id\":' in lineS):
                transSpeech = y.replace(',','')
                if((fuzz.partial_ratio(y, '\"episode_id\":') > 80)):
                    transName = y
            elif('\"scene_id\":' == y):
                transName = y
                transSpeech = ''.join(x for x in lineS[x+1] if x.isalnum())
            elif '\"speaker\":' == y:
                transName = ''.join(x for x in lineS[x+1] if x.isalnum())
#                 print(transName)
            elif '\"utterance_raw\":' == y:
                transSpeech = ' '.join(lineS[x+1:len(line)-1])
#                 print(transSpeech)
        transList.append((transName,transSpeech))
#     print(transList)    


def subToList(filenameSub):
    
    subList = []
    subLine = ""
    subLineTime = ""
    fileSub = open(filenameSub)
    
    for line in fileSub.readlines():
        lineS = line.split()
#         print(line)
        if('-->' in lineS):
            subLineTime = line
#             print(subLineTime)
        else:
            while '-->' not in lineS:
                subLine = subLine + line
                try:
                    next(fileSub)
                except(StopIteration):
                    break                    
        
            subLine = re.sub(r'[(\r)(\d+)(\n)]', '', subLine)
            subLineTime = re.sub(r'[(\r)(\n)]', '', subLineTime)
            if(subLine != ''):
                subList.append((subLineTime, subLine))
#                 print((subLineTime, subLine))
        subLine = ""    
    
    return subList
     
     
                
def matchTranSub(subList, fileM, epiNum):
    
    epiNum = int(epiNum)
    
    
    
    begInd = 0
    endInd = 0

    subLine = [y[1] for y in subList]
       
    transLine = []
    
    for x in transList:
        #x[1] in str(epiNum)
        if(x[1] == str(epiNum) and x[0] in '\"episode_id\":'):
#             transLine.append(transList[transList.index(x):])
            begInd = transList.index(x)
#             print x
            continue
        elif(x[1] == str(epiNum+1) and x[0] in '\"episode_id\":'):
            endInd = transList.index(x)
#             print x
            break
    
    transLine = list(transList[begInd:endInd])
#     print(transLine)
#     print transList[begInd:endInd]
    
    countSub = 0
    y = 0
    
    #==================================
#     fileOutput.write('\n'.join(str(line) for line in transLine))
    
    for item in transLine:
        
        if(fuzz.partial_ratio(item[0], "scene_id:") > 80):
            fileM.write(item[0] + "\t " + item[1] + "\n")
        
        countSub = 0

        while(len(subLine) > countSub):
            if(fuzz.partial_ratio(item[1], subLine[countSub]) > 80):
                fileM.write(subList[countSub][0] + "\n")
                fileM.write(item[0] + ": ")
                fileM.write(item[1] + "\n")

            countSub += 1
        

def episodeNum(filenameSub):
    epiNum = 0
    
    begInd = filenameSub.find("ep_")
    epiNum = filenameSub[begInd+3:(begInd+5)]
    
    return str(epiNum)


def convertST(directory):
    
    newPath = directory+"sub_trans_sync/"
    subPath = directory + "Subtitles/"
    
    if not os.path.exists(newPath):
        os.makedirs(newPath)

    for filenameSub in os.listdir(subPath):
        
        if(filenameSub.startswith(".")):
            continue
        
        os.chdir(newPath)
        
        try:
            file = open(filenameSub+".txt", 'w')
        except IOError:
            file = open(filenameSub +".txt", 'w')
        
        os.chdir(subPath)
        
        #==================================
#         fileOutput.write("\n" + filenameSub + "\n")
        
        print("Current subtitle file being evaluated: " + filenameSub)
        subList = subToList(filenameSub)
        
#         print subList
        
    
        epiNum = episodeNum(str(filenameSub))
        matchTranSub(subList, file, epiNum)
                    
    
mainDir = "/Users/almas/Documents/Research/Subtitles_Transcripts/"  

# #==================================
# fileOutput = open(mainDir + "output_check.txt", 'w')
  
cleanedJSON = cleanJSON(mainDir)
transcriptToList(cleanedJSON)

convertST(mainDir)

