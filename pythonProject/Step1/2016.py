def solution(a, b):
    week = ("THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED")
    days = (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    day = 0
    for i in range(0, a-1):
        day += days[i]
    answer = week[(day+b)%7]
    return answer