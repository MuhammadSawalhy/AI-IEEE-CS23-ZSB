# change directory to the containing folder before running the script
from problem_4 import parse_users_file


def stringify_user(user):
    # id name - birthyear
    return f"{user['id']} {user['name']} - {user['birthyear']}"


if __name__ == "__main__":
    users = parse_users_file("grades.txt")
    with open("filtered.txt", "w") as f:
        f.write("\n".join(map(stringify_user, users)))
