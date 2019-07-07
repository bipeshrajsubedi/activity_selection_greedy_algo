

activitySetIterative = ["A0"]
activitySetRecursive = []
def IterativeActivitySelection(st,fin,n):

    i=0
    for j in range(n):

        if st[j]>=fin[i]:
            activitySetIterative.append("A"+str(j))
            i=j
    return activitySetIterative

def RecursiveActivitySeletion(st,fin,i,n):
    j=i+1
    while j<n and st[j]<fin[i] and i>=0:
        j=j+1

    if j<n:
        activitySetRecursive.append("A"+str(j))
        RecursiveActivitySeletion(st,fin,j,n)
    return activitySetRecursive


























