#! /bin/bash


date_echo() {
    echo `date '+%Y-%m-%d %H:%M:%S'` '[+] '$1'...'
}

# Backup a file or lots of files  under the same directory
backup() {
    for filename in "$@"; do
        if [ -f $filename ]; then
            date_echo "Backing up <$filename> to <$filename.bk>"
            cp $filename{,.bk}
        else
            date_echo "File <$filename> does not exist. Skip"
        fi
    done
}

