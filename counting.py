import collections

urls = ["http://www.google.com/a.txt","http://www.google.com.tw/a.txt","http://www.google.com/download/c.jpg","http://www.google.co.jp/a.txt","http://www.google.com/b.txt","https://facebook.com/movie/b.txt","http://yahoo.com/123/000/c.jpg","http://gliacloud.com/haha.png",]

arr = []
for item in urls:
    arr.append(item.split('/')[-1])

most_common_result = collections.Counter(arr).most_common(3)

for item in most_common_result:
    print item[0], item[1]
