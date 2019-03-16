# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        numbers = []
        for List in lists:
            while List:
                numbers.append(List.val)
                List = List.next

        if len(numbers) == 0:
            return None
        numbers.sort()

        head = ListNode(numbers[0])
        temp = head

        for number in numbers[1:]:
            node = ListNode(number)
            temp.next = node
            temp = node

        return head