users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
    print(a)
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]
        print(a)


        active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(users)
print(active_users)
