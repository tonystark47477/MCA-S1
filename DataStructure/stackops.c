#include<stdio.h>
#define MAX 5
int stack[MAX], top=-1;
void push(int x){
if(top==MAX-1){
printf("Stack overflow\n");
}
else
{
stack[++top]=x;
printf("%d pushed\n",x);
}}
void pop()
{
if(top==-1){
printf("Stack Underflow\n");
}
else
{
printf("%d popped\n", stack[top-1]);
}}
void display(){
if(top==-1){
printf("Stack is empty\n");
}
else
{
printf("Stack elements:");
for(int i=top;i>=0;i--)
printf("%d", stack[i]);
printf("\n");
}
}
int main()
{
int choice,val;
while(1){
printf("\n1.Push 2.Pop 3.Display 4.Exit\n");
printf("Enter your choice:");
scanf("%d",&choice);
switch(choice){
case 1:
printf("Enter value to push:");
scanf("%d",&val);
push(val);
break;
case 2:
pop();
break;
case 3:
display();
break;
case 4:
return 0;
default:
printf("Invalid Choice\n");
}
}
}
