
# Part 2: Arrays & Strings (1 hr):

# isStringPermutation(s1: “asdf”, s2: “fsda”) == true
# isStringPermutation(s1: “asdf”, s2: “fsa”) == false
# isStringPermutation(s1: “asdf”, s2: “fsax”) == false


def isStringPermutation(s1: str, s2: str) -> bool:
    
    if len(s1) == len(s2):
         return True
     # check of both the length of the string are the same
     # count the character in both of the string
     # create a hashmap to keep track of count
     
    countS1, countS2 = {}, {}
     
    for i in range(len(s1)):
         # count the occurance character in str1 and str2
         
        countS1[s1[i]] = 1 + countS1.get(s1[i],0)
        countS2[s2[i]] = 1 + countS2.get(s2[i], 0)
         
    # iterate thru the hashamp key values
    for c in countS1:
        if countS1[c] != countS2.get(c, 0):
            return False
    return True 
     
    
# Driver Code
if __name__ == '__main__':
    s1 = "asdf"
    s2 = "fsda"
    if isStringPermutation(s1,s2):
        print("Yes")
    else:
        print("No")


"""
pairsThatEqualSum(...)

pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 5) == [(1, 4), (2, 3)]
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 1) == []
pairsThatEqualSum(inputArray: [1, 2, 3, 4, 5], targetSum: 7) == [(2, 5), (3, 4)]

"""
    
def pairsThatEqualSum(inputArray: list, targetSum: int) -> list:
    
    for i in range(len(inputArray))-1:
        for j in range(i + 1, len(inputArray)):
            
            if inputArray[i] + inputArray[j] == targetSum:
                print ('Pair found', (inputArray[i],inputArray[j]))
                

if __name__ == '__main__':
    inputArray = [1,2,3,4,5]
    targetSum = 5
    pairsThatEqualSum(inputArray,targetSum)
    
    