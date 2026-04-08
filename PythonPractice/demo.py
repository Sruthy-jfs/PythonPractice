from dbm import error


def sum(a=0):

    try:
        if a:
             return int(a)+5
        else:
            return('please enter a number')
    except ValueError as error:
        return error


print(sum(3))
