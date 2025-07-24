"""
This script generates a randomized list of study participants for an experimental study.
It creates a CSV file with 100 participants split into two groups of 50 each.
Each participant is assigned:
- A unique ID number
- A group type (1 or 2)
- A role (Operator or User)
- Random scenario order (from scenarios a,b,d,e)
- Random questionnaire order (bfi,ati,tse,ptt,aik,pva,bba,lota)

The output is saved to 'participants_randomized.csv' with appropriate column headers.
"""
import random
import csv

def rand_part(start):
    num_participants = 50

    num_type_0 = int(num_participants / 2)
    num_type_1 = num_participants - num_type_0
    exp_type_list = ["1"] * num_type_0 + ["2"] * num_type_1

    role_0_operator = int(num_type_0 / 2)
    role_0_user = num_type_0 - role_0_operator
    role_0_list = ["Operator"] * role_0_operator + ["User"] * role_0_user

    role_1_operator = int(num_type_1 / 2)
    role_1_user = num_type_1 - role_1_operator
    role_1_list = ["Operator"] * role_1_operator + ["User"] * role_1_user

    role_list = role_0_list + role_1_list

    all_list = []
    for i in range(num_participants):
        sc = ["a", "b", "d", "e"]
        qqq = ["bfi", "ati", "tse", "ptt", "aik", ["pva", "bba", "lota"]]
        random.shuffle(sc)
        random.shuffle(qqq)

        # Flatten
        q_flat = []
        for q in qqq:
            if isinstance(q, list):
                q_flat += q
            else:
                q_flat.append(q)
        temp = [exp_type_list[i], role_list[i]] + sc + q_flat
        all_list.append(temp)

    random.shuffle(all_list)
    participants = [str(start+i+1) for i in range(num_participants)]
    res = [[b] + a for a, b in zip(all_list, participants)]
    print(res)
    return res


if __name__ == '__main__':

    res_1 = rand_part(0)
    res_2 = rand_part(50)

    res = res_1 + res_2
    res.insert(0, ["participant", "group", "role", "S1", "S2", "S3", "S4",
                   "PM1", "PM2", "PM3", "PM4", "PM5", "PM6", "PM7", "PM8"])
    with open("participants_randomized.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(res)

