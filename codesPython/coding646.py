"""
Daily Coding Problem: Problem #646 [Easy]
Good morning! Here's your coding interview problem for today.
This problem was asked by Twitter.
A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.
{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group.
For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.
Given a friendship list such as the one above, determine the number of friend groups in the class.
"""
def find_group(friendships, friend ,group):
    # if all friends already explored return group
    if set(friendships[friend]) in group:
        return group
        
    for f in friendships[friend]:
        if f not in group:
            group.add(f)
            group.union(find_group(friendships,f,group))
    return group


def find_friend_groups(friendships):
    # get unique persons
    friends = set(friendships.keys())
    # list that holds groups of people
    groups = []
    # while set has persons
    while(friends):
        f = friends.pop()
        g = find_group(friendships,f,{f})
        friends = friends - g # remove this group of person for set 
        groups.append(g)
        
    return groups


if __name__ == "__main__":
    friendships = {
        0: [1, 2],
        1: [0, 5],
        2: [0],
        3: [6],
        4: [],
        5: [1],
        6: [3]
        }

    print(find_friend_groups(friendships))