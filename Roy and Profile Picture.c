#include <stdio.h>

int main(){
	int l,w,h,n;
	scanf("%d\n%d\n", &l,&n);              	                  
	while(n--){
		scanf("%d %d\n",&w,&h);
		if(w<l || h<l)
		  printf("UPLOAD ANOTHER\n");
		else if(w==h)
		   printf("ACCEPTED\n");
		else
		   printf("CROP IT\n");
	}
	return 0;
}
