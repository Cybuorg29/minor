class Node<T> {
    var value: T
    weak var parent: Node?
    var left: Node?
    var right: Node?

    init(value: T) {
        self.value = value
    }
}

class BinarySearchTree<T: Comparable> {
    fileprivate var root: Node<T>?

    init(elements: [T]) {
        for element in elements {
            add(value: element)
        }
    }
    // Add additional functions here 
}