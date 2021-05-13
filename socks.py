#n=int(input("enter no. of socks:"))
n=9
socks_list=[10,20,20,10,10,30,50,10,20]
def sock_merchant(n,socks_list):
    socks_set=set(socks_list)
    pair_count=0
    for sock in socks_set:
        pair_count += socks_list.count(sock)//2
    return pair_count
print(sock_merchant(n,socks_list))
#print(pair_count)