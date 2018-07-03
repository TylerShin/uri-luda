# Ruda Project
Collect and archive Ruda's photos.

## User scenario
- Crawl Ruda's photo's from seed url page.
- seed url page should be easily changed by an user.
- Archive the photos to local drive or S3.
- There is admin page that shows the photos and statistics about the crawling.

## Design specs
### Crawler
- Crawler should parse and execute Javascript to read SPA websites.
- There should be another crawler also parse only HTML because of the speed issue.
- Crawler should handle a blocking logic of the target webpage. So, it shouldn't be super fast and has too many parallel instances.

### Detector
- Detector should find and grab images on the webpage.
- Detector should know whether the photo's main character is Ruda or not.

## Archiver
- Archiver should know whether there was already same photo in local(s3) drive or not.
- To perform upper spec, Archiver should discriminate which photo is same photo. Not just by a file name.
- If same photo exists, Archiver will save a better one. (normally bigger size)
- If same photo doesn't exist, Archiver just save the photo.  

## Admin page
- WIP

## What we've done
- Make README.md
