
Winfilepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/WinApi.txt'
# Linfilepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/linuxApi.txt'
# Stlfilepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/StlApi.txt'
# GNUfilepath = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/GNUApi.txt'
outputfile = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/Api.txt'
outputfile2 = '/Users/chengxiao/Desktop/VulDeepecker/apilist/linuxApi/out/Api2.txt'

filepath = [Winfilepath, outputfile]
apilist = []
for fil in filepath:

    with open(fil, 'r') as f:
        apilist.extend(list(set(f.read().split(" "))))

apilist = list(set(apilist))[1:]

with open(outputfile2, 'w', encoding='utf-8') as f:
    for api in apilist:
        f.write(api+" ")
print("end")