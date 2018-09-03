#include <iostream>

using namespace std;

int cmp(int win_string[3])
{
	if(win_string[0] >= win_string[1] && win_string[0] >= win_string[2])		return 1;
	else if(win_string[1] >= win_string[0] && win_string[1] >= win_string[2])	return 2;
	else if(win_string[2] >= win_string[0] && win_string[2] >= win_string[1])	return 3;
}

int main()
{
	int i,N,ak,bk;
	char m,n;
	int a_win,a_pin,a_loss;
	int b_win,b_pin,b_loss;
	int a_win_string[3] = {0,0,0};
	int b_win_string[3] = {0,0,0};
	ak = bk = 0;
	a_win = b_win = 0;
	a_pin = b_pin = 0;
	a_loss = b_loss = 0;

	scanf("%d",&N);
	for(i=0;i<N;i++){
		getchar();
		scanf("%c %c",&m,&n);
		if((m=='C' && n=='J')||(m=='J' && n=='B')||(m=='B' && n=='C')){
			a_win ++;
			b_loss ++; 
			
			if(m == 'B')		a_win_string[0] ++;
			else if(m == 'C')	a_win_string[1] ++;
			else if(m == 'J')	a_win_string[2] ++;
		}
		else if(m == n){
			a_pin ++;
			b_pin ++;
		}
		else{
			a_loss ++;
			b_win ++;
			
			if(n == 'B')		b_win_string[0] ++;
			else if(n == 'C')	b_win_string[1] ++;
			else if(n == 'J')	b_win_string[2] ++;
		}	
	}
	
	printf("%d %d %d\n",a_win,a_pin,a_loss);
	printf("%d %d %d\n",b_win,b_pin,b_loss);
	if(cmp(a_win_string) == 1)		printf("B ");
	else if(cmp(a_win_string) == 2)	printf("C ");
	else if(cmp(a_win_string) == 3)	printf("J ");
	
	if(cmp(b_win_string) == 1)		printf("B");
	else if(cmp(b_win_string) == 2)	printf("C");
	else if(cmp(b_win_string) == 3)	printf("J");

	
	return 0;
} 
