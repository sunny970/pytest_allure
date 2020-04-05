# -*- coding:utf-8 -*-

def make_xpath_with_unit_feature(loc):
    key_index = 0
    value_index = 1
    option_index = 2

    args = loc.split(',')
    feature = ""
    if len(args) == 2:
        feature = "contains@"+args[key_index] + ",'" + args[value_index] + "')" + "and"
    elif len(args) == 3:
        if args[option_index] == "1":
            feature = "@" + args[key_index] + "='" + args[value_index] + "'" + "and"
        elif args[option_index] == "0":
            feature = "contains@" + args[key_index] + ",'" + args[value_index] + "')" + "and"
    return feature


def make_xpath_with_feature(loc):
    feature_start = "//*["
    feature_end = "]"
    feature = ""
    if isinstance(loc,str):
        if loc.startswith("//"):
            return loc
        feature = make_xpath_with_unit_feature(loc)
    else:
        for i in loc:
            feature += make_xpath_with_unit_feature(i)
    feature = feature.rstrip("and")
    loc = feature_start + feature + feature_end
    return loc

if __name__ == '__main__':
    make_xpath_with_feature("")