#Implementation of Sieve of Eratosthenes
def primeseive(n):
    prime=(True for i in range(n+1))
    currentnumber=2
    while(currentnumber*currentnumber <=n ):
        if (prime[currentnumber] == True ):
            for i in range(currentnumber ** 2, n+1 ,currentnumber):
                prime[i]=False
                currentnumber+=1
                prime[0]=False
                prime[1]=False
                for p in range(n+1):
                    if prime[p]:
                        prime(p)
n=int(input("enter the number to find all prime no.less the number : "))
primeseive(n)
print("following are the prime number smaller")
print("than or equal to")


