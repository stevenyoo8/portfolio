def main () :
    3 + 7
    3 - 10
    3 + 7 , 3 - 10
    print (" What happened to the previous lines ?")

nums = [-2,1,-3,4,-1,2,1,-5,4]

sum = 0
for i in nums:
    sum = sum + i
print(sum)


ans = float("-inf")
for i in range(len(nums)):
    cur_sum = 0
    for j in range(i, len(nums)):
        cur_sum = cur_sum + nums[j]
        ans = max(ans, cur_sum)
print(ans)