from zTest import zTest

def y_n(prompt="Answer yes or no\n"):
     while True:
         answer = input(prompt)
         if answer in ['y', 'Y', 'yes']:
             print ("You said yes!")
             break
         elif answer in ['n', 'N', 'no']:
             print ("You said no!")
             break
         else:
             print ("%s is an invalid answer."%answer)

zTest(["y", "n"])
y_n()
y_n()