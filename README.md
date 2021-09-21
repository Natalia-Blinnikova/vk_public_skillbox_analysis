<b> vk_public_skillbox_analysis </b> 
# Parcing of the VK-public of Skillbox and analysis for recomendations for SMM
<br> For Russian scroll down
### What has been made?
<br> I have parced a public page of Skillbox - this is a online-education company - and analyses retrived data, using pandas.
<br> I have parced a bit more than 1000 posts in this public and extracted this data about each of them:
* time of the publication
* text
* attachments type and number
* topic of the text
* number of comments, likes, views and reposts
### During the work I have used tools:
* VK-API 
* requests module
* pandas
* matplotlib
* regular expressions 
### What are the main recomendations I have produced?
* There is a difference in users activity during work-days and weekend, thus I have analysed these periods separetely. 
* During the weekend users are more active per one post and their activity is the highest between 11am and 3pm. 
* During the work-days users are the most active on the lunch time (1pm) and in the evening rush-hour (after 6pm).
* During the work-days users like text of length of approximately 120-220 words. At the weekend it is better to post texts up to 150 words. 
* Users like posts with photos and links. They like posts with video mostly at weekends and during lunch-time and rush-hour in work_days, the same for posts with documents. 
* The most favourable topics are: кейс, в закладки, вдохновляют (these are 3 the most popular topics in Russian language). 
* Also I have retrived the most likeable and shared posts and advised SMM to pay attention to them. 

# Парсинг паблика компании Skillbox в VK с целью анализа полученных данных и подготовки рекомендаций для SMM
### Что было сделано? 
<br> Я спарсила чуть более 1000 постов в паблике и извлекла такие данные о каждом посте:
* время публикации
* текст
* тип и количество вложений 
* тема текста
* количество комментариев, репостов, лайков и просмотров
### В ходе работы я использовала инструменты:
* VK-API 
* requests module
* pandas
* matplotlib
* regular expressions 
### Какие основные выводы я сделала? 
* Пользователи проявляют разную активность в течение будней и выходных, поэтому я анализировала эти периоды по отедельности. 
* В выходные пользователи проявляют больше активностей на один пост, чем в будни, и при этом они наиболее активны с 11.00 до 15.00. 
* В будн пользователи наиболее активны в обед (13.00) и в вечерний час пик (после 18.00).
* В будни лучше постить тексты длиной от 120 до 220 слов, а в выходные больше "заходят" тексты длиной до 150 слов. 
* Пользователям нравятся посты с фотографиями и ссылками. Посты с видео и документами нравятся больше в выходные и в течение обеда в будни. 
* Наиболее популярные темы постов: кейс, в закладки, вдохновлят. 
* Также я выявила наиболее популярные посты и посоветовала обратить на них внимание. 


