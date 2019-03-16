"""
The idea is to keep on merging the lists pairwise till the end pointer reaches start of list
and then return the list from the first index. The complexity becomes nkLog(n) which is less than n^2
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeLists(self, NodeA, NodeB):
        if not NodeA:
            return NodeB
        if not NodeB:
            return NodeA

        if NodeA.val < NodeB.val:
            head = NodeA
            NodeA = NodeA.next
        else:
            head = NodeB
            NodeB = NodeB.next

        temp = head
        while NodeA and NodeB:
            if NodeA.val < NodeB.val:
                temp.next = NodeA
                temp = NodeA
                NodeA = NodeA.next
            else:
                temp.next = NodeB
                temp = NodeB
                NodeB = NodeB.next

        if not NodeA:
            while NodeB:
                temp.next = NodeB
                temp = NodeB
                NodeB = NodeB.next
        else:
            while NodeA:
                temp.next = NodeA
                temp = NodeA
                NodeA = NodeA.next

        temp.next = None

        return head

    def printList(self, head):
        while head:
            print(str(head.val) + "->")
            head = head.next
        print("None")

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        end = len(lists) - 1

        while end != 0:
            i = 0
            j = end
            while i < j:
                lists[i] = self.mergeLists(lists[i], lists[j])
                i += 1
                j -= 1
                if i >= j:
                    end = j
                    break

        return lists[0]
