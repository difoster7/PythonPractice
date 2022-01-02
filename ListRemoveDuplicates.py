# https://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

def remove_dup(dupes_list):
    no_dupes = []
    for x in dupes_list:
        if x not in no_dupes:
            no_dupes.append(x)
    return no_dupes


def remove_dup_set(dupes_list):
    return set(dupes_list)


hi = [1, 1, 2, 2, 4, 6, 56, 7, 9, 7]

print(hi)
print(remove_dup(hi))
print(remove_dup_set(hi))