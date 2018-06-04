import sys
# alien_0 = {'color':'green','point':5}
# print(alien_0['color'])
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0['x_position'])

# del alien_0['x_position']
# print(alien_0['y_position'])
# user_0 = {
#     'userName':'effor',
#     'first':'enrico',
#     'last':'fermi'
# }

# for k,v in user_0.items():
#     print(k)
#     print(v)


# for name in user_0:
#     print(name.title())

# if 'userName' in user_0.keys():
#     print('userName in user_0')

favorite_language = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python2',
}
# # 遍历排序key
# # for name in sorted(favorite_language.keys()):
# #     print(name.title()+',thank you')
#
# # 遍历值,并取重
# for language in set(favorite_language.values()):
#     print(language.title())

# alien_0 = {'color': 'red', 'points':5}
# alien_1 = {'color': 'black', 'points': 8}
# alien_2 = {'color': 'yellow', 'points': 12}
#
# aliens = [alien_0, alien_1,alien_2]
#
# for alien in aliens:
#     print(alien)

# aliens = []
#
# # 创建30个green 外星人
# for alien_number in range(0,30):
#     new_alien = {'color':'green', 'point': 5, 'speed':'show'}
#     aliens.append(new_alien)
#
# for alien in aliens[0:3]:
#     if alien['color'] == 'green':
#         alien['color'] = 'yellow'
#         alien['speed'] = 'medium'
#         alien['point'] = '10'
#
# for alien in aliens[0:5]:
#     print(alien)

# 字典中存储列表
favorite_language = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'baskell'],
}
for name, languages in favorite_language.items():
    print("\n" + name.title()+' `s favorite language is ')
    for language in languages:
        print('\t'+language.title())

