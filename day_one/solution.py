def _next_pos(curr_pos, inst):
    d = -1 if inst[0] == 'L' else 1
    m = int(inst[1:])      
    new_pos = (curr_pos + (d * m))    
    ret_pos = new_pos % 100
    diff = new_pos // 100
    return ret_pos, diff

def _read_input():
    with open('input.txt', 'r') as fp:
        inst_list = fp.readlines()
    return inst_list

def solution_one():
    count = 0
    curr_pos = 50
    for inst in _read_input():
        curr_pos, _ = _next_pos(curr_pos, inst.strip())
        count += (curr_pos == 0)
    return count

def solution_two():
    count = 0
    curr_pos = 50
    for inst in _read_input():
        prev_turn_zero = (curr_pos == 0)
        curr_pos, diff = _next_pos(curr_pos, inst.strip())
        curr_turn_zero = (curr_pos == 0)
        clean_count = curr_turn_zero
        if diff < 0:
            clean_count += abs(diff) - prev_turn_zero
        elif diff > 0:
            clean_count += diff - curr_turn_zero
        
        clean_count = max(clean_count, 0)
        count += clean_count

    return count

if __name__ == "__main__":
    print(f"{solution_one()=}")
    print(f"{solution_two()=}")

