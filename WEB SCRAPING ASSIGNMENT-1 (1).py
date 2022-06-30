#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ques2.
from bs4 import BeautifulSoup
import requests


# In[2]:


url = 'https://www.imdb.com/list/ls091520106/'
response = requests.get(url)
response


# In[4]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[5]:


movies = soup.find(class_="lister-item-header")
movies


# In[6]:


movies.text.replace('\n','')


# In[10]:


movies = []
for i in soup.find_all(class_="lister-item-header"):
    movies.append(i.text)

movies


# In[11]:


ratings = soup.find(class_="ipl-rating-star small")
ratings


# In[15]:


ratings = []
for i in soup.find_all(class_="ipl-rating-star small"):
    ratings.append(i.text)
ratings


# In[16]:


year = soup.find(class_="lister-item-year text-muted unbold")
year


# In[17]:


year = []
for i in soup.find_all(class_="lister-item-year text-muted unbold"):
    year.append(i.text)
year


# In[18]:


print(len(movies),len(ratings),len(year))


# In[19]:


import pandas as pd
df=pd.DataFrame({'Movies': movies,'Ratings':ratings,'Year':year})
df


# In[20]:


#ques3.
url = 'https://www.imdb.com/list/ls009997493/'
response = requests.get(url)
response


# In[21]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[22]:


movies = soup.find(class_="lister-item-header")
movies


# In[23]:


movies = []
for i in soup.find_all(class_="lister-item-header"):
    movies.append(i.text)
movies


# In[24]:


ratings = []
for i in soup.find_all(class_="ipl-rating-widget"):
    ratings.append(i.text)
ratings


# In[25]:


year = soup.find(class_="lister-item-year text-muted unbold")
year


# In[26]:


year = []
for i in soup.find_all(class_="lister-item-year text-muted unbold"):
    year.append(i.text)
year


# In[27]:


print(len(movies),len(ratings),len(year))


# In[28]:


import pandas as pd
df=pd.DataFrame({'Movies': movies,'Ratings':ratings,'Year':year})
df


# In[29]:


#ques4.
page = requests.get('https://presidentofindia.nic.in/former-presidents.htm')
page


# In[30]:


soup=BeautifulSoup(page.content)
soup


# In[31]:


first_title = soup.find('div',class_="presidentListing")
first_title


# In[35]:


Presidents = []
for i in soup.find_all("div",class_="presidentListing"):
    Presidents.append(i.text)
Presidents


# In[37]:


print(len(Presidents))


# In[38]:


import pandas as pd
df=pd.DataFrame({'former presidents of India':Presidents})
df


# In[39]:


#ques7.
url = 'https://www.cnbc.com/world/?region=world'
response = requests.get(url)
response


# In[40]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[41]:


headline = soup.find(class_="LatestNews-headline")
headline


# In[42]:


headline = []
for i in soup.find_all(class_="LatestNews-headline"):
    headline.append(i.text)

headline


# In[43]:


time = []
for i in soup.find_all(class_="LatestNews-wrapper"):
    time.append(i.text)

time


# In[44]:


link = []
for i in soup.find_all(class_="LatestNews-headline"):
    link.append(i['href'])
link


# In[45]:


print(len(headline),len(time),len(link))


# In[46]:


import pandas as pd
df=pd.DataFrame({'Headline': headline,'Time':time,'News Link':link})
df


# In[47]:


#ques8.
url = 'https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles'
response = requests.get(url)
response


# In[48]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[49]:


titles = []
for i in soup.find_all(class_="sc-5smygv-0 nrDZj"):
    titles.append(i.text)

titles


# In[50]:


Authors = []
for i in soup.find_all(class_="sc-1w3fpd7-0 pgLAT"):
    Authors.append(i.text)
Authors


# In[51]:


Date = []
for i in soup.find_all(class_="sc-1thf9ly-2 bKddwo"):
    Date.append(i.text)
Date


# In[52]:


url = []
for i in soup.find_all(class_="sc-5smygv-0 nrDZj"):
    url.append(i['href'])
url


# In[53]:


print(len(titles),len(Authors),len(Date),len(url))


# In[54]:


import pandas as pd
df=pd.DataFrame({'Titles': titles,'Authors':Authors,'Date':Date,'URL':url})
df


# In[55]:


#ques9.
page = requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')
page


# In[56]:


soup=BeautifulSoup(page.content)
soup


# In[58]:


name = []
for i in soup.find_all(class_="restnt-name ellipsis"):
    name.append(i.text)
name


# In[59]:


Cuisine = []
for i in soup.find_all('div',class_="detail-info"):
    Cuisine.append(i.text)
Cuisine


# In[60]:


location = []
for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    location.append(i.text)
location


# In[61]:


rating = []
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[62]:


url = []
for i in soup.find_all('img',class_="no-img"):
    url.append(i['data-src'])
url


# In[63]:


print(len(name),len(Cuisine),len(location),len(rating),len(url))


# In[64]:


import pandas as pd
df=pd.DataFrame({'Restaurant name': name,'Cuisine':Cuisine,'Location':location,'Ratings':rating,'Image URL':url})
df


# In[65]:


#ques.10
url = 'https://scholar.google.com/citations?view_op=top_venues&hl=en'
response = requests.get(url)
response


# In[66]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[75]:


rank = []
for i in soup.find_all(class_="gsc_mvt_p"):
    rank.append(i.text)

rankimport pandas as pd

df=pd.DataFrame({'Rank': rank,'Publication':publication,'h5-index':index})


# In[68]:


publication = []
for i in soup.find_all(class_="gsc_mvt_t"):
    publication.append(i.text)

publication


# In[69]:


index = []
for i in soup.find_all('a',class_="gs_ibl gsc_mp_anchor"):
    index.append(i.text)

index


# In[70]:


median = []
for i in soup.find_all('span',class_="gs_ibl gsc_mp_anchor"):
    median.append(i.text)

median


# In[71]:



print(len(rank),len(publication),len(index),len(median))


# In[77]:


import pandas as pd

df=pd.DataFrame({'Rank': rank,'Publication':publication,'h5-index':index})
df


# In[78]:


#ques1.
url = 'https://en.wikipedia.org/wiki/Main_Page'
response = requests.get(url)
response


# In[79]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[80]:


header = []
for i in soup.find_all(class_='mw-headline'):
    header.append(i.text)
header


# In[81]:


print(len(header))


# In[82]:


import pandas as pd

df=pd.DataFrame({'header': header})
df


# In[83]:


#ques5.
url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
response = requests.get(url)
response


# In[84]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[85]:


matches = soup.find(class_="rankings-block__banner--matches")
matches


# In[ ]:


matches = []
for i in soup.find_all("td",class_="rankings-block__banner--matches"):
    matches.append(i.text)

matches

