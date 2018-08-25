#include <iostream>
#include <cmath>
using namespace std;

bool is_prime(int n)
{
	int i;
	if(n==0 || n==1)	return false;
	else if(n==2)	return true;
	else{
		for(i=2;i<sqrt(n)+1;i++){
			if(n%i == 0)	return false;
		}
		return true;
	}	
}

int main()
{
	int i,j,M,N;
	int a[10001];
	scanf("%d %d",&M,&N);
	for(i=2,j=0;j<10001;i++){
		if(is_prime(i)){
			a[j] = i;
			j ++;
		}
	}
	for(i=M-1,j=0;i<N;i++,j++){
		if(j%10==0&&j!=0)	printf("\n"); 
		if(j%10!=0)	printf(" ");
		printf("%d",a[i]);
	}
	return 0;
} 
