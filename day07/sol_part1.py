#!/bin/python3


def contains(bag1, bag2, contains_bag):
    if len(contains_bag.items()) == 0:
        return False
    else:
        for bag in contains_bag[bag1]:
            if bag == bag2 or contains(bag, bag2, contains_bag):
                return True

        return False


with open("input.txt") as f:

    contains_bag = dict()
    for line in f:
        line = line.strip("\n").split(" ")
        line[-1] = line[-1][:-1]  # remove period from last word
        line[2] = line[2][:-1]  # remove "s" from third word
        bag1 = " ".join([line[0], line[1], line[2]])

        if bag1 not in contains_bag:
            contains_bag[bag1] = dict()

        if line[-3] != "no":

            for bag2 in " ".join(line[4:]).split(", "):
                bag2 = bag2.split(" ")
                count = int(bag2[0])
                if bag2[-1][-1] == 's':
                    bag2[-1] = bag2[-1][:-1]
                bag2 = " ".join(bag2[1:])
                if bag2 not in contains_bag[bag1]:
                    contains_bag[bag1][bag2] = count
                else:
                    contains_bag[bag1][bag2] += count

    contains_count = sum([1 for bag in contains_bag if contains(bag, "shiny gold bag", contains_bag)])
    print(contains_count)
