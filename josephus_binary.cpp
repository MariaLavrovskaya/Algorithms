#include <bit>
#include <bitset>
#include <cstdint>
#include <iostream>
#include <limits>
#include <ios>
#include <sstream>
#include<cmath>

using namespace std;


int msbBitValue(unsigned long n) {
   int k = (int)(log2(n));
   return k;
}


int main() {
    int participants; //number of participants
    int msb; //leftomost significant bit
    unsigned long auxiliary; //interim binary number to perform AND operator to switch 1 to 0
    unsigned long interim_value; //the value that stores the result before the final one
    unsigned long winner; //stores result
    std::string  sparticipants; //string of participants to securely take input 

    cout << "Enter the number of participants: " ;
    std::getline(std::cin, sparticipants); // getting input from the user
    std::stringstream numberline(sparticipants);
    numberline >> participants;

    msb = msbBitValue(participants);
    std::cout << "MSB bit value is: " << msbBitValue(participants) << "\n"; //outputting the number of a digit that we should set to 1
    auxiliary = participants; //pass-by-value copy
    auxiliary ^= 1UL << msb; //changing the index with XOR operation 
    interim_value = (participants & auxiliary); // switching the value to the 0
    winner = interim_value << 1; // shifting the leftmost bit to the right
    winner ^= 1UL << 0; // toggling the last bit, set to 1
    std::bitset<8> winner_inbits(winner);
    
    std::cout << "Winner of the game: " << winner << "\n" << " Winner value bits : " << winner_inbits;
    }
