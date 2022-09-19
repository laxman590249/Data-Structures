"""
You are given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends
at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. You can only attend one event at any time d.

Return the maximum number of events you can attend.

Input: events = [[1,2],[2,3],[3,4]]
Output: 3

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

"""

events = [[1,5],[1,5],[1,5],[2,3],[2,3]]

event = sorted(events, key=lambda x: x[1])
start = event[0][0]
end = event[len(event)-1][1]
print(event)

count_days = 0

for days in event:
    if start in range(days[0], days[1]+1):
        count_days += 1
    start += 1

print(count_days)