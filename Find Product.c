#include <stdio.h>

void main(){
	int num,i,p=1;
	long int ar[1000];
	scanf("%d", &num);        
	for (i=0;i<num;i++){
		scanf("%ld\t",&ar[i]);
	}     
	for (i=0;i<num;i++){
		p=(p*ar[i])%(1000000007);
		
	}     
	printf("%d",p); 
		                
	}
