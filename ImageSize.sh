#!/bin/bash


# function die() {
# echo -e "${1}"
# exit 1
# }

# # check that user entered proper number of args
# if [[ "${#}" -ne "1" ]]
# then
# die "Usage: $0 <image>"
# fi

# IMAGE="${1}"

# # check that file exists
# if [[ ! -f "${IMAGE}" ]]
# then
# die "File not found: ${IMAGE}"
# fi

# # grab the identify string, make sure it succeeded
# IMG_CHARS=$(identify "${IMAGE}" 2> /dev/null) || die "${IMAGE} is not a proper image"

# # grab width and height
# IMG_CHARS=$(echo "${IMG_CHARS}" | sed -n 's/\(^.*\)\ \([0-9]*\)x\([0-9]*\)\ \(.*$\)/\2 \3/p')

# WIDTH=$(echo "${IMG_CHARS}" | awk '{print $1}')
# HEIGHT=$(echo "${IMG_CHARS}" | awk '{print $2}')


# echo -e "W: ${WIDTH} H: ${HEIGHT}"
echo 'test'