#!/bin/bash
export COMPOSE_PROJECT_NAME=chat_${CI_COMMIT_SHA}
docker-compose -f docker/compose/test.yml run chat unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
