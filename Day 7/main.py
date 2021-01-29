msg_template = """Hello {name},
Thank you for joining {website}. We are very happy to have you with us.
"""

def format_msg(my_name="Brian", my_website="www.libranconsult.com"):
    my_message = msg_template.format(name=my_name, website=my_website)
    print(my_message, "\n")
    return my_message

# Assignment_1
# Receive names from various users and save into a list
# Parse the names to the format_names() function and print out a a welcome note to each of them.

def get_names():
    user_list, answer, query = [], True, True,
    while answer == True:
        user = input("Enter name: ")
        user_list.append(user)
        query = input("Do you want to enter another name? Type Y or N : ")
        query = query.upper()
        if query == 'N':
            break
        else:
            continue

    return user_list

def print_user_list():
    users = get_names()
    for user in users:
        format_msg(user, "www.libranconsult.com")

if __name__ == "__main__":
    print_user_list()






