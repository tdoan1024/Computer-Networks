//Tai Doan
//Computer Networks
//Warm up assignment
//C++

#include <iostream>
#include <string>
#include <fstream>
#include <cctype>
#include <map>

using namespace std;

void Hello() {
  string name;
  cout << "What's your name?";
  cin >> name;
  cout << endl;
  cout <<"Hello "<<name<<", nice to meet you!"<<endl;
}

void LowerLine() {
  string fileName;
  cout << "Enter file name: ";
  cin >> fileName;
  cout << endl;
  ifstream inFile(fileName);
  if (inFile.fail()) {
    cerr << "Your file did not work" << endl;
    exit(1);
  }
  string line;
  string text;
  cout << "OG line: " << line<< endl;
  cout << "OG text: " << text<<endl;
  while (inFile >> line) {
    text+=line;
  }
  cout << "Text: ";
  for (int i=0;i<text.length();i++)
    text.at(i) = tolower(text.at(i));
  cout << text << endl;
  char character[36];
  int freq[36]={0};

  for (int i =0;i<26;i++)
    character[i] = char(i+97);
  for (int j=26;j<36;j++)
    character[j] = char(j+22);
  cout << endl;

  for (int i=0;i<text.length();i++) {
    for (int j=0;j<36;j++) {
      if (text.at(i) == character[j]) {
        freq[j]++;
      }
    }
  }

  for (int i=0;i<36;i++) {
    cout << character[i] << " " << freq[i] << endl;
  }

  inFile.close();
}

int* ReverseArray(int array[],int size) {
  int* revArray = new int[size];
  for (int i = size;i>0;i--) {
    revArray[size-i] = array[i-1];
  }
  return revArray;
}

struct Node {
  int data;
  struct Node* next;
};

void insert(struct Node** head, int newData) {
  struct Node* nNode = new Node;
  nNode->data = newData;
  nNode->next = *head;
  *head = nNode;
}

int CheckCycleList(struct Node *l) {
  if (l == nullptr)
    return 1;
  struct Node *slow = l ,*fast=l;
  while (slow && fast && fast->next) {
    slow = slow->next;
    fast = fast->next->next;
    if (slow == fast) {
      return 1;
    }
  }
  return 0;
}



int main() {
  //Test function Hello()
  Hello();

  //Test function LowerLine
  //file name is "Fn2Text.txt"
  LowerLine();

  //Test function ReverseArray()
  int test[5] = {1,2,3,5,6};
  int size = sizeof(test)/sizeof(test[0]);
  int* rev = ReverseArray(test,size);
  cout << "Original array: ";
  for (int i=0;i<size;i++)
    cout << test[i] << " ";
  cout << endl << "Reversed Array: ";
  for (int i=0;i<size;i++)
    cout << rev[i] << " ";
  cout << endl;

  //Test function CheckCycleList()
  struct Node*head = nullptr;
  insert(&head,1);
  insert(&head,3);
  insert(&head,5);
  insert(&head,7);

  head->next->next->next = head; //this is a cycle linked list
  int result = CheckCycleList(head);
  if(result == 0)
      cout<< "Not a cycle linked list" << endl;
  else
      cout<< "This is a cycle linked list" << endl;

  return 0;
}
