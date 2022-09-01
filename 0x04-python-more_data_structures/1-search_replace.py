#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_li(li):
        return (li if li != search else replace)
    return list(map(s_r_li, my_list))
