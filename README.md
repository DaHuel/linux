# linux

<h2>Вопрос 1</h2>

history 4

<h2>Вопрос 2</h2>
bg

<h2>Вопрос 3</h2>
Ctrl+Alt+F4

<h2>Вопрос 4</h2>
PWD

<h2>Вопрос 5</h2>
export MYVAR

<h2>Вопрос 6</h2>
Tab, Ctrl+I

<h2>Вопрос 7</h2>
$VAR

<h2>Вопрос 8</h2>
 /etc

<h2>Вопрос 9</h2>
 2
 
 <h2>Задача</h2>
 
``` 
#!/bin/bash
let A=$1-1
let B=$2-1
for ((i = 0; i < $1; i++)); do
   for ((j = 0; j < $2; j++)); do
   	if [ $i -eq 0 -o $i -eq $A ] 
   		then
   		echo -n $4
   	else 
   		if [ $j -eq 0 -o $j -eq $B ] 
   			then
   			echo -n $4
   		else					
   			if [ $3 -eq 0 ]
   				then
   				echo -n " "
   			else echo -n $4
   			fi
   		fi
   	fi
   done
   echo ''
done
```
