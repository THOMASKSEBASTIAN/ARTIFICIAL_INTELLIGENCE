first_list = ["O","X","A","C","D","K"]
second_list = ['1','2','3','4','5','6']

zipped_pairs = zip(first_list,second_list)

sorted_pairs = sorted(zipped_pairs)
print(sorted_pairs)
for item in sorted_pairs:
    print(item[1])



