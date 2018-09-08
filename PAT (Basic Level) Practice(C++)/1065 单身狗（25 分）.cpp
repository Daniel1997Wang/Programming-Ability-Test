#include <iostream> 
#include <vector>
#include <algorithm>
using namespace std;
struct PAT
{
	int man;
	int woman;
};

int main()
{
	int i,j,k,man,n,N;
	PAT temp;
	vector <PAT> stu;
	vector <int> test,remain;
	scanf("%d",&N);
	for(i=0;i<N;i++){
		scanf("%d %d",&temp.man,&temp.woman);
		stu.push_back(temp);
	}
	scanf("%d",&n);
	for(i=0;i<n;i++){
		scanf("%d",&man);
		test.push_back(man);
	}
	
	for(i=0;i<test.size();i++){
		for(j=0;j<N;j++){
			
			if(test[i]==stu[j].man){
				for(k=0;k<test.size();k++){
					if(test[k]==stu[j].woman){
						test.erase(test.begin()+i);
						test.erase(test.begin()+k-1);
						break;
					}
				}
			}
			
			if(test[i]==stu[j].woman){
				for(k=0;k<test.size();k++){
					if(test[k]==stu[j].man){
						test.erase(test.begin()+i);
						test.erase(test.begin()+k-1);
						break;
					}
				}
			}
			
		}
	}
	
	sort(test.begin(),test.end());
	printf("%d\n",test.size());
	printf("%d",test[0]);
	for(i=1;i<test.size();i++){
		printf(" %d",test[i]);
	}

	return 0;
}
