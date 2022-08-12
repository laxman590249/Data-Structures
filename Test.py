from datetime import datetime
print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

d = [1, 2]
d2 = [3, 4]
d3 = d.extend(d2)
print(d2)
print(d3)
print(d)