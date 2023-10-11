n = int(input())
def get_position(count_step):
    x, y, dx, dy, count_stp, cur_stp = 0, 0, 1, 1, 1, 0
    for k in range(1, count_step+1):
        dx = -dx
        for i in range(count_stp):
            x += dx
            cur_stp += 1
            if cur_stp >= count_step:
                return f"{x},{y}"
        dy = -dy
        for i in range(count_stp):
            y += dy
            cur_stp += 1
            if cur_stp >= count_step:
                return f"{x},{y}"
        count_stp += 1
    return "0,0"
print(get_position(n))