def bubble(customlist):
    for i in range(len(customlist)-1):
        for j in range(len(customlist)-i-1):
            if(customlist[j]>customlist[j+1]):
                customlist[j],customlist[j+1]=customlist[j+1],customlist[j]
    return customlist


print(bubble([1,2,3,4,7,8,67,76,45,90,123,122,121,120]))