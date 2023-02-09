# change directory to the containing folder before running the script
def parse_user(text):
    # id name grade - birthyear : gender
    user = {}
    values = text.split()
    user["id"] = int(values[0])
    user["name"] = values[1]
    user["birthyear"] = int(values[4])
    user["gender"] = values[6]
    assert values[3] == "-"
    assert values[5] == ":"

    if values[2] == "N/A":
        user["score"] = None
    else:
        user["score"] = int(values[2])

    return user


def parse_users_file(filepath):
    users = []

    try:
        f = open(filepath, "r")
        users = map(parse_user, f.readlines()[1:])
        users = filter(lambda u: u["score"], users)
        users = list(users)
        f.close()
    except FileNotFoundError:
        # NOTE: we can use os.path to get the file path relative to this script
        # without the need to cd into the containing directory, but we aren't allowed to use libs
        print(f"sorry the file {filepath} doesn't exist")
        print("make sure to run this script from the correct working directory")
        exit(1)
    except (AssertionError, ValueError):
        print(f"the file {filepath} contains in valid data")
        exit(1)

    return users


if __name__ == "__main__":
    users = parse_users_file("grades.txt")

    if not users:
        print("sorry, we can't find any user in grades.txt")
        exit(1)

    oldest_id = None
    max_score_gender = None
    max_age = -1
    max_score = -1
    score_sum = 0

    for u in users:
        score_sum += u["score"]
        age = 2023 - u["birthyear"]
        if age > max_age:
            max_age = age
            oldest_id = u["id"]
        if u["score"] > max_score:
            max_score = u["score"]
            max_score_gender = u["gender"]

    assert oldest_id
    assert max_score_gender

    print(f"ID of the oldest user:\t{oldest_id}")
    print(f"average score:\t{score_sum / len(users)}")
    print(f"gender of the user with highest score:\t{max_score_gender}")

