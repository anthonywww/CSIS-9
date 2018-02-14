#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Program Name: split_sentence.py
# Anthony Waldsmith
# 07/27/16
# Python Version 3.4
# Description: Split a sentence and count the words in it

def countWord(words, word):
	count = 0
	for s in words:
		if word == s:
			count += 1
	return count

def requestSearchWord():
	word = input("Enter a word to search for: ")
	return word

def countWords(words):
	count = 0
	for i in words:
		count += 1
	return count

def getLastWord(words):
	return words[len(words)-1]

def splitSentence(text):
	return text.split(' ')

def requestSentance():
	text = input("Enter a sentence: ")
	return text

def main():
	text = requestSentance()
	words = splitSentence(text)
	count = countWords(words)
	lastword = getLastWord(words)
	print ("There are %i words in the sentence '%s'" %(count,text))
	print ("The last word is '%s'" %(lastword))
	searchword = requestSearchWord()
	searchcount = countWord(words, searchword)
	print ("The word '%s' appears %i times in the sentence" %(searchword,searchcount))

main()

"""'
Enter a sentence: the fox and the dog are friends
There are 7 words in the sentence 'the fox and the dog are friends'
The last word is 'friends'
Enter a word to search for: the
The word 'the' appears 2 times in the sentence
"""
