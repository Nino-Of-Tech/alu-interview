#!/usr/bin/python3
def rain(walls):
    left, right = 0, len(walls) - 1
    left_max = right_max = total_water = 0
    while left < right:
        if walls[left] < walls[right]:
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total_water += (left_max - walls[left])
            left += 1
        else:
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total_water += (right_max - walls[right])
            right -= 1
    return total_water
