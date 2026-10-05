class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        leftToRightVals = []
        rightToLeftVals = []
        tracker = head
        while tracker is not None:
            leftToRightVals.append(tracker.val)
            rightToLeftVals.insert(0,tracker.val)
            tracker = tracker.next
        # Your code goes here
        if len(leftToRightVals) == 0:
            return True
        for i in range(len(leftToRightVals)):
            if leftToRightVals[i] != rightToLeftVals[i]:
                return False
        return True