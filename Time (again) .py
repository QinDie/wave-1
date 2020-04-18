time =int(input("seconds="))

day = time //86400
hour = (time-day*86400)//3600
minute =( time -day*86400-hour *3600 )//60
second =time -day*86400 -hour *3600- minute*60

print(f'{day }: {"%02d "% hour}:{"%02d " % minute} : { "%02d"% second }' ) 