#include<iostream>
	
using namespace std;

int main()
{ 
	int i, j, k, num;  // variable declaration
	
	{ cout<<"Enter a number : ";  // user input 
	  cin>>num;
	}
	
	do 
	{ cout<<i;
	
		do
		{ 
		cout<<j;
		
			do
			{ cout<<"*";
			}while (k < num);
		
		}while(j <= i);
		
		
	} while(i <= num);
		
		i++;
		
	return 0;
	
}
