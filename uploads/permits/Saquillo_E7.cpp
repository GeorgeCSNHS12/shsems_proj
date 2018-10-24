#include <iostream> 
#include <fstream>

using namespace std;

int main()
{
	fstream infile;  
	ofstream outfile; 
	
	int GN, LN, n[10];


	infile.open("Saquillo_E7.in"); 
	
	if (infile.fail())
	{
		cout << " Input Gone Wrong";
		exit(1);		
	}
	
	for(int j=0; j < 10; j++)
	{
	infile >> n[j];
	cout << "numbers[ "<< j <<" ] "<<"[" << n[j] <<"]" << endl;
	}

	LN=n[0];

	for(int j=0; j < 10; j++)
	if(n[j] > GN){
	GN=n[j];
	}
	for(int j=0; j < 10; j++)
	if(n[j] < LN){
	LN=n[j];
	}
	
	cout << "Greatest number is " << GN << endl;
	cout << "Least number is " << LN << endl;
	
		
	outfile.open("Saquillo_E7.out"); 
	outfile << "Least number <----" << LN << "---->"<< endl
	        << "Greatest number <----" << GN << "---->" << endl;

	
	infile.close();
	outfile.close();


	return 0;
}


