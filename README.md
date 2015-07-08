Packages to crawl video info from youtube.
Chen Wang, chenw@cmu.edu

<1> Breadth First Search of video IDs
Package: crawlVideoIDs.py
Usage: python crawlVideoIDs.py --seed="11 digit youtube id as the searching seed" --depth="The depth of breadth first search"
Output: "seed_id.ids"
Note: Need remove duplicates before using. 

<2> Get view counts of videos
Package: crawlViewCnts.py
Description: crawl view counts for all video ids in an video id list file
Usage: python crawlViewCnts.py --id_file="vid_id_list"
Output: "vid_id_list_viewCnts.csv"
Note: The output csv file may contain empty string on view counts. Normally view count is in the second column.
