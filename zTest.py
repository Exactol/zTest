import inspect

#index of test input
index = -1
testStrings = []
originalInput = input
raiseExceptionOnTestFinished = False
callingModule = None

#Input override to simulate input at index of test string
def testInput(printStr):
    print(printStr)

    global index
    index += 1

    #If out of index, return control to user
    if (index > len(testStrings) - 1):
        callingModule.input = originalInput
        print("{:->30}".format("-"), "Out of test cases, returning to user input", "{:->30}".format("-\n"))

        #Either raise exception or return empty string
        if (raiseExceptionOnTestFinished):
            callingModule.input = originalInput
            raise Exception("Out of test cases, returning to user input")
        else:
            retStr = input()
            return(retStr)
    else:
        print("-Test:", testStrings[index])
        #Returning string is equivilent of user input
        return testStrings[index]

class zTest:
    def __init__(self, testStrs, raiseException = False):
        #Get calling module by inspecting the parent frame of calling function
        global callingModule
        callingModule = inspect.getmodule(inspect.stack()[1][0])

        #Override calling function's input function
        callingModule.input = testInput
        
        global testStrings
        testStrings = testStrs

        global raiseExceptionOnTestFinished
        raiseExceptionOnTestFinished = raiseException