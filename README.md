# linux

<h2>Вопрос 1</h2>
1. r w x r- - r - -
chmod u=rwx file; chmod go=r file
chmod 744 file
2. r - - - w- - - x
chmod u=r file; chmod g=w file; chmod o=x file
chmod 421 file
3. - - x - w - r - -
chmod u=x file; chmod g=w file; chmod o=r file
chmod 124 file

<h2>Вопрос 2</h2>
У владельца файла есть права на запись и исполнение, у группы есть право на запись.

<h2>Вопрос 3</h2>
Владелец может читать, группа владельца может читать и исполнять, у всех остальных есть полный доступ.

<h2>Вопрос 4</h2>
chmod 312 file

<h2>Вопрос 5</h2>
сhmod 605 file

<h2>Вопрос 6</h2>
chmod 777 file

<h2>Вопрос 7</h2>
chmod +t filename
