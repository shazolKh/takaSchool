## Simple Bidding site
---

### Used Packages
  - Pillow : This packege is need for working with images. And when creating the `Product`, image needed to be uploaded and compressed. So, I used pillow to compressed and optimised the image, so that uploading don't take a large amount of time.
  - Whitenoise: After deploing the app on the server, there arises some issue regarding `Static Files`. To solved those issues, `Whitenoise` is needed. I just installed it and add it's `middleware` at the `MIDDLEWARE` section of `settings.py` file.
  - mysqlclient: I used mysql at local server. So, Installed it.
  - django-heroku: Didn't need to use this. It also take care of staticfiles on the heroku server.
  
### Challenges
#### Step 1:
  - Problem: First problem I faced was to `Register` and `Login` at the same time. I wrote the logic accordingly and I thought the logic was okay but it turned out that I couldn't login with already register already registered user because it trying to reister with already registerd cridentials and caused error.
  - Solution: Then I figured out that if I make the default value of `is_active` field `true`, then this whole module works just fine.
#### Step 2:
  - Didn't face any challenges.
  
#### Step 3:
  - Problem: At this step, I needed to compare datetime, and I spent hours to do that but I couldn't figured out why it dont't working.
  - Solution: After some study I realized that, maybe the datetime formats are different of `datetime.now()` and `datetime stored in database`. So, I converted them into same format and compared them.
  
#### Step 4:
  - Didn't face ony perticular challenges.
  
#### Step 5:
  - Couldn't implement the `Chart` to visualise the data.
#### Step 7: 
  - Deployed the Django applications on `Heroku` before. Also, smoothly done this time. 
