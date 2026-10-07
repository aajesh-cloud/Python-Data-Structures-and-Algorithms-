def can_finish(piles, h, speed):
    hours = 0
    for pile in piles:
        hours += (pile + speed - 1) // speed
    return hours <= h

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    answer = right

    while left <= right:
        mid = left + (right - left) // 2

        if can_finish(piles, h, mid):
            answer = mid     # It works! Save it.
            right = mid - 1  # Try to find an even smaller speed
        else:
            left = mid + 1   # Too slow. Must eat faster.

    return answer