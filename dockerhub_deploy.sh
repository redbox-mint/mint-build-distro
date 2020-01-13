#! /bin/bash
cd support/docker/
docker cp $(docker ps -l -q):/build/src/target ./
find ./target -name 'mint-*.tar.gz' | xargs -I % cp % ./mint.tar.gz
docker login -u $DOCKER_USER -p $DOCKER_PASS
export REPO=qcifengineering/mint
docker pull $REPO
export TAG=`if [ "$TRAVIS_BRANCH" == "master" ]; then echo "latest"; else echo $TRAVIS_BRANCH; fi`
docker build -f Dockerfile -t $REPO:$TRAVIS_COMMIT .
docker tag $REPO:$TRAVIS_COMMIT $REPO:$TAG
docker tag $REPO:$TRAVIS_COMMIT $REPO:travis-$TRAVIS_BUILD_NUMBER
docker push $REPO
