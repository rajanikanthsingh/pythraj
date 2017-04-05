
import json

l = [1, 2, 3, 4]

x = (sum(l) / float(len(l)))
y = max(l)
z = min(l)
RecordCount = len(l)






all = {'AverageValue':x,'MaxValue':y,'MinValue':z,'RecordCount':RecordCount}

print json.dumps(all, indent=4)
