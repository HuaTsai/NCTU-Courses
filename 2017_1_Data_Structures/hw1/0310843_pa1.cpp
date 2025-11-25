#include <fstream>
#include <iostream>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <vector>
#include <utility>
using namespace std;

vector<string> split(string str, string pattern);
void takeTargetFromStack(stack<deque<string>> &mystack,
                         queue<deque<string>> &myqueue,
                         deque<string> &deque1,
                         deque<string> &deque2,
                         int a,
                         int b);
bool combineProcess(deque<string> &deque1, deque<string> &deque2);
void pushBackProcess(stack<deque<string>> &mystack,
                     queue<deque<string>> &myqueue,
                     deque<string> &deque1,
                     bool lastmatch);
void pushBackQueue(stack<deque<string>> &mystack, queue<deque<string>> &myqueue);
void printdeque(ostream &output, deque<string> &deque1);
int main(int argc, char *argv[]) {
  ifstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open(argv[2]);
  if (!fin) {/*{{{*/
    cerr << "File could not be opened" << endl;
    return 0;
  }/*}}}*/
  stack<deque<string>> mystack;
  queue<deque<string>> myqueue;
  deque<string> deque1;
  deque<string> deque2;
  vector<string> token;
  string cur;
  int a, b;
  bool lastmatch;
  getline(fin, cur);
  while (cur != "#") {/*{{{*/
    token = split(cur, " ");
    for (int i = 0; i < token.size(); i++){
      deque1.push_front(token[i]);
    }
    mystack.push(deque1);
    deque1.clear();
    getline(fin, cur);
  }/*}}}*/
  while (fin >> a >> b) {/*{{{*/
    takeTargetFromStack(mystack, myqueue, deque1, deque2, a, b);
    lastmatch = combineProcess(deque1, deque2);
    pushBackProcess(mystack, myqueue, deque1, lastmatch);
  }/*}}}*/
  printdeque(fout, mystack.top());
  fin.close();
  fout.close();
  return 0;
}

vector<string> split(string str, string pattern) {/*{{{*/
  string::size_type pos;
  vector<string> result;
  str += pattern;
  for (int i = 0; i < str.size(); i++) {
    pos = str.find(pattern, i);
    if (pos < str.size() && i != pos) {
      string s = str.substr(i, pos - i);
      result.push_back(s);
      i = pos + pattern.size() - 1;
    }
  }
  return result;
}/*}}}*/
void takeTargetFromStack(stack<deque<string>> &mystack,/*{{{*/
                         queue<deque<string>> &myqueue,
                         deque<string> &deque1,
                         deque<string> &deque2,
                         int a,
                         int b)
{
  bool needSwap = false;
  if (a > b) {
    needSwap = true;
    swap(a,b);
  }
  for (int i = 0; i < a - 1; i++) {
    myqueue.push(mystack.top());
    mystack.pop();
  }
  deque1 = mystack.top();
  mystack.pop();
  for (int i = 0; i < b - a - 1; i++) {
    myqueue.push(mystack.top());
    mystack.pop();
  }
  deque2 = mystack.top();
  mystack.pop();
  if (needSwap) {
    deque1.swap(deque2);
  }
}/*}}}*/
bool combineProcess(deque<string> &deque1, deque<string> &deque2)/*{{{*/
{
  bool lastmatch;
  while (!deque2.empty()) {
    if (deque1.front()[0] == deque2.front()[0] ||
        deque1.front()[1] == deque2.front()[1]) {
      deque1.push_front(deque2.front());
      deque2.pop_front();
      lastmatch = true;
    }
    else {
      deque1.push_back(deque2.front());
      deque2.pop_front();
      lastmatch = false;
    }
  }
  return lastmatch;
}/*}}}*/
void pushBackProcess(stack<deque<string>> &mystack,/*{{{*/
                     queue<deque<string>> &myqueue,
                     deque<string> &deque1,
                     bool lastmatch)
{
  if (lastmatch) {
    mystack.push(deque1);
    pushBackQueue(mystack, myqueue);
  }
  else {
    pushBackQueue(mystack, myqueue);
    mystack.push(deque1);
  }
}/*}}}*/
void pushBackQueue(stack<deque<string>> &mystack, queue<deque<string>> &myqueue)/*{{{*/
{
  while (!myqueue.empty()) {
    mystack.push(myqueue.front());
    myqueue.pop();
  }
}/*}}}*/
void printdeque(ostream &output, deque<string> &deque1)/*{{{*/
{
  deque<string>::iterator it = deque1.begin();
  while (it != deque1.end())
    output << *it++ << ' ';
}/*}}}*/
