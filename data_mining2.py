#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Optional import for versions of python <= 2
from __future__ import print_function

#name: get_data_list
#param: FILE_NAME  - the file's name you saved for the stock's prices
#brief: get a list of the stock's records' lists
#return: a list of lists
def get_data_list (FILE_NAME):
	f = open(FILE_NAME, "r")
	array = []
	for line in f:
		array += [line]
	f.close()
	return array


#name: get_monthly_averages
#param: data_list  - the list that you will process
#brief: get a list of the stock's monthly averages and their corresponding dates
#return: a list
# THIS COULD BE OPTIMIZED, HOWEVER THIS WAY MAKES A BIT MORE SENSE TO ME
def get_monthly_averages (data_list):
	monthly_average_list = []
	skippedHeader = False
	years = []
	months = []
	data = []

	# For each line of data ...
	for line in data_list:
		if skippedHeader == True:
			section = line.split(',')
			date = section[0].split('-')
			years += [date[0]]
			months += [date[1]]
			data += [str(date[0] + "," + date[1] + "," + date[2] + "," + section[6][:-1]).split(',')]

		else:
			skippedHeader = True

	print ("Processing ...")

	for year in years:
		for month in months:
			amount = 0
			count = 0

			for s in data:
				print (s[1])
				print (month)
				if s[1] == month:
					count += 1
					amount += float(s[3])

			average = (amount / count)
			print (average)
			monthly_average_list += [year + "," + month + "," + str(average)]

	return monthly_average_list


#name: print_info
#param: monthly_average_list  - the list that you will process
#brief: print the monthly averages of Google stock
#return: None
def print_info (monthly_average_list):
	# show monthly averages of Google stock
	index = 0
	for s in monthly_average_list:
		print("monthly_average_list [%i]\t=\t%s" %(index,s))
		index +=1



def main():
	data_list = get_data_list("table.csv")
	monthly_average_list = get_monthly_averages(data_list)
	print_info(monthly_average_list)


main()

