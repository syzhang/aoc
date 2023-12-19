"""
day 19
"""
from typing import NamedTuple
from utils import get_input


def get_parts_rules(data):
    """get parts and procs"""
    rules = data.split("\n\n")[0]
    parts = data.split("\n\n")[1]
    return parts, rules


def rules_functions(rules):
    """turn rules into functions"""
    rules_dict = {}
    for r in rules.split("\n"):
        name, rule = r.split("{")
        name = name.strip()
        rule = rule.strip("}").strip()
        rules_dict[name] = rule
    return rules_dict


def accept(part, rules_dict):
    """judge if part is accepted"""
    state = "in"
    while True:
        rule = rules_dict[state]
        for r in rule.split(","):
            if not r:
                continue
            applies = True
            result = r
            if ":" in r:
                condition, result = r.split(":")
                condition = condition.strip()
                var = condition[0]
                operation = condition[1]
                num = int(condition[2:])
                if operation == "=":
                    applies = part[var] == num
                elif operation == "<":
                    applies = part[var] < num
                elif operation == ">":
                    applies = part[var] > num
                else:
                    print("error")
            if applies:
                if result == "A":
                    return True
                elif result == "R":
                    return False
                state = result
                break


def loop_parts(parts, rules_dict):
    """loop through parts"""
    accepted_sum = 0
    for part in parts.split("\n"):
        if not part:
            continue
        part = part.strip("{}")
        # get part number
        part = {x.split("=")[0]: int(x.split("=")[1]) for x in part.split(",")}
        if accept(part, rules_dict):
            accepted_sum += part["x"] + part["m"] + part["a"] + part["s"]
    print(accepted_sum)


class RangePart(NamedTuple):
    # https://github.com/Evgenus/advent-of-code/blob/main/2023/19/main.py
    x: range
    m: range
    a: range
    s: range

    @property
    def size(self):
        return len(self.x) * len(self.m) * len(self.a) * len(self.s)

    def _apply(self, func, name: str, value: int):
        # apply func to name
        a, b = self._asdict(), self._asdict()
        a[name], b[name] = func(a[name], value)
        return RangePart(**a), RangePart(**b)

    def apply_less(self, name: str, value: int):
        return self._apply(apply_less, name, value)

    def apply_more(self, name: str, value: int):
        return self._apply(apply_more, name, value)


def apply_less(r: range, value: int):
    if r.start > value:
        return range(0), r
    if r.stop > value:
        return range(r.start, value), range(value, r.stop)
    return r, range(0)


def apply_more(r: range, value: int):
    if r.stop < value:
        return range(0), r
    if r.start <= value:
        return range(value + 1, r.stop), range(r.start, value + 1)
    return r, range(0)


def part_b(rules):
    def run(part: RangePart, name):
        if part.size == 0:
            return 0
        if name == "A":
            return part.size
        if name == "R":
            return 0
        result = 0
        for rule in rules[name].split(","):
            if ":" in rule:
                condition, target = rule.split(":")
                if ">" in condition:
                    name, value = condition.split(">")
                    a, part = part.apply_more(name, int(value))
                    result += run(a, target)
                elif "<" in condition:
                    name, value = condition.split("<")
                    a, part = part.apply_less(name, int(value))
                    result += run(a, target)
                else:
                    assert 0, rule
            else:
                result += run(part, rule)
        return result

    return run


def task_b(rules_dict):
    part = RangePart(
        x=range(1, 4001),
        m=range(1, 4001),
        a=range(1, 4001),
        s=range(1, 4001),
    )

    run = part_b(rules_dict)

    return run(part, "in")


# main
if __name__ == "__main__":
    # get input
    # input = get_input(day=19, test_data=True)
    input = get_input(day=19, test_data=False)
    # part a
    parts, procs = get_parts_rules(input)
    rules = rules_functions(procs)
    # loop_parts(parts, rules)
    # part b
    output = task_b(rules)
    print(output)
