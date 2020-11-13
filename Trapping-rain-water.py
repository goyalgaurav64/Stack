def TrapRainWater(a):
    n=len(a)
    left=[0]*n
    right=[0]*n
    left[0],right[n-1]=a[0],a[n-1]
    for i in range(1,n):
        left[i]=max(left[i-1],a[i])
    for i in range(n-2,-1,-1):
        right[i]=max(right[i+1],a[i])
    water=0
    for i in range(n):
        water+=min(left[i],right[i]) - a[i]
    return water  



if __name__ == "__main__":
    # a=[3,0,0,2,0,4]
    a=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
    ans=TrapRainWater(a)
    print("Maximum Rain water that can be trapped is",ans,"units")