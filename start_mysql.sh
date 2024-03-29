#!/bin/bash

function main {
	set -e

	start_mysql
	import_anonymous_data
}

function start_mysql {
	docker-compose up --detach
}

function import_anonymous_data {
	TMP_DIR=$(mktemp -d -t serlo-anonymous-dataXXXXXX)
	TMP_DUMP="${TMP_DIR}/dump.zip"
	LATEST_DUMP=$(gsutil ls -l gs://anonymous-data \
		| grep dump \
		| sort -rk 2 \
		| head -n 1 \
		| awk '{ print $3 }')

	gsutil cp "${LATEST_DUMP}" "${TMP_DUMP}"
	unzip -d "${TMP_DIR}" "${TMP_DUMP}"

	exec_mysql serlo < "${TMP_DIR}/mysql.sql"
	docker cp "${TMP_DIR}/user.csv" $(docker-compose ps -q mysql):/
	exec_mysql -e "LOAD DATA LOCAL INFILE 'user.csv' INTO TABLE user \
	               FIELDS TERMINATED BY '\t' LINES TERMINATED BY '\n' \
	               IGNORE 1 ROWS;" serlo

	rm -r ${TMP_DIR}
}

function exec_mysql {
	docker-compose exec -T mysql mysql --user=root --password=secret "$@"
}

main
