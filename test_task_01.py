import time


def count_sum(n):
    sum_of_numbers = (n*(n + 1))/2
    return sum_of_numbers

def main():
    print ("Please input n:")
    n = int(input()) 
    #set timer
    start_time = time.time()
    print (str(count_sum(n)))
    print("--- %s seconds ---" % (time.time() - start_time))

main()