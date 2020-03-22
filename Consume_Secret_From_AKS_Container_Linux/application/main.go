package main

import (
	"io/ioutil"
	"os"

	"github.com/sirupsen/logrus"
)

const (
	secretDir = "/mnt/kv"
)

// The main function
func main() {
	var log = logrus.New()
	log.Level = logrus.TraceLevel
	log.Out = os.Stdout

	data, err := ioutil.ReadFile(secretDir + "/mytestsecret")
	if err != nil {
		log.Errorf("File reading error : %w", err)
	} else {
		log.Infof("Contents of file: %s", string(data))
	}
}
