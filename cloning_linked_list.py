class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        node_map={}
        curr=head
        while curr:
            node_map[curr]=Node(curr.val)
            curr=curr.next
        
        curr=head
        while curr:
            if curr.next:
                node_map[curr].next=node_map[curr.next]
            if curr.random:
                node_map[curr].random=node_map[curr.random]
            curr=curr.next
        return node_map[head]
