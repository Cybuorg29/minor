public class PriorityQueue {

  private int size;
  private int[] data;

  public PriorityQueue(int capacity) {
    this.size = 0;
    this.data = new int[capacity];
  }

  public void add(int item) {
    if (this.size == this.data.length) {
      throw new IllegalStateException("The queue is full!");
    }
    this.data[this.size+1]  = item;
    this.size++;
  }

  public int peek() {
    if (this.size == 0) {
      throw new IllegalStateException("The queue is empty!");
    }
    return this.data[this.size-1];
  }

  public int poll() {
    int item = peek();
    this.data[this.size-1] = 0;
    this.size--;
    return item;
  }

  public int size() {
    return this.size;
  }

}