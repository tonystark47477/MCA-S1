#include<stdio.h>
int main()
{
int n,i,key,found=0;
printf("Enter number of elements:\n");
scanf("%d",&n);
int arr[n];
printf("Enter %d elements:\n", n);
for(i=0;i<n;i++)
{
scanf("%d",&arr[i]);
}
printf("Enter element to search:\n");
scanf("%d",&key);
for(i=0;i<n;i++)
{
if(arr[i] == key){
printf("Element %d found at position %d \n",key,i+1);
found=1;
break;
}
}
if(found==0)
{
printf("Element %d not found in the array \n",key);
}
return 0;
}



