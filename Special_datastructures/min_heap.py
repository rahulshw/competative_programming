from typing import List


class minHeap:

    def __init__(self, l: List[int]):
        self.list = []
        self.size = 0
        for i in l:
            self.list.append(i)
            self.size += 1
            self.heapifyUp()

    def pop(self):
        val = self.list[0]
        self.size -= 1
        self.list[0] = self.list.pop()
        self.heapifyDown()
        return val

    def getParentIndex(self, index):
        if index % 2 != 0 : # odd --> left node
            return (index - 1)//2
        else: # even --> right node
            return (index - 2)//2

    def getLeftIndex(self, index):
        return 2*index + 1

    def getRightIndex(self, index):
        return 2*index + 2

    def swap(self, index1, index2):
        tmp = self.list[index1]
        self.list[index1] = self.list[index2]
        self.list[index2] = tmp

    def heapifyUp(self):
        index = self.size - 1
        parent_index = self.getParentIndex(index)
        while index != 0 and self.list[index] < self.list[parent_index]:
            self.swap(index, parent_index)
            index = self.getParentIndex(index)
            parent_index = self.getParentIndex(index)

    def heapifyDown(self):
        if not self.list:
            return
        index = 0
        left_index = self.getLeftIndex(index)
        right_index = self.getRightIndex(index)
        while left_index < self.size and self.list[index] > self.list[left_index]:
            if right_index < self.size:
                if self.list[left_index] < self.list[right_index]:
                    self.swap(index, left_index)
                    index = left_index
                else:
                    self.swap(index, right_index)
                    index = right_index
            else:
                self.swap(index, left_index)
                index = left_index

            left_index = self.getLeftIndex(index)
            right_index = self.getRightIndex(index)


if __name__ == '__main__':
    l = [3,4,2,1,5,7]
    heap = minHeap(l)
    print(heap.list)
    heap.pop()
    print(heap.list)
