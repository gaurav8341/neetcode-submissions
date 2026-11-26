#include<string> // this is for cpp string
#include <cstring> // this is for c string
#include<unordered_map>

using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if(strlen(s.c_str()) != strlen(t.c_str())){
            return false;
        }
        unordered_map<char, int> s_freq, t_freq;

        for(int i = 0; i < strlen(s.c_str()); i++){
            s_freq[s[i]]++;
            t_freq[t[i]]++;
        }

        return s_freq == t_freq;


    }
};