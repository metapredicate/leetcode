from copy import deepcopy

class Solution:        
    # Definition for singly-linked list.
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    def addTwoNumbers(self, l1, l2):
        def traverse_to_str(l1, init_str):
            mystr = deepcopy(init_str)
            mystr += (str(l1.val))
            if(l1.next):
                return traverse_to_str(l1.next, mystr)
            else:
                return mystr
        
        l1_int = int(traverse_to_str(l1, ""))
        l2_int = int(traverse_to_str(l2, ""))
        result_int = l1_int + l2_int
        
        def stringToListNode(stringTotal):
            previousNode = None
            first = None
            for i in stringTotal:
                currentNode = ListNode(i)
                if first is None:
                    first = currentNode
                if previousNode is not None:
                    previousNode.next = currentNode
                previousNode = currentNode
            return first
        
        return stringToListNode(str(result_int))
        
if __name__ == '__main__':
    foo = Solution()
    print("No good test case to put here. Damn leetcode smokescreen.")
