#!/bin/bash
DATE=`date +%Y-%m-%d-%H-%M-%S`
ARCHIVE=${DATE}-users.sql.gz.enc
MYSQLINFO=~/.mysqldump
DATABASE=ansibletest
DUMPPATH=~/ansible-homeassignment/dbbackups
PUBLIC_KEY=~/mysqldump-key.pub.pem
mysqldump --defaults-extra-file=${MYSQLINFO} ${DATABASE} --single-transaction --routines --events --triggers \
  | gzip -c \
  | openssl smime -encrypt -binary -text -aes256 -out ${DUMPPATH}/${ARCHIVE} -outform DER ${PUBLIC_KEY}

cd ${DUMPPATH}
git add ${ARCHIVE}
git commit -m "$DATE backup done" && git push
