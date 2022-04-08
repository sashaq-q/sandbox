#include <iostream>
using namespace std;
class Queue {
  int size;
  int* queue;
  
  public:
  Queue(){
    size = 0;
    queue = new int[111]
  }
  
  void add(int data) {
    queue[size] = data;
    size++;
  }
  
  void remove() {
    if (size==0) {
      cout << "Queue is empty" <<endl;
      return;
    }
    else {
      for (int i=0; i<size-1; i++) {
        queue[i] = queue[i+1];
      }
      size--;
    }
  }
  
  void print() {
    if (size==0) {
      cout << "Queue is empty" <<endl;
      return;
    }
    for (int i=0; i<size; i++) {
      cout << queue[i] <<" .. ";
    }
    cout << endl;
  }
  
  Queue operator+(Queue &q) {
    Queue sum;
    for (int i=0; i<this->size; i++) {
      sum.add(this->queue[i]);
    }
    for (int i=0; i<q.size; i++) {
      sum.add(q.queue[i]);
    }
    return sum;
  }
}

int main() {
  Queue q1;
  q1.add(777); q1.add(7); q1.add(77);
  Queue q2;
  q2.add(1); q2.add(3); q2.add(5); q2.add(7);
  Queue q3 = q1+q2;
  q3.print();
  
  return 0;
}
