# 미로 탈출 알고리즘 중 우수법 사용

# 이동 중 우회전 가능한 경우, 우회전 후 전진
# 우회전이 불가능하면, 직진 여부 확인 후 직진
# 직진 불가능한 경우, 좌회전 후 다시 이동 시도
# 세방향 모두 막혀 있으면 뒤로 후퇴 다만 바라보는 방향은 유지

def turn_right():
    for _ in range(3):
        turn_left()

def turn_around():
    for _ in range(2):
        turn_left()
    move()
    for _ in range(2):
        turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()
    else:
        turn_around()

        


