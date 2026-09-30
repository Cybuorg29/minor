class Vector3d {
    double x, y, z;

    //Constructor
    Vector3d(double x, double y, double z) {
        this.x = x;
        this.y = y;
        this.z = z;
    }

    // Dot product
    double dotProduct(Vector3d vec2) {
        double result = this.x * vec2.x + this.y * vec2.y + this.z * vec2.z;
        return result;
    }

    // Normalization
    Vector3d normalize() {
        double magnitude = Math.sqrt(this.x * this.x + this.y * this.y + this.z * this.z);
        Vector3d normalized = new Vector3d(this.x / magnitude, this.y / magnitude, this.z / magnitude);
        return normalized;
    }
}