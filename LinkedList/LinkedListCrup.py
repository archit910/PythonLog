# Node Class
class Node:

	#Constructor 
	def __init__(self,data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None
		self.tail = None

	def push(self,Node):
		if not self.head and not self.tail:
			self.head = self.tail = Node
		else:
			self.tail.next = Node
			self.tail = Node
	
	def traverse(self):
		current_node = self.head
		while(current_node):
			print current_node.data,
			current_node = current_node.next
			
	def insert_after(self, req_data , data):
		req_node = self.head
		while(req_node):
			if req_node.data == req_data:
				break
			req_node = req_node.next
		if req_node:
			node = Node(data)
			node.next = req_node.next
			req_node.next = node

	def delete_node(self, key):
		prev_node = current_node = self.head

		while(current_node):
			if current_node.data == key:
				break
			prev_node = current_node
			current_node = current_node.next

		#head node
		if prev_node == current_node:
			self.head = self.head.next
			prev_node = current_node = None
		else:
			prev_node.next = current_node.next
			current_node = None

	def count_node_R(self, node):
		if node == None:
			return 0
		else:
			return 1 + self.count_node_R(node.next)

	def count_node(self):
		return self.count_node_R(self.head)
	
	def get_middle(self):
		prev_node = current_node = self.head
		while(current_node.next):
			prev_node = prev_node.next
			current_node = current_node.next
			if current_node:
				current_node = current_node.next
		return prev_node

			
	def get_count_integer(self, data):
		return self.get_count_check
		 
# The main function
if __name__ == "__main__":
	l_list = LinkedList()
	n1 = Node(1)
	n2 = Node(2)
	n3 = Node(3)
	l_list.push(n1)
	l_list.push(n2)
	l_list.push(n3)
	l_list.insert_after(2,4)
	l_list.insert_after(3,5)
	l_list.traverse()
	mid_node = l_list.get_middle()
	print '\n' , l_list.count_node()
	print '\n' , mid_node.data
 
