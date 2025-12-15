START_POS = 50
INPUT_FILE = 'input.txt'


def _next_pos(curr_pos, inst):
    if inst[0] == 'L':
        direction = -1
    else:
        direction = 1
    
    magnitude = int(inst[1:])
    count = 0
    if direction == -1:
        for _ in range(magnitude):
            curr_pos -= 1
            count += (curr_pos % 100 == 0)
    else:
        for _ in range(magnitude):
            curr_pos += 1
            count += (curr_pos % 100 == 0)
            
    return curr_pos, count

def main():
    with open(INPUT_FILE, 'r') as fp:
        inst_list = fp.readlines()
    count = 0
    curr_pos = START_POS
    prev_turn_zero = 0
    for inst in inst_list:
        curr_pos, ct = _next_pos(curr_pos, inst.strip())


        count += ct
    print(f"Answer is {count}")

if __name__ == "__main__":
    main()



    # if prev_turn_zero:
    #     if old_sig_dig > new_sig_dig:
    #         clean_count = old_sig_dig - new_sig_dig - 1
    #     elif old_sig_dig < new_sig_dig:
    #         clean_count = new_sig_dig - old_sig_dig - curr_turn_zero
    # else:
    #     if old_sig_dig > new_sig_dig:
    #         clean_count = old_sig_dig - new_sig_dig
    #     elif old_sig_dig < new_sig_dig:
    #         clean_count = new_sig_dig - old_sig_dig - curr_turn_zero