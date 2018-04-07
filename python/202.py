def vovels(con):
    v=['a','e','o','i','u']
    vovels=[]
    constant=[]
    for i in con:
        if i in v:
            vovels.append(i)
        else:
            constant.append(i)
    print("".join(vovels))
    print("".join(constant))
vovels(input())
                
