from typing import Iterable, Union
import os


def pbar(
        iter: Iterable,
        total: Union[int, None] = None,
        max_width: Union[int, None] = None,
        desc: Union[str, None] = None
        ) -> Iterable:

    if total is None:
        try:
            total = len(iter)
        except TypeError:
            total = None

    desc_len = len(desc) if desc is not None else 0
    if max_width is None:
        max_width = os.get_terminal_size().columns - (2 * len(str(total))) - 4
        if desc is not None:
            max_width -= len(desc) + 2

    assert total is None or total > 0, "Total must be greater than 0 or None"

    for i, item in enumerate(iter):
        if desc is not None:
            print(f"{desc}: ", end="")

        if total is not None:
            bricks = '█' * int((i / total) * max_width + 1)
            spaces = ' ' * (max_width - len(bricks))
            left_pad = ' ' * (len(str(total)) - len(str(i + 1)))
            print(f"{left_pad}{i + 1}/{total} |{bricks}{spaces}|", end="\r")
        else:
            print(f"{i + 1}/?", end="\r")
        yield item

    print()


if __name__ == "__main__":
    import time
    entries = 100
    time_epsilon = 0.01

    def defualt_test():
        print("Testing with no parameters")
        for i in pbar(range(entries)):
            time.sleep(time_epsilon)

    def intended_usage():
        print("Testing intended usage")
        for i in pbar(range(entries), desc="Loading"):
            time.sleep(time_epsilon)

    def total_entries():
        print("Testing with total=entries")
        for i in pbar(range(entries), desc="Loading", total=entries):
            time.sleep(time_epsilon)

    def none_total():
        print("Testing with total=None")
        for i in pbar(range(entries), desc="Loading", total=None):
            time.sleep(time_epsilon)

    def none_desc():
        print("Testing with width=80")
        for i in pbar(range(entries), total=entries, max_width=50):
            time.sleep(time_epsilon)

    def none_width():
        print("Testing with width=None")
        for i in pbar(range(entries), desc="Loading", total=entries, max_width=None):
            time.sleep(time_epsilon)

    def bad_iterable():
        print("Testing with bad iterable")

        def _bad_range():
            for i in range(entries):
                yield i

        bad_iterable = _bad_range()

        for i in pbar(bad_iterable, desc="Loading"):
            time.sleep(time_epsilon)

    def run_tests():
        intended_usage()
        defualt_test()
        total_entries()
        none_total()
        none_desc()
        none_width()
        bad_iterable()

    run_tests()
