#include <iostream>
#include <string>
#include <vector>
using namespace std;

vector<string> split(string str, string pattern) {
  string::size_type pos;
  vector<string> result;
  str += pattern;
  for (int i = 0; i < str.size(); i++) {
    pos = str.find(pattern, i);
    if (pos < str.size()) {
      string s = str.substr(i, pos - i);
      result.push_back(s);
      i = pos + pattern.size() - 1;
    }
  }
  return result;
}

int main() {
  string str;
  cout << "Please input str: " << endl;
  getline(cin, str);
  string pattern(" ");
  vector<string> result = split(str, pattern);
  cout << "The result: " << endl;
  for (int i = 0; i < result.size(); i++) {
    cout << result[i] << endl;
  }
  return 0;
}
