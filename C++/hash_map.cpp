// hash_map
#include <iostream>
#include <unordered_map>
using namespace std;
int main(){
    unordered_map<char, int> m;
    m['a'] = 1;
    m['b'] = 2;
    cout << m.find('a') -> first << endl;
    cout << m.find('a') -> second;
}