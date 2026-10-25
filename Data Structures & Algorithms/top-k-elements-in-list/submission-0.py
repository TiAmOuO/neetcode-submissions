class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        for n in nums:
            count[n] = count.get(n, 0) +1
#        ranked = sorted(count, key=count.get, reverse=True)
#        return ranked[:k]

        # 第 2 步：建格子，把數字放進對應次數的格子
        buckets = [[] for n in range(len(nums) + 1)]
        for num, freq in count.items():
            buckets[freq].append(num)

        # 第 3 步：從次數最多的格子開始拿，拿滿 k 個就回傳
        result = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result)==k:
                    return result