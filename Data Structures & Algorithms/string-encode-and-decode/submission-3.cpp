class Solution {
public:
    string encode(vector<string>& strs) {
        string encoded = "";
        for (int i = 0; i < strs.size(); i++) {
            encoded += to_string(strs[i].size()) + "#" + strs[i];
        }
        return encoded;
    }

    vector<string> decode(string s) {
        vector<string> res;
        int i = 0;
        
        while (i < s.size()) {
            int j = i;
            // Move j forward until it hits the '#' delimiter
            while (s[j] != '#') {
                j++;
            }
            
            // Extract the number before the '#' and convert to integer
            int length = stoi(s.substr(i, j - i));
            
            // Extract the actual word based on the length we just found
            res.push_back(s.substr(j + 1, length));
            
            // Jump 'i' forward past the word we just read to start the next one
            i = j + 1 + length;
        }
        
        return res;
    }
};