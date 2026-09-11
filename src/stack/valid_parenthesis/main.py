class Solution:
    def isValid(self, s: str) -> bool:
        tracker = []
        chararray = list(s)
        for i in chararray:
            match i:
                case "{":
                    tracker.append(i)
                case "(":
                    tracker.append(i)
                case "[":
                    tracker.append(i)
                case "}":
                    if len(tracker) == 0:
                        return False
                    if tracker.pop() != "{":
                        return False
                case ")":
                    if len(tracker) == 0:
                        return False
                    if tracker.pop() != "(":
                        return False
                case "]":
                    if len(tracker) == 0:
                        return False
                    if tracker.pop() != "[":
                        return False
        if len(tracker) != 0:
            return False
        return True