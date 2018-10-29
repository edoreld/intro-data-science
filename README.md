# Rapport Data Science

## Intro

The source files are named after the exercises they refer to. So for example, mapper4.py is for exercise 4.

### Exercice 1

Done.

### Exercice 2 Map/Reduce (sans Hadoop)


#### mapper0.py

Takes text from standard input.

It outputs a list containing all the words of the text, ungrouped, along with a 1 next to them.

#### reducer0.py

It takes its input from the result of mapper0.py

It outputs a list of words with the count for each word

The '|' character is a classical Unix command used to pass the output of the command to the left of the pipe to the input of the command to the right.

The sort commands by default sorts by alphabetical order

The commands take 0.1000 seconds on my system!

### Exercice 3. Exécution de WordCount en Map/Reduce avec Hadoop

J'utilise la version 3.1.1 de Hadoop, donc j'ai du changer cela dans la commande.

```python
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.1.jar -input data/lesmiserables.txt -output output/ -file src/mapper0.py -file src/reducer0.py -mapper mapper0.py -reducer reducer0.py
```

2.

MapInputRecords: number of input lines
MapOutputRecords: number of output lines

Reduce input records: number of input lines (of the reducer)
Reduce output records: number of output lines

3. After aggregating locally, the number of exit records is reduced by more than 5 times! That's a big advantage as it will result in reduced network traffic.

4. The solution is not entirely satisfactory. The performance of Map is going to be reduce because we are going to do the grouping for each call to Map.

5. We want a combiner. The combiner is going to do the grouping that we were doing with the mapper, but it's going to do it with the combination of the outputs of all calls to Map, so it's more efficient.

### Exercice 4. Temps de consultation moyen avec Map/Reduce

Done.

Because the average does not have the associative property.

On the combiner we will send the number of terms and the partial moyennes

Combiner sends -> (<url>, (<sum>, nbre. elements)), then the Reducer will calculate the moyennes by adding up the sums and dividing by total number of elements.

### Exercice 5. Requêtes SQL en MapReduce


1.

i. We need to use a mapper to filter by the condition, but we don't need to use a reducer.

ii. Map Input/Output
File, Chunk -> id, value

2. Done (52.py)
3.

a. Yes, we need a mapper and a reducer. When we are iterating in the reducer, we discard all the values with the same key except for the first.

b. Map I/O
File, Chunk -> id, value

Reducer I/O
id, value -> id, value

4. We can use a combiner that will take the mapper output and remove duplicates. This will reduce network traffic as less data will be sent to the reducer.

5.

One option to compare performance is to use the time command.

Another option is to look at the output from the hadoop command. For example, we can take a look at the number of input records for the reducer. We can also see how many bytes were written.

6.

 -> R2:
mapper62.py
reducer62.py

The more efficient version will group the results in a combiner

mapper62x.py
reducer62x.py
combiner62x.py

 -> R3:
 mapper63.py
 reducer63.py

 To improve the program, we would add the sorting logic to a combiner

 -> R4:
  mapper64.py
  reducer64.py

 -> R5:
  mapper65.py
  reducer65.py














