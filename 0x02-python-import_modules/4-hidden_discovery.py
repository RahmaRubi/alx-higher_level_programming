#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    mod_names = dir(hidden_4)
    filterd_names = [name for name in mod_names if (not name.startswith("__"))]
    for name in filterd_names:
        print("{}".format(name))
