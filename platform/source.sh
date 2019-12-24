#!/bin/sh

cd auto/onsystemd
f=`find -name \*.service`

for file in $f
do
  file="$(basename "$file")"
  echo "Обработка сервиса автозапуска: ${file}"
  sudo chmod 644 $file
  echo "Перемещение сервиса в /lib/systemd/system/"
  sudo cp $file /lib/systemd/system/
  sudo systemctl daemon-reload
  sudo systemctl enable $file
  #sudo systemctl start $file
done

echo "Все сервисы обработаны, перезагрузите ОС для их запуска"



