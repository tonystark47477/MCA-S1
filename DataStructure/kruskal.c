#include <stdio.h>
#define MAXE 100
#define MAXV 100
struct Edge{int u,v,w;}e[MAXE],t;
int parent[MAXV];
int find(int x){if(parent[x]==x)return x;return parent[x]=find(parent[x]);}
void unite(int a,int b){a=find(a);b=find(b);if(a!=b)parent[b]=a;}
int main(){
int V,E,i,j,cost=0,count=0;
scanf("%d%d",&V,&E);
for(i=0;i<E;i++)scanf("%d%d%d",&e[i].u,&e[i].v,&e[i].w);
for(i=0;i<E-1;i++)for(j=0;j<E-1-i;j++)if(e[j].w>e[j+1].w){t=e[j];e[j]=e[j+1];e[j+1]=t;}
for(i=1;i<=V;i++)parent[i]=i;
for(i=0;i<E&&count<V-1;i++){
int a=find(e[i].u),b=find(e[i].v);
if(a!=b){
printf("%d %d %d\n",e[i].u,e[i].v,e[i].w);
cost+=e[i].w;
unite(a,b);
count++;
}}
printf("%d",cost);
return 0;
}
