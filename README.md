<b> vk_public_skillbox_analysis </b> 
# Parcing of the VK-public of Skillbox and analysis for recomendations for SMM
<br> For Russian scroll down
### The task
To perform analytics of the VK-public of Skillbox to produce recomendations for the SMM-department. 
### What has been made?
<br> I have parced a public page of Skillbox - this is an online-education company - and analyses retrived data, using pandas.
<br> I have parced a bit more than 1000 posts in this public and extracted this data about each of them:
<br>time of the publication
<br>text
<br>attachments type and number
<br>topic of the text
<br>number of comments, likes, views and reposts
### During the work I have used tools:
<br>VK-API 
<br>requests module
<br>pandas
<br>matplotlib
<br>regular expressions 
### What are the main conclusions I have produced?
<br>1. During the weekend users are more active per one post and their activity is the highest between 11am and 3pm. 
<br>2. During the work-days users are the most active on the lunch time (1pm) and in the evening rush-hour (after 6pm).
<br>3. During the work-days users like text of length of approximately 120-220 words. At the weekend it is better to post texts up to 150 words. 
<br>4. Users like posts with photos and links. They like posts with video mostly at weekends and during lunch-time and rush-hour in work_days, the same for posts with documents. 
<br>5. The most favourable topics are: кейс, в закладки, вдохновляют (these are 3 the most popular topics in Russian language). 
<br>6. Also I have retrived the most likeable and shared posts and advised SMM to pay attention to them. 

# Парсинг паблика компании Skillbox в VK с целью анализа полученных данных и подготовки рекомендаций для SMM
### Что было сделано? 
<br> Я спарсила чуть более 1000 постов в паблике и извлекла такие данные о каждом посте:
<br>время публикации
<br>текст
<br>тип и количество вложений 
<br>тема текста
<br>количество комментариев, репостов, лайков и просмотров
### В ходе работы я использовала инструменты:
<br>VK-API 
<br>requests module
<br>pandas
<br>matplotlib
<br>regular expressions 
### Какие основные выводы я сделала? 
<br>1. В выходные пользователи проявляют больше активностей на один пост, чем в будни, и при этом они наиболее активны с 11.00 до 15.00. 
<br>2. В будни пользователи наиболее активны в обед (13.00) и в вечерний час пик (после 18.00).
<br>3. В будни лучше постить тексты длиной от 120 до 220 слов, а в выходные больше "заходят" тексты длиной до 150 слов. 
<br>4. Пользователям нравятся посты с фотографиями и ссылками. Посты с видео и документами нравятся больше в выходные и в течение обеда в будни. 
<br>5. Наиболее популярные темы постов: кейс, в закладки, вдохновлят. 
<br>6. Также я выявила наиболее популярные посты и посоветовала обратить на них внимание. 


