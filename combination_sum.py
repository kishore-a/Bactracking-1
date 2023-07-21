#

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int],
                       target: int) -> List[List[int]]:
        result = []
        Solution.helper(candidates, 0, target, result,path=[])
        return result

    def helper(candidates, idx, target, result,path):
        
        if (idx == len(candidates) or target < 0):
            return
        #Base Case#
        if (target == 0):
            result.append(path[:])
            return
        #Not Choose
        Solution.helper(candidates, idx + 1, target, result,path)
        path.append(candidates[idx])
        Solution.helper(candidates, idx, target - candidates[idx], result,path)
        path.pop(len(path)-1)


candidates = [2, 3, 6, 7]
target = 7
obj = Solution()
print(obj.combinationSum(candidates, target))
