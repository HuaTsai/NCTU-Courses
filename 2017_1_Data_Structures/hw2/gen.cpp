#include <iostream>
#include <cstdlib>
#include <ctime>
#include <fstream>
using namespace std;
int main(int argc, char *argv[]) {
  ofstream fout;
  fout.open(argv[1]);
  srand(time(NULL));
  int c, n, x, y;
  x = rand() % 15 + 3;
  for (int i = 0; i < x; i++) {
    fout << rand() % 100 + 5 << " ";
  }
  fout << "-9" << endl;
  for (int i = 0; i < x-1; i++) {
    y = rand() % 10 + 5;
    for (int j = 0; j < y; j++) {
      fout << (char)(rand() % 26 + 'a');
    }
    fout << endl;
  }

  return 0;
}
