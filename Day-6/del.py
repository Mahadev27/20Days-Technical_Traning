def func(var1, var2) :
    try:
        var3=(int) (var1)
        var2=var3+"A"
        print (var2)
    except TypeError:
        print("T")
    finally:
        print("IF")
try:
    func('R', 13)
except ValueError:
    print("V")
finally:
    print ("OF")