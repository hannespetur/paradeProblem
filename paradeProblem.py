import copy
import os

def nextCards(row,uniqueSorts,lengd):
	# Input: row (list), uniqueSorts (int) and lengd (int)
	# Output: list of new valid rows (list of lists)
	resultRow = []
	resultUniqueSorts = []
	lengd += 1
	for sort in xrange(0,min(100*(uniqueSorts+1),600),100):
		for card in reversed(xrange(11)):
			temp = copy.deepcopy(row)
			temp.append(card+sort)
			if card+sort not in set(row) and validRow(temp,lengd):
				resultRow.append(temp)
				if sort > ((uniqueSorts-1)*100):
					resultUniqueSorts.append(uniqueSorts+1)
				else:
					resultUniqueSorts.append(uniqueSorts)
	return resultRow, resultUniqueSorts, lengd

def validRow(row,lengd):
	checkRow = row[-1]
	checkSort, checkRank = splitRow(checkRow)
	for i in xrange(lengd-1):
		compareRow = row[i]
		compareSort, compareRank = splitRow(compareRow)
		if compareRank+i < lengd-1:
			if compareSort == checkSort or compareRank <= checkRank:
				return False
	return True

def splitRow(row):
	sort = row/100
	rank = row-100*sort
	return sort, rank
	
def solveRow(row,uniqueSorts,lengd):
	if problemSolved(row,uniqueSorts,lengd):
		return row,uniqueSorts,lengd
	else:
		newRows, resultUniqueSorts, newlengd = nextCards(row,uniqueSorts,lengd)
		return solveRowList(newRows,resultUniqueSorts,newlengd)
	
def problemSolved(row,uniqueSorts,lengd):
	global condition
	if row != False and len(row) >= condition and validRow(row,lengd):
		condition = len(row)
		f.write(str(lengd)+' '+str(row)+'\n')
	return False

def solveRowList(rowlist,uniqueSortslist,lengd):
	if rowlist == []:
		return False, 0, 0
	else:
		checkRow, checkSorts, checkLengd = solveRow(rowlist[0],uniqueSortslist[0],lengd)
		if problemSolved(checkRow,checkSorts,checkLengd):
			f.write("Problem solved!\n")
			f.write(','.join(str(e) for e in list(checkRow))+'\n')
			return checkRow, checkSorts, checkLengd
		else:
			return solveRowList(rowlist[1:], uniqueSortslist[1:], lengd)

os.chdir('c:/')
f = open('paradaProblemOutput.txt','w')
row = []
uniqueSorts = len(list(set([el/100 for el in row])))
condition = 20
lengd = len(row)
print solveRow(row,uniqueSorts,lengd)
f.close()