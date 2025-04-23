import os
import smtplib
from dotenv import load_dotenv
load_dotenv()

login = os.getenv("LOGIN")
password = os.getenv("PASS")

invite_letter = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''

invite_letter = invite_letter.replace('%my_name%', 'Дмитрий')
invite_letter = invite_letter.replace('%friend_name%', 'Иван')
invite_letter = invite_letter.replace('%website%', 'https://dvmn.org/profession-ref-program/jackimov.dima/NPCGg/')

email_send = 'jackimov.dima@yandex.ru'
emeil_recip = 'dimasssikd@icloud.com'
email_sub = 'Приглашение!'

letter = '''From: {e_send}
To: {e_rec}
Subject: {e_sub}
Content-Type: text/plain; charset="UTF-8";

{inv_let}'''.format(e_send=email_send, e_rec=emeil_recip, e_sub=email_sub, inv_let=invite_letter)

letter = letter.encode("UTF-8")

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
server.login(login, password)
server.sendmail(email_send, emeil_recip, letter)
server.quit()