import sys
sys.stdin = open('1208_flatten.txt')


for tc in range(1, 11):
    dump_num = int(input())
    box = list(map(int, input().split()))

    max_box = 0
    min_box = 101
    for i in box:

        if i > max_box:
            max_box = i
        if i < min_box:
            min_box = i


        if max_box != 101 and min_box != 0:
            idx_max = box.index(max_box)
            idx_min = box.index(min_box)
            box[idx_max] = max_box-1
            box[idx_min] = min_box + 1
            dump_num -= 1



        if max_box - min_box < 2:
            print(max_box - min_box)

        if dump_num == 0:
            print(max_box - min_box)