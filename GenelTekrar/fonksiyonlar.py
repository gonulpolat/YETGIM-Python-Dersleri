
# def numbers_sum(nums):
#     nums_sum = 0
#     for i in nums:
#         nums_sum += i
#     return nums_sum
# my_list = [1,2,3,4,5,6,7,8,9]

# print(numbers_sum(my_list))


"""
Özge – göze, Bahri - ihbar
"""

# def is_anagaram(string1,string2):


#     if len(string1) != len(string2):
#         return False

#     used = [False] * len(string2)
#     for i in string1:
#         bool_is_anagram = False
#         for j in range(len(string2)):
#             if not used[j] and i == string2[j]:
#                 used[j] = True
#                 bool_is_anagram = True
#                 break
                
    
#     if not bool_is_anagram:
#         return False

#     return True

# print(is_anagaram("abcd","dcba"))


# def is_anagaram(string1,string2):
#     if len(string1) != len(string2):
#         return False

#     string1_sort = sorted(string1)
#     string2_sort = sorted(string2)

#     return string1_sort == string2_sort 


# print(is_anagaram("abcd","dcbx"))

# def is_anagaram(string1:str,string2:str) -> bool:
#     if len(string1) != len(string2):
#         return False
#     string1 = string1.lower()
#     string2 = string2.lower()
#     string1_dict = {}
#     string2_dict = {}

#     for i in string1:
#         if i in string1_dict:
#             string1_dict[i] += 1
#         else:
#             string1_dict[i] = 1

#     for i in string2:
#         if i in string2_dict:
#             string2_dict[i] += 1
#         else:
#             string2_dict[i] = 1

#     return string1_dict == string2_dict

# print(is_anagaram("Özge","göze"))


"""
[1,2,2,3,4,4,5] bu listedeki tekrar eden elemanları çıkarın
"""

# def remove_duplicate_item(nums:list) -> list:
#     temp = []
#     for i in nums:
#         if i not in temp:
#             temp.append(i)
#     return temp

# def remove_duplicate_item(nums:list) -> list:
#     return list(set(nums))

# def remove_duplicate_item(nums:list) -> list:
#     nums_dict = {}
#     result = []
#     for i in nums:
#         if i in nums_dict:
#             nums_dict[i] += 1
#         else:
#             nums_dict[i] = 1
    
#     for i in nums_dict:
#         result.append(i)
#     return result
# print(remove_duplicate_item([1,2,2,3,4,4,5]))


"""
[1,3,5]
[2,4,6]
[1,2,3,4,5,6]
"""
# def concat_list(list1:list,list2:list)->list:
#     list_min_len = min(len(list1),len(list2))
#     result = []
#     i = 0

#     while i < list_min_len:
#         result.append(list1[i])
#         result.append(list2[i])
#         i += 1
    
#     if len(list1) > len(list2):
#         for i in range(list_min_len,len(list1)):
#             result.append(list1[i])
#         return result
    

#     for i in range(list_min_len,len(list2)):
#         result.append(list2[i])

#     return result
# list1 = [1,3,5,7,8,9]
# list2 = [2,4,6]
# print(concat_list(list1,list2))



# A=[1,3,5]
# B=[2,4,6,7,8,9]
# i=0
# sirali=[]
# while len(A)>i and len(B)>j:
#     if A[i] < B[j]:
#         sirali.append(A[i])
#         i+=1
#     else:
#         sirali.append(B[j])
#         j+=1

# while i < len(A):
#     sirali.append(A[i])
#     i += 1
# while j < len(B):
#     sirali.append(B[j])
#     j += 1
# print(sirali)