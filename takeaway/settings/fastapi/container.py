container = '''
#!bin/bash
# # docker rmi $(docker images -a -q) 
# # docker rm $(docker ps -a -f status=exited -q)
# # docker rmi $(docker images -q -f dangling=true)

# imgs=$(docker images | awk '/<none>/ { print $3 }')
# if [ "${imgs}" != "" ]; then
#    echo docker rmi ${imgs}
#    docker rmi ${imgs}
# else
#    echo "No images to remove"
# fi

# procs=$(docker ps -a -q --no-trunc)
# if [ "${procs}" != "" ]; then
#    echo docker rm ${procs}
#    docker rm ${procs}
# else
#    echo "No processes to purge"
# fi


# # # Delete all stopped containers (including data-only containers).
# # docker ps -a -q --no-trunc --filter "status=exited" | xargs --no-run-if-empty docker rm -v

# # # Delete all tagged images more than a month old
# # # (will fail to remove images still used).
# # docker images --no-trunc --format '{{.ID}} {{.CreatedSince}}' | grep ' months' | awk '{ print $1 }' | xargs --no-run-if-empty docker rmi || true

# # # Delete all 'untagged/dangling' (<none>) images
# # # Those are used for Docker caching mechanism.
# # docker images -q --no-trunc --filter dangling=true | xargs --no-run-if-empty docker rmi

# # # Delete all dangling volumes.
# # docker volume ls -qf dangling=true | xargs --no-run-if-empty docker volume rm



# Remove all the dangling images
DANGLING_IMAGES=$(docker images -qf "dangling=true")
if [[ -n $DANGLING_IMAGES ]]; then
    docker rmi "$DANGLING_IMAGES"
fi

procs=$(docker ps -a -q --no-trunc)
if [ "${procs}" != "" ]; then
   echo docker rm ${procs}
   docker rm ${procs}
else
   echo "No processes to purge"
fi


STALLED_IMAGES=$(docker images  | awk -v proj=$CI_PROJECT_NAME '$0 ~ proj || $1 ~ /none/{print $3}')
if ! test -z "$STALLED_IMAGES";
   then
      docker rmi -f $STALLED_IMAGES
fi


# # Get all the images currently in use
# USED_IMAGES=($( \
#     docker ps -a --format '{{.Image}}' | \
#     sort -u | \
#     uniq | \
#     awk -F ':' '$2{print $1":"$2}!$2{print $1":latest"}' \
# ))

# # Get all the images currently available
# ALL_IMAGES=($( \
#     docker images --format '{{.Repository}}:{{.Tag}}' | \
#     sort -u \
# ))

# # Remove the unused images
# for i in "${ALL_IMAGES[@]}"; do
#     UNUSED=true
#     for j in "${USED_IMAGES[@]}"; do
#         if [[ "$i" == "$j" ]]; then
#             UNUSED=false
#         fi
#     done
#     if [[ "$UNUSED" == true ]]; then
#         docker rmi "$i"
#     fi
# done
'''