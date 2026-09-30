class Point2D {
   private:
     double x;
     double y;
   public:
     Point2D(double x_coordinate, double y_coordinate);
     double get_x();
     double get_y();
};

Point2D::Point2D(double x_coordinate, double y_coordinate) {
   x = x_coordinate;
   y = y_coordinate;
}

double Point2D::get_x() {
   return x;
}

double Point2D::get_y() {
   return y;
}