# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

int main()
{
	int i,j,N,temp,count,result;
	long int a,p;
	vector <int> stu;
	
	scanf("%d %ld",&N,&p);
	for(i=0;i<N;i++){
		scanf("%d",&temp);
		stu.push_back(temp);
	}
	sort(stu.begin(),stu.end());

	result = 0;count = 0;
	for(i=0;i<N;i++){
		//count=1;
		for(j=i+result;j<N;j++){
			a = stu[i]*p;
			if(a>=stu[j])	//count++;
			count = j-i+1;
			if(result < count)	result = count;
			else	break;
		}
		//if(result < count)	result = count;
	}


	printf("%d",result);
	return 0;
}
