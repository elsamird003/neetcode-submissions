class Solution {
public:
    bool isValid(string s) {
        size_t pos;
        while (true) {
            // Logic: find a pair, delete it, start over.
            if ((pos = s.find("()")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            // Fixed parentheses here:
            if ((pos = s.find("{}")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            // And fixed here:
            if ((pos = s.find("[]")) != string::npos) {
                s.erase(pos, 2);
                continue;
            }
            break;
        }
        return s.empty();
    }
};