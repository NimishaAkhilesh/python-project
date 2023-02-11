# lst=[
#     [1,34],
#     [40,5],
#     [5,70]
# ]

#print all numbers>50
# for ls in lst:
#     for num in ls:
#         if num>50:
#             print(num)


# print([n for ls in lst for n in ls])
#
# num_gt=[n for ls in lst for n in ls if n>40]
# print(num_gt)

# print(max([n for ls in lst for n in ls ]))

#maxpair
# max_num=(max([n for ls in lst for n in ls ]))
# max_pair=[ls for ls in lst if max_num in ls]
# print(max_pair)


# simple input
# lst=[2,4,6]
#
#
# # sample input2
# lst=[3,4,1]

# lst=[1,2,3,4]
#out=7 #(4,3)
# using one loop

pairnbr = int(input("enter the number:"))
lst=[1,2,3,4]
sum = 0
for i in lst:
    sum = i+(i+1)
    if sum == pairnbr:
        print(i,i+1)
