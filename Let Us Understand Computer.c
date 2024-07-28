#include <stdio.h>
#include<math.h>

int main(){
	unsigned long long int num;
	scanf("%llu", &num);   
	while(num--){
		unsigned long long int k,n,ans,i;
		scanf("%lld",&n);
		i=1;
		while(i<=sqrt(n)){
			i=i*2;
		}
		if(n/i>=i/2)
		  ans=n-n/i;
		else
		  ans=(n-(i/2))+1;
	    printf("%lld\n",ans);
	}           	                  
	
}
