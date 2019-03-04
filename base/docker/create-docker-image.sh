#!/bin/bash

PROJECT_ID=$(gcloud config get-value project 2>/dev/null)

IMAGE_VERSION=""


main()
{
	IMAGE_NAME="gcr.io/${PROJECT_ID}/endpoints-image:${IMAGE_VERSION}"
	echo "Creating docker image with name $IMAGE_NAME ..."
	docker build -t $IMAGE_NAME .

	echo -e "\nPushing image to gcr.io ..."
	docker push $IMAGE_NAME

	echo -e "\nDONE"
	echo "Buit image $IMAGE_NAME"
	echo "Run the following command to test it locally:"
	echo -e "\ndocker run --rm -p 8080:8080 $IMAGE_NAME \n"
}





while test $# -gt 0; do
	case $1 in
		-h | --help)
			echo "options:"
			echo "-h, --help		show help and optional arguments"
			echo "-v, --version=VERSION	specify a version to build with docker"
			exit 0
			;;
		-v)
			shift
			IMAGE_VERSION=$1
			main
			exit 0
			;;
		--version*)
			IMAGE_VERSION=`echo $1 | sed -e 's/^[^=]*=//g'`
			main
			exit 0
			;;
		*)
			main
			exit 0
			;;
	esac
done
