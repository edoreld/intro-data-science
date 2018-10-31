# Rapport Spark

## Exercise 1

### 6.

```python
wordCounts.sortBy(lambda x: x[1], ascending=False).take(50)
```

## Exercise 2

### 4. 

Take returns a list of strings, where each string corresponds to one line in the file.

First returns a string corresponding to the first line.

### 5. 

2420766 lines.

2420766 people that follow other people on Twitter.

### 6. 

In exercice part we determined that the results are returned as strings. It would be better if they were lists so that we can access each ID individually. We can achieve this using split()

### 7.
```python
twits = map(lambda line: line.split())
```

### 8.
```python
twits.flatMap(lambda x: [x[0], x[1]]).distinct()
# or
twits.flatMap(lambda x: (x[0], x[1])).distinct()
```

### 9.
```python
twitsMapped = twits.map(lambda lst : (lst[1], 1))

indegree = twitsMapped.reduceByKey(lambda a, b: a + b)
```

### 10.
```python
indegree.filter(lambda x: x[1] >= 1000).take(10)
```

It represents the user IDs of people being followed by 1000 or more users

## Exercise 3

### 1.
```py
distrange = sc.parallelize(range(0, 100))
```

### 2.

The problem that we can run across is that we need to use two RDDs on the same command, but that's just not possible.

### 3.

We export indegree as a broadcast variable

```py
bcInDegree = sc.broadcast(indegree.collect())

# We need to broadcast the indegree list

twitProbs = distrange.map(lambda n : (n, len([x for x in bcInDegree.value if x[1] > n]) / len(bcInDegree.value)))

```

### 4.

```py
twitProbs.map(lambda row: str(row[0]) + "," + str(row[1])).saveAsTextFile("outputfolder")
```

### 5. 

The part files correspond to each of the tasks writing their output to their own file.

How would it work if the output was just one file? In this case, all tasks would try to write to the same file in the HDFS, which means there would be a number of locks on the file to ensure integrity. This would diminish performance.

### 6.

It's a "greater than" cumulative frequency distribution. We can use it for things like dice rolls, coin flips and more (i.e: what's the probability that I will roll more than 5 on a 6-faced die roll)

![greater than cumulative frequency distribution](https://i.imgur.com/wMWrVqA.png)
