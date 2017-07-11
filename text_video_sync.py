'''
Created on May 20, 2017

@author: almasM
'''

import os
from math import ceil
from fuzzywuzzy import fuzz
import time

start_time = time.time()

mainDir = "/Users/almas/Documents/Research/"
subFileDir = mainDir + "Subtitles_Transcripts/sub_trans_sync/"
syncFolder = mainDir + "video_text_sync/"

if not os.path.exists(syncFolder):
    os.makedirs(syncFolder)

# #==================================
fileOutput = open("/Users/almas/Documents/Research/output_check.txt", 'w')


def findSubFile(videoF):
    
    videoSeason = videoF.find('_')
    endIndex = videoF.find('x')
    
    videoSeason = int(videoF[videoSeason+1:endIndex])
    videoEpisode = int(videoF[endIndex+1:])
    
#     videoStr = "VIDEO - season: " + str(videoSeason) + " episode: " + str(videoEpisode)

    for subFile in os.listdir(subFileDir):
        
        if subFile.startswith("."):
            continue
        
        subSeason = subFile.find('s_')
        subEpisode = subFile.find('ep_')
        subEndIndex = subFile.find('-')
        
#         print subFile
        subSeason = int(subFile[subSeason+2:subEpisode-1])
        subEpisode = int(subFile[subEpisode+3:subEndIndex])
        
#         subtitleStr =  "SUBTITLE - season: " + str(subSeason) + " episode: " + str(subEpisode)
        
        if videoSeason == subSeason and subEpisode == videoEpisode:
#             print videoStr + "<===>" + subtitleStr
           return subFile
        
def subTraverse(subFile):
    
    subFile = open(subFileDir + subFile, 'r')
    subList = []
    
    
    
    for line in subFile.readlines():
        if '-->' in line:
            
            begSubTime = line[:line.find('-')]
            begSubTime = begSubTime[:begSubTime.find(',')]
            
            endSubTime = line[line.find('>'):]
            endSubTime = endSubTime[endSubTime.find('>')+1:endSubTime.find(',')]
    
            subList.append( (line.strip('\n'), (toSecondConvert(begSubTime), toSecondConvert(endSubTime))) )
    return subList


def toSecondConvert(strTime):
    intTime = 0
    
    sec = int(strTime[len(strTime)-2:])
    
    min = strTime[strTime.find(':')+1:]
    min = int(min[:min.find(':')])
    
    hour = int(strTime[:strTime.find(':')])
    
    intTime = sec+(min*60) + (hour*3600)
    
    return intTime

def compSubVideo(timeVideo,subList):
    for tup in subList:
        if tup[1][0] <= timeVideo <= tup[1][1]:
            return tup[0]
    
    return min(subList, key=lambda x:abs(x[1][0]-timeVideo))[0]


def appendVideo(matchList, subFile):
    
    try:
        file = open(syncFolder + subFile, 'w')
    except IOError:
        file = open(syncFolder + subFile, 'w')
    
    subFile = open(subFileDir + subFile, 'r')
    
    for line in subFile:

        file.write(line)
        for item in matchList:      
            if fuzz.partial_ratio(line,item[1]) > 90:
                file.write(item[0] + "\n")
                break
    

def videoFolder():
    
    if not os.path.exists(mainDir+"episodes_images/"):
        raise ValueError('episodes_images folder does not exist')
    else:
        videoDir = mainDir+"episodes_images/"
    
    for videoF in os.listdir(videoDir):
#         print videoF
        if(videoF.startswith(".")):
            continue
        
        
        subFile = findSubFile(videoF)
        subList = subTraverse(subFile)
        
        begInd = videoF.find("x")
        epNum = videoF[begInd+1:]
        seasNum = videoF[begInd-1:begInd]
        
        matchList = []

        for picName in os.listdir(videoDir+videoF):
        
            if picName.startswith("."):
                continue
            
            minInd = picName.find("min_")
            secInd = picName.find("_sec_")
            endInd = picName.find(".png")
            
            minuteTime = picName[minInd+4:secInd]
            secondTime = picName[secInd+5:endInd]
            
            timeVideo =  (60*int(minuteTime)) + int(round(ceil(float(secondTime)), 1))
            
            matchTime = compSubVideo(timeVideo,subList)
            
            timeVideo = str(timeVideo)
            
            matchList.append((str(picName),matchTime))
            
            #==================================
            fileOutput.write("\n" + videoF + "\n" + " " + str(picName) + " | converted timeVideo: " + timeVideo + "\n matchTime: " +  str(matchTime))
#             fileOutput.write('\n'.join(str(line) for line in subList))
            
        appendVideo(matchList, subFile)



videoFolder()

print("--- %s seconds ---" % (time.time() - start_time))