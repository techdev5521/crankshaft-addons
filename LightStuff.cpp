#include <iostream>
#include <random>
#include <chrono>
#include <thread>
#include <fstream>
#include <stdio.h>

using namespace std;
int lightvalue;
int decider = 50;   // Sets interval of brightness change
int times = 50;   // Length of interval


//Randomly generates a number between 1 and 100
int firstselection(){
	random_device rd; // obtain a random number from hardware
    mt19937 eng(rd()); // seed the generator
    uniform_int_distribution<> distr(0, 100); // define the range
    lightvalue = 1;        //distr(eng);// generate numbers
    return 0;
}

//changes the inital value in somewhat controlled increments
int manipulate(){

        
    	random_device rd2; // obtain a random number from hardware
    	mt19937 eng2(rd2()); // seed the generator
    	uniform_int_distribution<> distr2(0, 100);
    	//distr2(eng2);
        //int hold = decider%10;
    	if(lightvalue == 99){
            decider = 40;
        }
        if(lightvalue == 1){
            decider = 50;
        }
        if(decider>=0 && decider <=49 ){
            
    		if(lightvalue>0){
    		lightvalue--;
    		/*}else{
    			lightvalue++;
    		*/}

    	}
    	if(decider>=50 && decider <=100 )
        {
            
    		if(lightvalue<100){
    			lightvalue++;
    		/*}else{
    			lightvalue--;
    		}*/
    		
    	   }
        }

        
        /*if(decider>=20 && decider <=39){
            if(lightvalue <(100-hold)){
                lightvalue = lightvalue +hold;
            }
            else{
                lightvalue = lightvalue - hold;
            }

        }
        if(decider>=60 && decider <=79){
            if(lightvalue >(0+hold)){
                lightvalue = lightvalue -hold;
            }
            else{
                lightvalue = lightvalue + hold;
            }
        }*/
    	

    	std::this_thread::sleep_for(std::chrono::milliseconds(times));
        
    	
    
    return 0;
}
//this is the one that actually looks at the "light sensor" data
int main(){
    const char *path  = "/sys/class/backlight/rpi_backlight/brightness";
    ofstream myfile(path); 
    

	firstselection();
	
    int ctr = 0;
	while(ctr<=1000){
  
        myfile.open(path);
	   
    	if(lightvalue<40)
    	{
           myfile << 30;		       
	    }
    	if(lightvalue>=40 && lightvalue<70){

            myfile << 105;
 		}
    	if(lightvalue>=70 && lightvalue <=100)
		{

            myfile << 255;
            
		}
        
        myfile.close();
        cout<<lightvalue<<endl;
        
       manipulate();
        
    }
        

        return 0;
}
