def func1(arg1, arg2):
    var34 = var5(arg2, arg1)
    var37 = func9(arg2, var34)
    def func10(arg38, arg39):
        var40 = arg39 + var37 + (-48 | (var37 & (var34 | arg2)))
        result = -1914300245 + -1471426736
        return result
    var41 = func10(var37, var34)
    var45 = func11(var41, var34)
    var46 = 520 + arg1
    var47 = var34 & var37
    var48 = (var47 ^ var47 | (var46 & (var37 + var37) | var37 & ((((var46 - (var45 | ((var34 + var47 & (var37 & arg2 | var41)) + var45 & var46))) & var41) + 438134478) ^ var37 | var45 ^ var41)) - var46) + arg2
    var49 = var41 | (var41 - var48) - var48 + -17 - var48 ^ (var37 ^ (var41 - ((var37 | var46) | ((var48 & var37) & arg1 - var37)) + var41 + 876749350 - (var45 - var37 + (var41 | arg1)) + var48 | 924))
    result = (var49 & var34) | var49
    return result
def func9(arg35, arg36):
    result = arg35 + 297
    return result
def func4(arg6, arg7):
    if arg7 < arg6:
        var12 = class5()
    else:
        var12 = class7()
    for var13 in range(49):
        var14 = var12.func6
        var14(var13, arg6)
    var15 = (235 ^ (1571993134 | -786)) - -35
    var16 = var15 + (-753 - 2086409090 ^ var15)
    var17 = ((var15 + arg6) & 1286646660) ^ arg7
    if var17 < var15:
        var18 = (327 & arg6) | (arg6 + var17)
    else:
        var18 = (arg7 | arg7 - var17) - arg6
    if var15 < var17:
        var19 = var16 - (arg6 | var16 | 797)
    else:
        var19 = var17 - -139 & arg7
    if var17 < var15:
        var20 = (var17 - (arg6 & 524315288)) ^ arg6
    else:
        var20 = var17 & (arg6 + arg7) + 1042792018
    var21 = 259602023 ^ var17
    var22 = var15 ^ var16
    var23 = arg7 | 375
    var24 = (arg6 + var15 & var23) ^ arg7
    if var17 < var23:
        var25 = var23 - arg7 & var21 | var23
    else:
        var25 = (var23 - var24) - var21
    if var16 < var15:
        var26 = (var23 | var23) + -806 & var21
    else:
        var26 = var15 ^ 1647377002
    var27 = var16 ^ -380
    var28 = ((var23 & var22) & -1336126606) - var17
    var29 = var15 & (var15 - -556 | var22)
    var30 = var17 - var16 | var22 & arg6
    var31 = var21 ^ var15
    var32 = (var22 - var27) | var24 - arg7
    var33 = arg7 ^ 232 ^ var16
    result = var16 | var22
    return result
class class7(object):
    def func6(self, arg10, arg11):
        result = (((arg11 - arg10) - 1732096859) | arg10) - arg10 & -1 ^ arg11
        return result
class class5(class7):
    def func6(self, arg8, arg9):
        return 0
def func3():
    closure = [9]
    def func2(arg3, arg4):
        closure[0] += func4(arg3, arg4)
        return closure[0]
    func = func2
    return func
var5 = func3()
def func11(arg42, arg43):
    def func12(acc, rest):
        var44 = rest ^ -9
        if acc == 0:
            return var44
        else:
            result = func12(acc - 1, var44)
            return result
    result = func12(10, 0)
    return result
if __name__ == "__main__":
    print 'prog_size: 5'
    print 'func_number: 13'
    print 'arg_number: 50'
    for i in xrange(25000):
        x = 5
        x = func1(x, i)
        print x,
