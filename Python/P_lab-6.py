def duplicate_Value(list_of_item):
    list_empty = set([])
    for i in range (len(list_of_item)):
        for j in range (len(list_of_item)):
            if list_of_item[i]==list_of_item[j] and i!=j:
                list_empty.add(list_of_item[i])
    return list(list_empty)

if __name__ == "__main__":
    list_of_item = [1,3,9,4,1,2,3,1,2]
    # list containing dublicate values
    print(f"Duplicate values in the list : {duplicate_Value(list_of_item)} ")