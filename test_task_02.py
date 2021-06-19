#if islands == just land


def number_of_islands(m,n,matrix):
    if(matrix == None):
        return 0
    counter = 0
    for i in range(n):
        for j in range(m):
            if(matrix[i][j]==1):
                counter+=1
                delete_land(matrix,i,j,n,m)
    return counter

#define land and delete to make it easier to identify new islands
def delete_land(matrix,i,j,n,m):
    if(i>=0 and i< n 
        and j>=0 and j<m and matrix[i][j]!=0):
        matrix[i][j] = 0
        delete_land(matrix,i+1,j,n,m)
        delete_land(matrix,i-1,j,n,m)
        delete_land(matrix,i,j+1,n,m)
        delete_land(matrix,i,j-1,n,m)

print ("Please input n:")
n = int(input()) 
print ("Please input m:")
m = int(input()) 
print ("Please input matrix:")
matrix = [list(map(int, input().split())) for i in range(n)]

print ("Number of islands: " + str(number_of_islands(m,n,matrix)))