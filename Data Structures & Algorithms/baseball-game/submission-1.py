class Solution:
    def calPoints(self, operations: List[str]) -> int:
        l = []
        for op in operations:
            if op == "C":
                l.pop()
            elif op == "D":
                l.append(l[-1] * 2)
            elif op == "+":
                l.append(l[-1] + l[-2])
            else:
                l.append(int(op))
        return sum(l)