U
    ��^X  �                   @   s�   d dl Z d dlZd dlZd dlZd dlZd dlmZ e�d� e �	dd�Z
de
� �ZdZdZd	Zd
ZdZdddddddddddgZde �e�fgZdd� Zdd� Ze�  dS )�    N)�BeautifulSoup�clear�   �   z.https://www.insecam.org/en/bycountry/IT/?page=z
[1;37;40mz
[1;31;40mz
[1;30;40mz
[1;34;40mz
[1;32;40mzHMozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0zIMozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0zMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586zrMozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36zDMozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like GeckozwMozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/602.3.12 (KHTML, like Gecko) Version/10.0.2 Safari/602.3.12zLMozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0z�Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML, like Gecko) Version/10.0 Mobile/14D27 Safari/602.1z�Mozilla/5.0 (Linux; Android 6.0.1; Nexus 6P Build/MTC19X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36z�Mozilla/5.0 (Linux; Android 4.4.4; Nexus 5 Build/KTU84P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87Mobile Safari/537.36zHMozilla/5.0 (compatible; Googlebot/2.1; (http://www.google.com/bot.html)z
User-Agentc                  C   sh   t � dt� dt � dt� dt � dt� dt � dt� dt � d�} | D ]$}tj�|� tj��  t�d	� q>d S )
Nu�  
   ▄▄ • ▄▄▄ .▄▄▄▄▄   ▄▄·  ▄▄▄· • ▌ ▄ ·. 
  ▐█ ▀ ▪▀▄.▀·•██    ▐█ ▌▪▐█ ▀█ ·██ ▐███▪
  ▄█ ▀█▄▐▀▀▪▄ ▐█.  ▪██ ▄▄▄█▀▀█ ▐█ ▌▐▌▐█·
  ▐█▄▪▐█▐█▄▄▌ ▐█▌  ·▐███▌▐█ ▪▐▌██ ██▌▐█▌
  ·▀▀▀▀  ▀▀▀  ▀▀▀   ·▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀
<�/z	> code byz:
	=> Hickin
	   TeleGram �:z Hickin
  	   YouTube  z Hickin Hack z..
__________________________________________

�{�G�z�?)�g�w�sys�stdout�write�flush�time�sleep)Zbann�i� r   �	GetCam.py�banner2   s    �
�
�
�
r   c                  C   s  t �  z�t�� } | j�t� | �t�}t|jd�}d}|�	dddi�D ]n}|�d�}|�
d�}tt� dt� |� t� d	t� d
t� |d � d|d � dt� dt� �� t�d� |d }qFtd� W nV   t� dt� dt� dt� d�}|d D ]$}tj�|� tj��  t�d� q�Y nX d S )Nzhtml.parserr   Zimg�classz"thumbnail-item__img img-responsive�srcr   �[z] - z[ r   z//�   z/ �]g      �?� �!z&] Check your connection and try again �.z

r   )r   �requestsZSession�headers�update�get�url�BSZcontentZfindAll�split�printr
   r	   r   r   �rer   r   r   r   )�s�rZsoup�xr   �lZprir   r   r   �startF   s(    


D


r*   )Zrandomr   r   �osr   Zbs4r   r"   �systemZrandintZnumr!   r
   r%   �p�br	   Z
useragentsZchoicer   r   r*   r   r   r   r   �<module>   s2   (

�!