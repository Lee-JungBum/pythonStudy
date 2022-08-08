'''
graph : bfs(너비우선탐색) ->최단 경로 -> dijkstra(우선순위큐)
'''
# que = []
# que.append(100)
# que.append(200)
# que.append(300)
# print(que)
# print(que)
# print('pop :',que.pop(0))
# print(que)


# from queue import Queue,PriorityQueue
# q= Queue()
# q.put(100)
# q.put(200)
# q.put(300)


# from collections import deque
# dq = deque()
# dq.append(100)
# dq.append(200)
# print(dq)
# dq.appendleft(300)
# print(dq)
#
# print('pop :',dq.pop())
# print(dq)
# print('pop: ',dq.popleft())
# print(dq)

#우선순위큐 == heapTree를 기점으로 만듬
#python -> 작은값 먼저나옴
from queue import PriorityQueue
pq = PriorityQueue()
# pq.put(3)
# pq.put(2)
# pq.put(8)
# pq.put(1)
# while not pq.empty():
#     print(pq.get())
pq.put((2,100))
pq.put((3,300))
pq.put((1,500))
pq.put((4,400))
while not pq.empty():
    print(pq.get())