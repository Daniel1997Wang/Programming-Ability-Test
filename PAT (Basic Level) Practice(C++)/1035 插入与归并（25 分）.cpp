# include <iostream>
# include <vector>
# include <algorithm>
# include <cmath>
using namespace std;

void vector_print(int flag,vector <int> v)
{
	int i,N;
	N = v.size();
	if(flag == 0)	printf("Insertion Sort\n");
	else	printf("Merge Sort\n");
	for(i=0;i<N-1;i++)
		printf("%d ",v[i]);
	printf("%d",v[i]);
}

int main()
{
	int i,j,k,N,temp,flag;
	vector <int> scanf_v,v,cmp_v,orid_v,result;
	//输入 
	scanf("%d",&N);
	for(i=0;i<N;i++){
		scanf("%d",&temp);
		scanf_v.push_back(temp);
	}
	for(i=0;i<N;i++){
		scanf("%d",&temp);
		cmp_v.push_back(temp);
	}
	orid_v = scanf_v;
	sort(orid_v.begin(),orid_v.end());
	//插入排序的算法 
	v = scanf_v;
	for(i=1;i<N;i++){
		//if(equal(v.begin(),v.end(),orid_v.begin())){
		//	flag = 0;	result = v;	break;
		//}
		sort(v.begin(),v.begin()+i);
		if(equal(v.begin(),v.end(),cmp_v.begin())){
			sort(v.begin(),v.begin()+i+1);
			flag = 0;	result = v;	break;	
		}
	}
	

	//归并排序的算法 
	v = scanf_v;
	k = 2;
	for(j=0;j<N;j++){
		if(equal(v.begin(),v.end(),orid_v.begin())){
			flag = 1;	result = v;	break;
		}
		for(i=0;i<N/k;i++){
			temp = k*i;
			sort(v.begin()+temp,v.begin()+temp+k);
		}
		k = k*2;
		if(equal(v.begin(),v.end(),cmp_v.begin())){
			if(equal(v.begin(),v.end(),orid_v.begin()) == false){
				for(i=0;i<N/k;i++){
					temp = k*i;
					sort(v.begin()+temp,v.begin()+temp+k);
				}
				flag = 1;	result = v;	break;
			}
			
		}		
	}
	vector_print(flag,result);
	return 0;
}
