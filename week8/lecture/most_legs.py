import wiki_shows3

creepy_crawlies = {
"snake":0,
"centipede":254,
"dog":4,
"ant":6,
"dufflepud":1,
"millipede":400,
"human":2,
"spider":8,
"bird":2
}

if __name__ == "__main__":
    min_legs = wiki_shows3.findExtremeValue(creepy_crawlies, max=False)
    print("%s has the fewest (%d) legs in the dataset" % (min_legs[0], min_legs[1]))

    max_legs = wiki_shows3.findExtremeValue(creepy_crawlies)
    print("%s has the most (%d) legs in the dataset" % (max_legs[0], max_legs[1]))