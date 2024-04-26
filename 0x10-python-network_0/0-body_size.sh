#!/bin/bash
# bash script for content_length body of a web page
#curl sI for sending an http request, -o for redirecting the response to index file
# then greping the lines starts with content_length in the index file
# afterwards, pip the output to awk which extracts the second word(content_length)
#printing it using echo
curl -sI "$1" -o index && content_length=$(grep -i 'Content-Length:' index | awk '{print $2}') && echo $content_length

