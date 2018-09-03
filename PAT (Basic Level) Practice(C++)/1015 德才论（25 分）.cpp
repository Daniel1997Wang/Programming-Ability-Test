#include <iostream> 
#include <vector> 
#include <algorithm>

using namespace std;

struct Student{
	int ID;
	int D;
	int C;
	int sum;
	int rank;
};

bool cmp(Student a,Student b)
{
	if(a.rank != b.rank){
		return a.rank < b.rank;
	}
	else{
		if(a.sum != b.sum){
			return a.sum > b.sum;
		}
		else{
			if(a.D != b.D){
				return a.D > b.D;
			}
			else{
				if(a.ID != b.ID){
					return a.ID < b.ID;
				}
			}
		}
	}
}

int main()
{
	int N,L,H;
	int i;
	Student stu;
	vector <Student> v;

	scanf("%d %d %d",&N,&L,&H);
	for(i=0;i<N;i++){
		scanf("%d %d %d",&stu.ID,&stu.D,&stu.C);
		if(stu.D>=L && stu.C>=L){
			stu.sum = stu.D + stu.C;
			if(stu.D>=H && stu.C>=H)					stu.rank = 1;
			else if(stu.D>=stu.C && stu.D>=H)			stu.rank = 2;
			else if(stu.D>=stu.C && stu.D<H && stu.C<H)	stu.rank = 3;
			else										stu.rank = 4;
			v.push_back(stu);
		}
	}
	
	sort(v.begin(),v.end(),cmp);	
	
	printf("%d\n",v.size());
	//Êä³ö 
	for(i=0;i<v.size();i++){
		printf("%08d %d %d",v[i].ID,v[i].D,v[i].C);
		if(i!=v.size()-1){
			printf("\n");
		}
	}
	return 0;
}
