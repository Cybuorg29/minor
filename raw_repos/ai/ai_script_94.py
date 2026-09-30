class Point {
 public:
  Point(int x, int y) : x_(x), y_(y) {}

  int getX() const { return x_; }
  int getY() const { return y_; }

  int getSum() const { return x_+ y_; }

 private:
  int x_, y_;
}

int main() {
  Point p(3, 4);
  cout << p.getSum() << endl;
  
  return 0;
}