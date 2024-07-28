#include <stdio.h>

int main(){
	char a[100];
	int x=0,y=0,i;
	scanf("%s",&a);
	for(i=0;i< strlen(a);i++){
		if(a[i]=='z')
		   x+=1;
		else 
		   y+=1;
	}
	if ((2*x)==y)
	   printf("Yes");
	else
      printf("No");
	
	return 0;
}
	
	

