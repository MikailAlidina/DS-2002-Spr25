#!/bin/bash

if [ "$#" -ne 3 ]; then
	echo "Use: $0 <local_file> <name_of_bucket> <expiration_in_seconds>"
	exit 1
fi

local_file=$1
bucket=$2
expiration=$3

echo "Adding $local_file to s3://$bucket/"
aws s3 cp "$local_file" "s3://$bucket/"

echo "Presigning a url for $expiration seconds"
aws s3 presign --expires-in "$expiration" "s3://$bucket/$local_file"