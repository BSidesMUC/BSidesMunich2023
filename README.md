
# BSides Munich conference page.

This site is based on jekyll and hosted on github pages.

## Getting started

- Create a repository
- The relevant files from the latest edition
- Adjust the `CNAME` and other relevant information
- 

## Build with Docker

```
export JEKYLL_VERSION=3.8; sudo docker run --rm -p 4000:4000 --volume="$PWD:/srv/jekyll" -it jekyll/jekyll:$JEKYLL_VERSION jekyll serve --watch
```

```
export JEKYLL_VERSION=3.8
docker run --rm \
  --volume="$PWD:/srv/jekyll:Z" \
  -it jekyll/jekyll:$JEKYLL_VERSION \
  jekyll build
```

```
export JEKYLL_VERSION=3.8
docker run --rm \
    --volume="$PWD:/srv/jekyll" \
    --volume="$PWD/vendor/bundle:/usr/local/bundle" \
    --env JEKYLL_ENV=development \
    -p 4000:4000 \
    -it jekyll/jekyll:${JEKYLL_VERSION} \
    jekyll serve --watch --incremental --trace
```

## References
 
 - https://github.com/envygeeks/jekyll-docker
 - https://github.com/envygeeks/jekyll-docker/blob/master/README.md

