# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            temp = []        
            for i in range(0,len(lists),2):
                if i+1<len(lists):
                    temp.append(self.mergelists(lists[i],lists[i+1]))
                else:
                    temp.append(lists[i])
            lists = temp
        return lists[0]

        
    def mergelists(self,list1,list2):
        dummy= head = ListNode()
        while list1 and list2:
            if list1.val<list2.val:
                head.next = list1
                list1 = list1.next
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        head.next = list1 or list2
        return dummy.next
            


        
        