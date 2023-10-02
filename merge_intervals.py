def merge(intervals):
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        return stack

intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
intervals_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(merge(intervals))
print(merge(intervals_1))