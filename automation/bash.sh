#!/bin/bash

printf "cURL examples and playground :)\n"

# Check if there were any arguments passed
if [ $# -eq 0 ]
then
    echo "No options selected, please choose at least one from 'GET', 'POST', 'PUT', and 'DELETE'."
    exit
fi

# Loop through all the arguments provided
for argument in $@
do
    if [ "$argument" == "GET" ]
    then
        # GET
        echo "Executing GET..."
        GET=$(curl -s -X GET https://jsonplaceholder.typicode.com/users)
        echo $GET | jq '. | map({id: .id, name: .name, email: .email, company: .company.name})'
    elif [ "$argument" == "POST" ]
    then
        # POST
        echo "Executing POST..."
        POST=$(curl -s -X POST https://jsonplaceholder.typicode.com/posts -H 'Content-Type: application/json' -d '{"title":"My new post", "body":"Lorem ipsom style beat", "userId": 1}')
        echo $POST | jq '. | {"message":"success", "id": .id, "title": .title, "body": .body}'
    elif [ "$argument" == "PUT" ]
    then
        # PUT
        echo "Executing PUT..."
        PUT=$(curl -s -X PUT https://jsonplaceholder.typicode.com/posts/$(shuf -i1-10 -n1) -H 'Content-Type: application/json' -d '{"title":"My new post", "body":"Lorem ipsom style beat", "userId": 2, "id": 1}')
        echo $PUT | jq '. | {"message":"success", "id": .id, "title": .title, "body": .body}'
    elif [ "$argument" == "DELETE" ]
    then
        # DELETE
        echo "Executing DELETE..."
        echo "What ID would you like to delete? 1-10"
        read id
        if [[ $id =~ ^[0-9]+$ ]]
        then
            DELETE=$(curl -s -w "%{http_code}" -o /dev/null -X DELETE 'https://jsonplaceholder.typicode.com/posts/$id')
            echo \{\"status_code\"\:$DELETE\,\"status\"\:\"$([[ $DELETE == 200 ]] && echo "success" || echo "failed")\"\} | jq '.'
        else
            echo "Not a valid ID, it has to be a number!"
        fi
    else
        echo "Wrong options selected, please choose at least one from 'GET', 'POST', 'PUT', and 'DELETE'."
    fi
done