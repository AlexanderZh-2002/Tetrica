def appearance(intervals: dict[str, list[int]]) -> int:
    pup, tut = preprocess(intervals)
    res = 0
    for p in pup:
        for t in tut:
            res += intersect(p,t)
    return res

def sort_fn(element):
    return element[0]

def merge_intervals(arr, beg, end):
    flag = True
    while flag:
        flag = False
        for i in range(len(arr)):
            if arr[i][0] > end or arr[i][1] < beg:
                flag = True
                del arr[i]
                break
            if arr[i][0] < beg:
                arr[i] = (beg, arr[i][1])
            if arr[i][1] > end:
                arr[i] = (arr[i][0], end)
            if (i<len(arr)-1) and (arr[i][1] >= arr [i+1][0]):
                flag = True
                arr[i] = (arr[i][0], max(arr[i][1], arr[i+1][1]))
                del arr[i+1]
                break
    return arr

def preprocess(intervals):
    pup = list(zip(intervals['pupil'][::2], intervals['pupil'][1::2]))
    pup.sort(key = sort_fn)
    pup = merge_intervals(pup, intervals['lesson'][0], intervals['lesson'][1])
    #print(pup)

    tut = list(zip(intervals['tutor'][::2], intervals['tutor'][1::2]))
    tut.sort(key = sort_fn)
    tut = merge_intervals(tut, intervals['lesson'][0], intervals['lesson'][1])
    #print(tut)
    
                    
    return pup, tut

def intersect(p, t):
    return max((min(p[1],t[1]) - max(p[0],t[0])), 0)



tests = [
    {'intervals': {'lesson': [1594663200, 1594666800],
             'pupil': [1594663340, 1594663389, 1594663390, 1594663395, 1594663396, 1594666472],
             'tutor': [1594663290, 1594663430, 1594663443, 1594666473]},
     'answer': 3117
    },
    {'intervals': {'lesson': [1594702800, 1594706400],
             'pupil': [1594702789, 1594704500, 1594702807, 1594704542, 1594704512, 1594704513, 1594704564, 1594705150, 1594704581, 1594704582, 1594704734, 1594705009, 1594705095, 1594705096, 1594705106, 1594706480, 1594705158, 1594705773, 1594705849, 1594706480, 1594706500, 1594706875, 1594706502, 1594706503, 1594706524, 1594706524, 1594706579, 1594706641],
             'tutor': [1594700035, 1594700364, 1594702749, 1594705148, 1594705149, 1594706463]},
    'answer': 3577
    },
    {'intervals': {'lesson': [1594692000, 1594695600],
             'pupil': [1594692033, 1594696347],
             'tutor': [1594692017, 1594692066, 1594692068, 1594696341]},
    'answer': 3565
    },
]

if __name__ == '__main__':
    for i, test in enumerate(tests):
       test_answer = appearance(test['intervals'])
       assert test_answer == test['answer'], f'Error on test case {i}, got {test_answer}, expected {test["answer"]}'
    print("done")

