linkedIn Compare
================

An easy way to compare LinkedIn profiles.

In this app you can add LinkedIn public links to get a public url with these links.
You can share link and your friends can compare profiles easily. See video below:

[![LinkedIn Compare Usage](https://i.ytimg.com/vi/6dhMeNVTQn0/0.jpg)](https://www.youtube.com/watch?v=6dhMeNVTQn0)

Installation
------------

For local installation just:

```
make install
```

Than:


```
make run
```

will open a webserver in port 8000.

To test access: http://localhost:8000/linkedin_compare


Limitations
-----------

LinkedIn block some ips. Amazon or Heroku ips will get error 999
causing ticket error in application. Localhost works great.