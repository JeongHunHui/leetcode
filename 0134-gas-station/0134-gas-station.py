class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start, current_tank, total_tank = 0, 0, 0
        for i in range(len(gas)):
            use_amount = gas[i] - cost[i]
            current_tank += use_amount
            total_tank += use_amount
            if current_tank < 0:
                current_tank = 0
                start = i+1
        return start if total_tank >= 0 else -1