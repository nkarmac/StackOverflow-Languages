getwd()
filename <- "objective-c.csv"
lang = read.csv(filename)
x = lang["count"]
y = lang["positive"]
z = lang["normalized.viewcount"]
f = lang["total.viewcount"]
p = lang["negative"]

lang2 = read.csv("ruby.csv")
x2 = lang2["count"]
y2 = lang2["positive"]
z2 = lang2["normalized.viewcount"]
f2 = lang2["total.viewcount"]
p2 = lang2["negative"]