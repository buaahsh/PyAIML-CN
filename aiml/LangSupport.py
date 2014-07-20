# -*- coding: utf-8 -*-


import aiml.jieba as jieba


def splitChinese(s):
    tokens = jieba.cut(s)
    # result = []
    # for c in s:
    #     if isChinese(c):
    #         result.extend([" ", c, " "])
    #     else:
    #         result.append(c)
    # ret = ''.join(result)
    # return ret.split()
    return tokens


def mergeChineseSpace(s):
    assert type(s) == unicode, "string must be a unicode"
    segs = splitChinese(s)
    result = []
    for seg in segs:
        # English marks
        if seg[0] not in ".,?!":
            try:
                str(seg[0]) and result.append(" ")
            except:
                pass
        result.append(seg)
        try:
            str(seg[-1]) and result.append(" ")
        except:
            pass
    return u''.join(result).strip()
