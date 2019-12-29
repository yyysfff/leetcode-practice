class ListNode(object):
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1==None:
            return l2
        if l2==None:
            return l1
        q=ListNode(0)
        p=ListNode(0)
        if l1.val>l2.val:
            q=l1
            l1=l2
            l2=q
        head=l1
        p=l1.next
        while(l2!=None and l1!=None):
            if p==None:
                l1.next=l2
                return head
            elif l2.val>p.val:
                l1=p
                p=l1.next
            else:
                q=l2
                l2=l2.next
                l1.next=q
                q.next=p
                l1=q
        if l1==None:
            l1.next=l2
        return head

list1=[1,2,4]
list2=[1,3,4]

l1_head=ListNode(list1[0])
l1=l1_head
for i in range(1,len(list1)):
    q = ListNode(list1[i])
    l1.next=q
    l1=l1.next
l2_head=ListNode(list2[0])
l2=l2_head
for i in range(1,len(list2)):
    q = ListNode(list2[i])
    l2.next=q
    l2=l2.next


S=Solution()
S.mergeTwoLists(l1_head,l2_head)
l1=l1_head
while(l1!=None):
    print(l1.val,"->",end='')
    l1=l1.next