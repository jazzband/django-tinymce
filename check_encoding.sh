#!/usr/bin/env bash
STATICS='tinymce/static/'


FULLPATH=$(cd $(dirname "$STATICS"); pwd)/$(basename "$STATICS")

echo -en "Checking files in $FULLPATH\r"

find "$FULLPATH" -type f -exec file {} \; | egrep -v "(ASCII|GIF|PNG|JPEG|Flash|UTF-8)"

if [ "$?" -ne 1 ]; then
    echo "Please check encoding of files listed above."
    exit 1
fi
echo "Encoding of '$FULLPATH' files checked. Status OK."
exit 0
