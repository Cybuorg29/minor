class Point {
    private:
        int x, y;
    public: 
        Point(int x, int y) : x{x}, y{y} {};

        Point operator + (const Point& other) {
            return Point(this->x + other.x, this->y + other.y);
        }
};