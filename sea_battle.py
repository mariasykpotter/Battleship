LENGTH = 10


def read_field(filename: str) -> list:
    '''
    :param str
    :return: list
    '''
    result = []
    f = open(filename, "r")
    data = f.read()
    s = data.split("\n")
    for el in s:
        text = []
        for e in el:
            if e == "*":
                text.append(1)
            else:
                text.append(0)
        result.append(text)
    return result


print(read_field("sea.txt"))


def has_ship(data, tup):
    '''
    :param list
    :param tuple
    :return: bool
    '''
    x = int(tup[0])
    y = int(tup[1])
    # print(data[y])
    return bool(data[y][x])

# print(has_ship(read_field("sea.txt"), (7, 1)))


def ship_size(data, tup):
    '''

    :param list
    :param tuple
    :return: int
    '''
    if has_ship(data, tup):
        x = int(tup[0])
        y = int(tup[1])
        row = data[y]
        # print(row)
        col = [row1[x] for row1 in data]
        # print(col)
        if not has_ship(data, tup):
            return 0
        size = 1
        if x != len(row) - 1:
            right_index = x + 1
            # print(right_index)
            right_el = row[right_index]
            # print(right_el)
            while right_el:
                if len(row) > right_index + 1 >= 2:
                    size += 1
                    right_index += 1
                    right_el = row[right_index]
                    # if right_index < len(row) - 1:
                    #     right_el = row[right_index]
                    # else:
                    #     right_el = row[right_index-1]
                    # print(right_index)
                elif row[len(row)-1]:
                    size += 1
                    right_el = False
                else:
                    break
        left_index = x - 1
        left_el = row[left_index]
        # print(left_index)
        # print(left_el)
        while left_el:
            if len(row) > left_index + 1 >= 0:
                size += 1
                left_index -= 1
                if left_index > 0:
                    left_el = row[left_index]

            else:
                break
        top_index = y - 1
        top_el = col[top_index]
        # print(top_el)
        while top_el:
            if len(col) > top_index >= 0:
                size += 1
                top_index -= 1
                if top_index > 0:
                    top_el = col[top_index]

            else:
                break
        # print(size)
        b_index = y + 1
        b_el = col[b_index]
        # print(b_el)
        while b_el:
            if len(col) >= b_index + 1 >= 0:
                size += 1
                b_index += 1
                b_el = col[b_index]

            else:
                break
        return size


# print(ship_size(read_field("sea.txt"), (7, 1)))


def is_valid(data):
    '''
    :param list
    :return: bool
    '''
    result = []
    nums = []
    for i in range(10):
        lst = []
        for j in range(10):
            lst.append(ship_size(read_field("sea.txt"), (j, i)))
        result.append(lst)
    for el in result:
        for e in el:
            if isinstance(e, int):
                nums.append(e)
    for num in nums:
        if num in[1,2,3,4]:
            if nums.count(1) == 4 and  nums.count(2) == 6 and  nums.count(3) == 6 and nums.count(4) == 4:
                return True
            else:
                return False
        else:
            return False
def  field_to_str_with_ships(data,item):

    '''
    :param list
    :return: str
    '''
    field = ""
    for el in data:
        for e in el:
            if e == 1:
                field += "*"
            elif e == 0:
                field += item
            elif e == "shot":
                field+="X"
            elif e == None:
                field+="_"
            # elif e == 0:
            #     field+="_"
            else:
                field+=item
        field += "\n"
    return field
def  field_to_str(data,item):
    '''
    :param list
    :return: str
    '''
    field = ""
    for el in data:
        for e in el:
            if e == 0 or e == 1:
                field += item
            elif e == "shot":
                field+="X"
            elif e == None:
                field+="_"
            # elif e == 0:
            #     field+="_"
            else:
                field+=item
        field += "\n"
    return field

def generate_field ():
    '''
    param: None
    :returns: str
    '''
    pass

