package main

import (
	"bufio"
	"fmt"
	"os"
)

func greet(name string) string {
	return "Hello, " + name + "!"
}

func main() {
	reader := bufio.NewReader(os.Stdin)
	fmt.Print("Enter your name: ")
	name, _ := reader.ReadString('\n')
	name = name[:len(name)-1] // Remove the newline character
	fmt.Print("Enter your favorite programming language: ")
	lang, _ := reader.ReadString('\n')
	lang = lang[:len(lang)-1] // Remove the newline character
	message := greet(name)
	fmt.Println(message)
	fmt.Printf("It's great that you like %s!\n", lang)
}
