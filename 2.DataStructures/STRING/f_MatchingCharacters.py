#Write a python program to count the numbers of matching characters in pair of strings

#By iteration
def count_matching_chars(str1, str2):
    count = 0
    for i in range(len(str1)):
        if i < len(str2) and str1[i] == str2[i]:
            count += 1
    return count

#By sets
def count_matching_chars_sets(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    return len(set1.intersection(set2))

string1 = "apple"
string2 = "appeal"
print(count_matching_chars(string1,string2))
print(count_matching_chars_sets(string1,string2))

"""The iteration method counts matching characters in the same positions.
The sets method counts unique matching characters regardless of position."""