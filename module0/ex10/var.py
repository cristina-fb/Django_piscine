def my_var():
    v_int = 42
    v_str = "42"
    v_str2 = "quarante-deux"
    v_float = 42.0
    v_bool = True
    v_list = [42]
    v_dict = {42: 42}
    v_tup = (42,)
    v_set = set()

    print(str(v_int) + " has a type " + str(type(v_int)))
    print(str(v_str) + " has a type " + str(type(v_str)))
    print(str(v_str2) + " has a type " + str(type(v_str2)))
    print(str(v_float) + " has a type " + str(type(v_float)))
    print(str(v_bool) + " has a type " + str(type(v_bool)))
    print(str(v_list[0]) + " has a type " + str(type(v_list)))
    print(str(v_dict) + " has a type " + str(type(v_dict)))
    print(str(v_tup) + " has a type " + str(type(v_tup)))
    print(str(v_set) + " has a type " + str(type(v_set)))

if __name__ == '__main__':
    my_var()