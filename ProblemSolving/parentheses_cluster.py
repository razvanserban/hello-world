'''
Write a function that groups a string into parentheses cluster. Each cluster should be balanced.
'''

def groupCluster(parentheses):
    slicedParentheses = []
    parenthesesGroup = ''
    countOpen = 0
    countClose = 0

    for item in parentheses:
        parenthesesGroup = parenthesesGroup + item
        countOpen = parenthesesGroup.count('(')
        countClose = parenthesesGroup.count(')')
        if countOpen == countClose:
            slicedParentheses.append(parenthesesGroup)
            parenthesesGroup = ''

    return slicedParentheses

print(groupCluster('((()))(())()()(()())'))