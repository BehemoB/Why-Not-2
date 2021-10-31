def is_monotonic(nums):
    P=[]
    P.extend(nums)
    O = []
    O.extend(nums)
    P.sort()
    O.reverse()
    if nums == P:
        return True
    elif P == O:
        return True
    else:
        return False
nums = []
print('Великое правило ввода: список ограничивать квадратными скобками, элементы писать без пробела и через запятую, иначе все сломается...')
nums = input('nums = ')
A = nums[1:-1]
S = (A.split(','))
i = iter(S)
L = list(iter(lambda: int(next(i)), None))
print(is_monotonic(L))
