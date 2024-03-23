#복습
import heapq
import sys
input=sys.stdin.readline

def dual_priority_queue(operations):
    min_heap, max_heap = [], []
    entry_finder = {}
    counter = 0

    for operation in operations:
        if operation[0] == 'I':
            num = int(operation[1])
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
            entry_finder[num] = entry_finder.get(num, 0) + 1
            counter += 1
        elif counter > 0:
            if operation[1] == '1':
                while max_heap:
                    num = -heapq.heappop(max_heap)
                    if entry_finder[num] > 0:
                        entry_finder[num] -= 1
                        counter -= 1
                        break
            else:
                while min_heap:
                    num = heapq.heappop(min_heap)
                    if entry_finder[num] > 0:
                        entry_finder[num] -= 1
                        counter -= 1
                        break

    if counter > 0:
        while max_heap:
            max_val = -heapq.heappop(max_heap)
            if entry_finder[max_val] > 0:
                break

        while min_heap:
            min_val = heapq.heappop(min_heap)
            if entry_finder[min_val] > 0:
                break

        return f"{max_val} {min_val}"
    else:
        return "EMPTY"

T = int(input())
for _ in range(T):
    k = int(input())
    operations = [input().split() for _ in range(k)]
    print(dual_priority_queue(operations))