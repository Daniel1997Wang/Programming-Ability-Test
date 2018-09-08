#include <iostream> 
using namespace std;

int main()
{
	int start_address,N,K;
	int data[100001],next_address[100001],temp_address[100001];
	int i,j,k,temp,pre_address,count,next;
	scanf("%d %d %d",&start_address,&N,&K);

	for(i=0;i<N;i++){
		scanf("%d",&pre_address);
		scanf("%d %d",&data[pre_address],&next_address[pre_address]);
	}
	count = 0;
	pre_address = start_address;
	temp_address[count] = pre_address;
	
	while(pre_address != -1){
		count ++;
		temp_address[count] = next_address[pre_address];
		pre_address = next_address[pre_address];
	}
	
	
	for(k=0;k<(count/K);k++){
		for(i=0;i<K-1;i++){
			for(j=i+1;j<K;j++){
				temp = temp_address[k*K+i];
				temp_address[k*K+i] = temp_address[k*K+j];
				temp_address[k*K+j] = temp;
			}
		}		
	}
	
	for(i=0;i<count-1;i++){
		pre_address = temp_address[i];
		next = temp_address[i+1];
		printf("%05d %d %05d\n",pre_address,data[pre_address],next);
	}
	pre_address = temp_address[i];
	printf("%05d %d -1",pre_address,data[pre_address]);

	
	return 0;
}
