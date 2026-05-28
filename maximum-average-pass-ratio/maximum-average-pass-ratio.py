import heapq

class Solution:

    def calculate_gain(self, pass_, total):
        return (pass_ + 1)/(total + 1) - (pass_/total)

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        # there are n classes with pass, total of each class.
        # and extrastudents who 100% pass.
        # need to distribute it across the different classes where we get max averrage pass ratio.

        # Find the lowest performing classes. add them in min heap.

        # we need heap, but max heap along the gain in passing ratio when we increase the student in that class

        avg = 0.0 
        classheap = []
        for pass_, total in classes:
            # heapq.heappush(classheap, (self.calculate_gain(pass_, total) * -1, pass_, total))
            classheap.append((self.calculate_gain(pass_, total) * -1, pass_, total))
            avg += pass_/total

        heapq.heapify(classheap)
        
        for _ in range(extraStudents):

            gain, pass_, total = heapq.heappop(classheap)

            gain *= -1 
            
            avg += gain#(pass_/total)
            pass_ += 1
            total += 1

            pass_ratio = pass_/total
            # avg += pass_ratio

            heapq.heappush(classheap, (self.calculate_gain(pass_, total) * -1, pass_, total))
        # avg_ = 0.0

        # for pass_ratio, _ in classheap:
        #     avg_ += pass_ratio
        
        return avg/len(classes)
