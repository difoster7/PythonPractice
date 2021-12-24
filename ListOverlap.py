# https://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

import random

ran_nums1 = []
ran_nums2 = []

for i in range(15):
    ran_nums1.append(random.randint(0, 20))
    if i < 10:
        ran_nums2.append(random.randint(0, 20))

print("array1: " + str(ran_nums1))
print("array2: " + str(ran_nums2))

overlap = [x for x in ran_nums1 if x in ran_nums2]
print("overlap is: " + str(overlap))