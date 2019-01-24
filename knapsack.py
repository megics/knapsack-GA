#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#--------------------------------------------------------#
# Author: Meliha Gizem ÇELİK
# Copyright: Copyright 2018
# Python Version: 3
# Project: Solve Knapsack Problem with Genetic Algorithms
#--------------------------------------------------------#

import math
import matplotlib.pyplot as plt

randomList = []
weightList = []
valueList = []
randCount = 0

### read the file section ###
txtNum = input('Enter a test file number: ')        # file number can be:1, 2, 3, 4, 5
f = open("input/test{0}.txt".format(txtNum),"r")
randomList = f.readline().strip('\n').split(",")  	# comma separated random list
populationSize = int(f.readline().strip('\n')) 	    # population size
k = f.readline() 	                                # number of tournament elements
m = float(f.readline().strip('\n'))		            # mutation probability[0-1]
iteration = int(f.readline().strip('\n')) 	        # number of iteration
bagSize = int(f.readline().strip('\n')) 	        # bag size
weightList = f.readline().strip('\n').split(",") 	# comma separated weight list
valueList = f.readline().strip('\n').split(",") 	# comma separated value list
f.close()

### create population method ###
def initialise():  
	person = ""
	personList = []
	global randCount
	for x in range(populationSize):
		for z in range(len(weightList)):
			if(randCount == len(randomList)):
				randCount=0
			if(float(randomList[randCount%len(randomList)]) < 0.5):
				person += "0"
			else:
				person += "1"

			randCount+=1		
		personList.append(person)
		person = ""
	return personList	

### create fitness values list for population in this method ###
def evaluate(pList):
	sumWeight=0
	sumValue=0
	fitnessList = []
	for i in range(len(pList)):
		for j in range(len(pList[i])):
			if(pList[i][j] == "1"):
				sumWeight += int(weightList[j])
				sumValue += int(valueList[j])
		if(sumWeight <= bagSize):
			fitnessList.append((pList[i],sumValue))
		else:
			fitnessList.append((pList[i],0))
		sumWeight=0
		sumValue=0
	return fitnessList

### using tournament select algorithm for parent select in this method ###
def parentSelect(fList):
	tempList = []
	parentSelectList = []
	global randCount
	for i in range(len(fList)):
		for j in range(int(k)):
			if(randCount == len(randomList)):
				randCount=0
			index = math.ceil(float(randomList[randCount%len(randomList)])*len(fList))-1
			tempList.append(fList[index])
			randCount+=1
		tempList.sort()
		parentSelectList.append(tempList[0])
		tempList = []
	return parentSelectList

### recombine parents and create child list in this method ###
def recombine(pList):
	childList = []
	global randCount
	for i in range(int(len(pList)/2)):
		if(randCount == len(randomList)):
			randCount=0
		index = math.ceil(float(randomList[randCount%len(randomList)])*len(weightList))-1
		randCount+=1	
		c1=pList[i][0][:index]+pList[i+1][0][index:]
		c2=pList[i+1][0][:index]+pList[i][0][index:]
		childList.append(c1)
		childList.append(c2)
	return childList

### mutation apply the child list and create mutation list in this method ### 
def mutation(cList):
	mutationList = []
	global randCount
	for i in range(len(childList)):
		for j in range(len(weightList)):
			if(randCount == len(randomList)):
				randCount=0
			if(float(randomList[randCount%len(randomList)]) < m):
				if(childList[i][j]=="0"):
					temp = list(childList[i])
					temp[j] = "1"
					childList[i] = "".join(temp)
				else:
					temp = list(childList[i])
					temp[j] = "0"
					childList[i] = "".join(temp)	
			randCount+=1					
		mutationList.append(childList[i])				
	
	return mutationList	

### choose the best childrens in this method ###
def survivorSelect(cList, pList):
	childEva = evaluate(cList)
	eva = list(childEva + pList)
	eva.sort(key=lambda srt: srt[1],reverse=True)

	return eva[:len(pList)]	

### main section ###
if __name__=='__main__':
	i = 0
	minList = []
	maxList = []
	avg = 0
	avgList = []
	itList = range(iteration)

	populationList=initialise()
	fitnessList=evaluate(populationList)

	while(i < iteration):
		avg = 0
		parentSelectedList = parentSelect(fitnessList)
		childList = recombine(parentSelectedList)	
		mutationList = mutation(childList)
		survivorList = survivorSelect(mutationList,fitnessList)

		for j in range(len(survivorList)):
			avg += int(survivorList[j][1])

		avgList.append(avg/len(survivorList))
		minList.append(min(survivorList,key=lambda srt: srt[1])[1])
		maxList.append(max(survivorList,key=lambda srt: srt[1])[1])
		fitnessList = survivorList	
		i += 1

	### display graphic for min, max and average values ###
	plt.plot(itList,minList,'o-',c='blue')
	plt.plot(itList,avgList,'s-',c='red')
	plt.plot(itList,maxList,'o-',c='brown')
	plt.grid(True)		
	plt.xlabel('Iterator')
	plt.ylabel('Fitness')
	plt.legend(["min","avg","max"])
	plt.show()
