import time
import sys


def loading():
    basic_move = "\033[2000D"

    info_text = "Loading... "
    percent = "%"

    bar_lng = 50
    bar_s, bar_e = '[', '] '
    bar_l, bar_r = '#', ' '

    iter_obj = range(0, 100)
    step_curr, step_total = 0, len(iter_obj)
    for i in iter_obj:
        step_curr += 1
        bar_curr = bar_lng*step_curr//step_total
        bar = (bar_l*bar_curr)
        bar += bar_r * (bar_lng-bar_curr)
        bar = bar_s + bar + bar_e

        text_percent = f"{str(i+1):>3}" + percent

        output_text = bar + info_text + text_percent

        sys.stdout.write(basic_move+output_text)
        sys.stdout.flush()

        time.sleep(0.05)


loading()
