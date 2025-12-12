
string = "Python sınıfı çok iyi"

# for i in range(10):
#     print(type(i))
#     print(i)


# for i in string:
#     print(type(i))
#     print(i)


# i = 0

# while i < 10:
#     print(i)
#     i += 1

# import random
# user1_num_list = []
# user2_num_list = []
# user1_score = 0 
# user2_score = 0
# user1_win = 0
# user2_win = 0
# tie = 0
# for i in range(6):
#     user1_num = random.randint(1,7)
#     user1_num_list.append(user1_num)
#     user2_num = random.randint(1,7)
#     user2_num_list.append(user2_num)

# # print(user1_num_list)
# # print(user2_num_list)

# i = 0

# while i < 6:
#     if user1_num_list[i] > user2_num_list[i]:
#         user1_win += 1
#         user1_score += 10
#     elif user2_num_list[i] > user1_num_list[i]:
#         user2_win += 1
#         user2_score += 10
#     else:
#         tie += 1
#     i += 1


# print(f"""
#     ====Oyun Bilgileri====:
#         Kullanıcı 1'in kazandığı oyun sayısı : {user1_win}
#         Kullanıcı 2'in kazandığı oyun sayısı : {user2_win}
#         Berabere biten oyun sayısı : {tie}
# """)


# if user1_score > user2_score:
#     print("Kullanıcı 1 Oyunu kazandı...")
# elif user2_score > user1_score:  
#     print("Kullanıcı 2 Oyunu Kazandı...")
# else:
#     print("Berabere Bitti...")


"""
Kullanıcıdan alınan cümlenin kaç kelimeden oluştuğunu ekrana bastırın 
"""
# cümle = "Kullanıcıdan alınan cümlenin kaç kelimeden oluştuğunu ekrana bastırın"

# kelime_sayisi = 1

# for i in cümle:
#     if i == " ":
#         kelime_sayisi += 1

# kelime_icinde = False

# for i in cümle:
#     if i != " " and not kelime_icinde:
#         kelime_sayisi += 1
#         kelime_icinde = True
#     elif i == " ":
#         kelime_icinde = False
    



# print(kelime_sayisi)

