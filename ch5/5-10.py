current_name = ["ilya", "leo", "admin", "denis", "max"]
new_users = ['ilya', 'leo', 'todd', 'john', 'peter']
for n_user in new_users:
    if n_user.lower() in current_name:
        print("NO")
    else:
        print(f"Hello {n_user.title()}")