"""
You are given n activities with their start and finish times. Select the maximum number of activities that can be
performed by a single person, assuming that a person can only work on a single activity at a time.

Solution:

Sort it according to finish time
Pick every Activity and check the last end time was greater then or equal to it or not.

1) Sort the activities according to their finishing time
2) Select the first activity from the sorted array and print it.
3) Do the following for the remaining activities in the sorted array.
…….a) If the start time of this activity is greater than or equal to the finish time of the previously selected activity
 then select this activity and print it.
"""