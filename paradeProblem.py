## The Parade Problem
#  Create the longest possible row of cards that do not break these rules:
#    1. If there exists a card of rank i and at position j there cannot be a card at positions >= j+i with rank >= i.
#    2. If there exists a card of rank i, at positions j and some type there cannot be a card of the same type at positions >= j+i of any rank.
import itertools
import collections
import copy
import os

os.chdir('c:/')
f = open('paradaProblemOutput.txt','w')
	
def validRow(row):
	# Input: row (list)
	# Output: True/false, if the row valid.
	if row.count(row[-1])>6:
		return False
	# for pos1 in xrange(len(row)):
		# for pos2 in range(pos1+row[pos1],len(row)):
			# if row[pos2] >= row[pos1]:
				# return False

	for pos in xrange(len(row)):
		if pos==0:
			sorts = [0]
		else:
			sort = checkLastRow(row[:pos+1],sorts)
			if sort != 6:
				sorts += [sort]
				# print "Sorts and row are:",sorts
				# print row
			else:
				return False
	# print "Sorts and row are:",sorts
	# print row
	return True

def checkLastRow(row,sorts):
	def checkRowForSort(row,checkSort):
		checkRow = row[-1]
		for pos1 in xrange(len(row)-1):
			for pos2 in xrange(len(row)-1):
				if checkSort == sorts[pos1] and pos1+row[pos1]<=pos2:
					return False
			if checkSort == sorts[pos1] and checkRow == row[pos1]:
				return False
		return True
	for sort in xrange(6):
		if checkRowForSort(row,sort):
			return sort
	return 6

def nextCards(row):
	# Input: row (list)
	# Output: list of new valid rows (list of lists)
	result = []
	for card in reversed(xrange(11)):
		temp = copy.deepcopy(row)
		temp.append(card)
		result.append(temp)
	newRows = [rows for rows in result if validRow(rows)]
	return newRows

def problemSolved(row):
	if row != False and len(row) >= condition and validRow(row):
		return True
	else:
		return False

def solveRow(row):
	if problemSolved(row):
		return row
	else:
		return solveRowList(nextCards(row))

def solveRowList(rowlist):
	if rowlist == []:
		return False
	else:
		check = solveRow(rowlist[0])
		if problemSolved(check):
			f.write("Problem solved!\n")
			f.write(','.join(str(e) for e in list(check))+'\n')
			return check
		else:
			return solveRowList(rowlist[1:])
			
row = [9]
condition = 17
print solveRow(row)
f.close()