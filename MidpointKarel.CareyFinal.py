"""
File: MidpointKarel.py
Name: Carey
耗時：5小時
日期：114.4.6
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""

from karel.stanfordkarel import *
from CollectNewspaperKarel import *


def main():
    """
    找出任何世界的street1中點
    """
# 1 第一輪去程、回程（只放不撿）
    put_one_ahead()
    while front_is_clear():
        move()
    turn_around_and_put_one_ahead()
    move()
    go_straight()
    """
     while front_is_clear():
        if not on_beeper():
            move()
        else:
            pick_beeper()
            turn_around_and_put_one_ahead()
    """

# 2 第一輪回程碰到beeper迴轉，進入第二輪去程，開始撿
    while front_is_clear():
        if on_beeper():
            pick_beeper()
            turn_around_and_put_one_ahead()
        else:
            go_straight()
    turn_around()

# 3 最後一步
    while not on_beeper():
        move()
    pick_beeper()


def put_one_ahead():
    """
    pre-condition:面東
    post-condition:往前（東）放一顆
    """
    move()
    put_beeper()


def turn_around_and_put_one_ahead():
    """
    走到撞牆或遇到beeper迴轉，並往前放一顆，再往前一步
    """
    turn_around()
    put_one_ahead()
    move()


def go_straight():
    """
    pre-condition:直線前進
    post-condition:走到撞牆或遇到beeper為止（迴轉）
    """
    while front_is_clear():
        if not on_beeper():
            move()
        else:
            pick_beeper()
            turn_around_and_put_one_ahead()





# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
