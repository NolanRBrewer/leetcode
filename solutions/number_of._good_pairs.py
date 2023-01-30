# list of nums
nums = [1,2,3,1,1,3]
# dictionary key = num, value = times num occurs
good_pairs = {}
# tracks number of valid pairs between nums
pair_count = 0
for num in nums:
    if num not in good_pairs:
        good_pairs[num] = 1
    elif num in good_pairs:
        good_pairs[num] += 1

    if good_pairs[num] > 1:
        pair_count = pair_count + good_pairs[num] - 1
    
print(pair_count)