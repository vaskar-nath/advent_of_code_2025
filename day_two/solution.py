def _read_input():
    with open('input.txt', 'r') as fp:
        s = fp.readlines()[0]
    return [x.split('-') for x in s.split(',')]

def _find_all_invalid_ids(start, end):
    ret = 0
    for i in range(start, end + 1):
        si = str(i)
        l = len(si)
        if l % 2 == 0 and si[:l//2] == si[l//2:]:
            ret += int(si)
    return ret

def _find_all_invalid_ids_two(start, end):
    ret = 0
    for i in range(start, end + 1):
        si = str(i)
        l = len(si)
        for k in range(1, l):
            if l % k == 0:
                is_not_valid = True
                start_entry = None
                for t in range(0, l//k):
                    curr_entry = si[t*k:(t+1)*k]
                    if start_entry == None:
                        start_entry = curr_entry
                    else:
                        if start_entry != curr_entry:
                            is_not_valid = False
                            break
                if is_not_valid:
                    ret += int(si)
                    break
    return ret


def solution_one():

    ans = 0
    for entry in _read_input():
        ans += _find_all_invalid_ids(int(entry[0]), int(entry[1]))
    return ans

def solution_two():

    ans = 0
    for entry in _read_input():
        ans += _find_all_invalid_ids_two(int(entry[0]), int(entry[1]))
    return ans
    


if __name__ == "__main__":
    print(f"{solution_one()=}")
    print(f"{solution_two()=}")