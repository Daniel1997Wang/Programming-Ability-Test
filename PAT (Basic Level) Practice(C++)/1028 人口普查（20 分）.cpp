# include <iostream>
# include <vector>
# include <string>
# include <algorithm>
using namespace std;

struct People
{
	char name[20];
	int year;
	int month;
	int day;
	int time;
};

bool cmp(People a,People b)
{
	return a.time < b.time;
}

int main()
{
	
	int i,N;
	People temp;
	vector <People> stu;
	scanf("%d",&N);
	for(i=0;i<N;i++){
		scanf("%s %d/%d/%d",&temp.name,&temp.year,&temp.month,&temp.day);
		temp.time = temp.year*10000 + temp.month*100 + temp.day;
		if((temp.time>=18140906)&&(temp.time<=20140906))	stu.push_back(temp);
	}
	
	sort(stu.begin(),stu.end(),cmp);
	
	int count = stu.size(); 
	if(count == 0)	printf("0");
	else	printf("%d %s %s",count,stu[0].name,stu[count-1].name);

	return 0;
}
