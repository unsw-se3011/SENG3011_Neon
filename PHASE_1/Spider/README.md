# Scrap

## venv

Setting up the virutal environment

```bash
sudo apt install python3-dev
virtualenv venv `where python3`
source venv/bin/activate
pip install -r requirments.txt

```

## ProMed

Promed doesn't use standard way as html, we need find another way out. Also scraper doesn't design fairly well.

Some feed we don't need to follow, because the language is not english.

We only need to care these feed:  
[South Asia](http://www.promedmail.org/ajax/getPosts.php?edate=2019-01-24&return_map=0&feed_id=170&seltype=latest)
[Anglophone Africa](http://www.promedmail.org/ajax/getPosts.php?edate=2019-02-24&return_map=0&feed_id=24&seltype=latest)
[Mekong Basin](http://www.promedmail.org/ajax/getPosts.php?edate=2019-01-24&return_map=0&feed_id=15&seltype=latest)
[Promed mail](http://www.promedmail.org/ajax/getPosts.php?edate=2019-02-24&return_map=0&feed_id=1&seltype=latest)

So it's feed 1,15,17,24
