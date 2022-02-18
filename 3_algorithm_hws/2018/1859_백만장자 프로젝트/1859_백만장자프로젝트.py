import sys; sys.stdin = open('1859_백만장자프로젝트.txt')

t = int(input())
for tc in range(1, t + 1):
    days = int(input())
    price = list(map(int, input().split()))

    # for i in range(days, -1):
    #     add = 0
    #     for j in range(i):
    #         if price[i - (days-1)] <price[j]:
    #             add += price[j] - price[i - (days - 1)]
    #         print(add)



    count = 0
    money = 0
    profit = 0
    for i in range(days - 1):
        if price[i] <= price[i + 1]:
            count += 1
            money += price[i]

        elif price[i] > price[i + 1]:
            profit += (price[i] * count) - money

    print(profit)

