#include <iostream> 
#include <cmath>
using namespace std;

bool Is_prime(int n)
{
	int i;
	if(n==0 || n==1)	return false;
	else if(n == 2)	return true;
	else{
		for(i=2;i<sqrt(n)+1;i++){
			if(n%i == 0)	return false;
		}
		return true;
	}
} 

int main()
{
	int i,N,count;
	scanf("%d",&N);
	for(i=2,count=0;i<N-1;i++){
		if(Is_prime(i) && Is_prime(i+2))	count ++;
	}
	printf("%d",count);
	
	return 0;
}
