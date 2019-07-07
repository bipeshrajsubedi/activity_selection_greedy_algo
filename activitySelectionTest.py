import unittest
import activitySelection

#Start and Finish time are sorted
stTime = [1, 3, 0, 5, 8, 5]
finTime = [2, 4, 6, 7, 9, 9]
sizeArray = len(stTime)
expectedOutcome = ["A0","A1","A3","A4"]

class TestActivitySelection(unittest.TestCase):
    def testActivity(self):
        testResultIterative = activitySelection.IterativeActivitySelection(stTime,finTime,sizeArray)
        self.assertListEqual(testResultIterative,expectedOutcome)
        testResultRecursive = activitySelection.RecursiveActivitySeletion(stTime,finTime,-1,sizeArray)
        self.assertListEqual(testResultRecursive,expectedOutcome)

