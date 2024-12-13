package main

import (
	"fmt"
	// "io"
	"os"
	// "strconv"
	"bufio"
)

func main(){
	reader := bufio.NewReader(os.Stdin)
	text, _ := reader.ReadString('\n')
	fmt.Println(text)
}