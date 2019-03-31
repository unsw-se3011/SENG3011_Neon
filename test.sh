#!/bin/bash

if [ ! -f output.txt ]; then
    touch output.txt
fi

echo "--------------------time for requesting reports http://localhost:8000/v0/reports/: 	-------------------------"  > output.txt
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/v0/reports/" >> output.txt

echo "--------------------time for requesting articles http://localhost:8000/v0/articles/: 	-------------------------" >> output.txt
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/v0/articles/" >> output.txt

echo "--------------------time for requesting location http://localhost:8000/v0/location/: 	-------------------------" >>output.txt
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/v0/location/" >> output.txt

echo "--------------------time for requesting diseases http://localhost:8000/v0/diseases/: 	-------------------------" >>output.txt
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/v0/diseases/" >> output.txt

echo "--------------------time for requesting syndromes http://localhost:8000/v0/syndromes/: 	-------------------------" >>output.txt
curl -w "@curl-format.txt" -o /dev/null -s "http://localhost:8000/v0/syndromes/" >> output.txt


echo "------------------time for requesting registration http://localhost:8000/v0/syndromes/: 	---------------" >>output.txt
curl -w "@curl-format.txt" -o /dev/null -s\
  --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"Toby","password":"toby","first_name":"Huang","last_name":"Toby"}' \
  http://localhost:8000/v0/users/  \ >> output.txt

printf "\n" >>output.txt
echo "------------------time for requesting login http://localhost:8000/v0/syndromes/: 	----------------" >>output.txt
curl -w "@curl-format.txt" -o /dev/null -s\
  --header "Content-Type: application/json" \
  --request GET \
  --data '{"username":"ttt","password":"apple123"}' \
  http://localhost:8000/v0/users/  \ >> output.txt
  
printf "\n all outputs are stored in output.txt\n"

rm output.txt