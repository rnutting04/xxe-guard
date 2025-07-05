package main

import (
	"encoding/xml"
	"fmt"
	"os"
)

type Note struct {
	XMLName xml.Name `xml:"note"`
	To      string   `xml:"to"`
	From    string   `xml:"from"`
	Heading string   `xml:"heading"`
	Body    string   `xml:"body"`

}

func main() {
	note := Note{
		To:      "Alice",
		From:    "Bob",
		Heading: "Reminder",
		Body:    "Don't forget the meeting at 10 AM.",
	}

	file, err := os.Create("note.xml")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	encoder := xml.NewEncoder(file)
	encoder.Indent("", "  ")

	if err := encoder.Encode(note); err != nil {
		panic(err)
	}

	fmt.Println("note.xml written successfully")
}

