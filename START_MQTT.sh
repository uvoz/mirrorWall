PATH_LOG="log_mqtt.txt"

echo -n `date` >> $PATH_LOG
echo ": bash started">> $PATH_LOG 
while true
do
	echo - `date` >> $PATH_LOG
	echo ": mqtt started" >> $PATH_LOG
	hostname -I
	mosquitto -v -p 1883 >> $PATH_LOG
done
echo -n `date` >> $PATH_LOG
echo ": bash end">> $PATH_LOG
