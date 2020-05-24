#include<iostream>
#include<stdlib.h>
#include<cmath>
#include<string>
using namespace std;
int main(){
    int c[10001]={0},b[10001]={0},t[10001];
    int L=0,m=0,j=0,d=0,i=0;
    string s;
    cin>>s;
    int N;
    N=s.length();
    c[0]=1;
    b[0]=1;
    while(j<N&&L<=10000){
        d=(int)s[j]-48;
        for(i=j-L;i<=j-1;i++){
            d=(d+(((int)s[i]-48)*c[j-i]))%2;
        }
        m=m+1;
        if(d!=0){
            for(i=0;i<=10001;i++)
                t[i]=c[i];
            for(i=10001;i>=m;i--)
                c[i]=(c[i]^b[i-m])%2;
            if(L<=(j/2)){
                L=j+1-L;                
                for(i=0;i<=10001;i++)
                    b[i]=t[i];
                m=0;
            }
        }
        j=j+1;
    }
    cout<<L;
}