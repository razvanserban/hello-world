'''
A city skyline can be represented as a 2-D list with 1s representing buildings. In the example below, the height of the tallest building is 4 (second-most right column).

[[0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 1, 0],
[0, 0, 1, 0, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1]]

Create a function that takes a skyline (2-D list of 0's and 1's) and returns the height of the tallest skyscraper.
'''

def tallestSkyscraper(twoDList):
    #create a list to store results
    resultList = []
    for item in twoDList[0]:
        resultList.append(0)

    #iterare trugh given building list and get the results
    for list in twoDList:
        position = 0
        for item in list:
            resultList[position] = int(resultList[position]) + item
            position += 1

    #get the highest element in the result list
    compare = 0
    for item in resultList:
        if item > compare:
            compare = item
    return(compare)

print(tallestSkyscraper([
  [0, 0, 0, 0],
  [0, 0, 0, 0],
  [1, 1, 1, 0],
  [1, 1, 1, 1]
]))