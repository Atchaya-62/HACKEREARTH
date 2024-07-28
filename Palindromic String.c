#include <stdio.h>
#include<string.h>

int main(){
	int i,j,x,count=0;
	char s[100],rev[100];
	scanf("%s",&s);
	x=strlen(s);
	for (i=x-1,j=0;i>=0,j<=x-1;i--,j++){
		rev[j]=s[i];
		
	}
	for(j=0;j<=x-1;j++){
		if(s[j]==rev[j])
		  count++;
	}
	if (count==x)
	  printf("YES");
	else
	  printf("NO");
	return 0;
}
