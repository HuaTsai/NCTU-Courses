#include <iostream>
#include <fstream>
#include <list>
using namespace std;

enum {CLOCKWISE, COUNTERCLOCKWISE} order;
class Node {/*{{{*/
  public:
    Node(int id, string letter):id(id), letter(letter){}
    ~Node(){}
    int getid();
    string getletter();
    void addletter(char, string);
  private:
    int id;
    string letter;
};/*}}}*/
int Node::getid() {/*{{{*/
  return id;
}/*}}}*/
string Node::getletter() {/*{{{*/
  return letter;
}/*}}}*/
void Node::addletter(char c, string from) {/*{{{*/
  if (from == "back") {
    letter += c;
  } else if (from == "front") {
    letter = c + letter;
  }
}/*}}}*/

bool isvowel(char);
void callTheWord(list<Node> &, list<Node>::iterator &, string);
void changeOrderIfNeed(string);
void oneOutFromGame(list<Node> &, list<Node> &, list<Node>::iterator &);
void putItToNextPlace(list<Node> &, list<Node>::iterator &);

int main(int argc, char *argv[]) {
  ifstream fin;
  ofstream fout;
  fin.open(argv[1]);
  fout.open(argv[2]);
  list<Node> mylist;
  list<Node> result;
  list<Node>::iterator it;
  int start, num;
  order = CLOCKWISE;
  string str;
  fin >> start;
  while (fin >> num && num > -1) {
    mylist.push_back(Node(num, str));
  }
  it = mylist.begin();
  while (it->getid() != start) {
    it++;
  }
  while (fin >> str) {
    callTheWord(mylist, it, str);
    changeOrderIfNeed(str);
    oneOutFromGame(mylist, result, it);
  }
  result.push_back(*it);
  for (it = result.begin(); it != result.end(); it++) {
    fout << it->getid() << " " << it->getletter() << endl;
  }
  fin.close();
  fout.close();

  return 0;
}
bool isvowel (char c) {/*{{{*/
  switch(c) {
    case 'A':
    case 'a':
    case 'E':
    case 'e':
    case 'I':
    case 'i':
    case 'O':
    case 'o':
    case 'U':
    case 'u':
      return true;
      break;
    default:
      return false;
  }
}/*}}}*/
void callTheWord(list<Node> &mylist, list<Node>::iterator &it, string str) {/*{{{*/
  for (int i = 0; i < str.size()-1; i++) {
    if (order == CLOCKWISE) {
      it->addletter(str[i], "back");
    }
    else if (order == COUNTERCLOCKWISE) {
      it->addletter(str[i], "front");
    }
    putItToNextPlace(mylist, it);
  }
  if (order == CLOCKWISE) {
    it->addletter(str[str.size()-1], "back");
  } else if (order == COUNTERCLOCKWISE) {
    it->addletter(str[str.size()-1], "front");
  }
}/*}}}*/
void changeOrderIfNeed(string str) {/*{{{*/
  if (!isvowel(str[str.size()-1])) {
    if (order == CLOCKWISE) {
      order = COUNTERCLOCKWISE;
    } else {
      order = CLOCKWISE;
    }
  }
}/*}}}*/
void oneOutFromGame(list<Node> &mylist, list<Node> &result, list<Node>::iterator &it) {/*{{{*/
  result.push_back(*it);
  it = mylist.erase(it);
  if (order == CLOCKWISE) {
    it--;
  }
  putItToNextPlace(mylist, it);
}/*}}}*/
void putItToNextPlace(list<Node> &mylist, list<Node>::iterator &it) {/*{{{*/
  if (order == CLOCKWISE) {
    it++;
    if (it == mylist.end()) {
      it = mylist.begin();
    }
  }
  else if (order == COUNTERCLOCKWISE) {
    if (it == mylist.begin()) {
      it = mylist.end();
    }
    it--;
  }
}/*}}}*/
