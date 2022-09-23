# def add(*args):
#     total = []
#     for n in args:
#         total.append(n)
#     print(sum(total))
#
#
# add(1,2,3,45,454,6,6,6,67)

#COMO ELLA LO HIZO:
def add(*args):
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(1,2,3,45,454,6,6,6,67)