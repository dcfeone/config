#!/bin/sh

# echo "w3m-control: BACK"
# # echo "w3m-control: TAB_GOTO https://www.google.com/search?q=$QUERY_STRING"
# echo "w3m-control: GOTO https://www.google.com/search?q=$QUERY_STRING"
url="$(cat /var/share/fileu)"

# set open-url value to zero (aka empty url line)
# printf "%s\r\n" "W3m-control: SET_OPTION default_url=0"

#GOTO url in clipboard in current page. If the clipboard has a
#"non url string/nothing" an blank page is shown.
printf "%s\r\n" "W3m-control: TAB_GOTO $url"
