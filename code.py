class Solution:
  def findMaximizedCapital(k, W, Profit, Capital):
    heap, projects = [], sorted(zip(Profit, Capital), key=lambda x:x[1])
    i, n = 0, len(projects)
    for _ in range(k):
      while i < n and projects[i][1] <= W:
        heapq.heappush(heap, (-projects[i][0]))
        i += 1
      if heap: W -= heapq.heappop(heap)
      else: break
    return W
