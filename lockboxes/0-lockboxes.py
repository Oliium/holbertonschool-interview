#!/usr/bin/python3


def canUnlockAll(boxes):
    unlocked = set([0])
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if key < len(boxes) and key not in unlocked:
            unlocked.add(key)
            keys.extend(boxes[key])

    return len(unlocked) == len(boxes)
