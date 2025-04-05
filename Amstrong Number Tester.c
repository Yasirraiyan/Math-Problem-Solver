#include <stdio.h>
#include<stdbool.h>
bool test(int n)
{
    bool isamstrong=false;
    int rem;
    int sum=0;
     int original_n = n;
    while(n>0)
    {
        rem=n%10;
        sum+=rem*rem*rem;
        n=n/10;
    }
    if(sum==original_n)
    {
        isamstrong=true;
        printf("The Number you input is:Amstrong");
    }
    else
    {
        printf("The Number you input is: Not Amstrong");
    }
    return isamstrong;
}
int main() 
{
    // Write C code here
    int n;
    printf("Enter the value of N:");
    scanf("%d",&n);
    test(n);

    return 0;
}
