package main

import "fmt"

func main() {
    var str string
    fmt.Printf("Enter a string: ")
    fmt.Scanf("%s\n", &str)
    fmt.Printf("The reverse of the string is %s\n", reverse(str))
}

func reverse(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}