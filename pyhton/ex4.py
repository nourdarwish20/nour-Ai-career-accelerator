# def ifexist(List,nb):
#     return nb in List

# list=[1,4,6,9]
# # res=ifexist(list,5)
# res=ifexist(list,1)
# print(res)


def ifexist(List,nb):
  for x in List:  
    if x==nb:
        return True
    return False
list=[1,4,6,9]
# res=ifexist(list,5)
res=ifexist(list,1)
print(res)