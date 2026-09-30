class StringList {
    constructor(arr) {
        this.list = arr;
    }

    filterA() {
        return this.list.filter(val => !val.includes('a'))
    }
}