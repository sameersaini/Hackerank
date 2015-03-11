#include <iostream>
#include <string>

using namespace std;

int counter[26];

int main() {
  string str; cin >> str;
  for(int i = 0; i < str.length(); i++)
    counter[str[i] - 'a']++;
   int odd=0;
  for(int i = 0; i < 26; i++) {
    if(counter[i] % 2 != 0) 
    { odd++;
      if(odd==2) 
      break;
    }
  }
  if(odd>1)
      cout << "NO";
    else
        cout << "YES";
  return 0;
}
