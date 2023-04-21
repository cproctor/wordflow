# WordFlow

WordFlow provides several simplified command-line utilities meant to be 
composed with UNIX pipes. This package is part of 
[Making With Code](https://makingwithcode.org), a 
Constructionist introductory CS curriculum. Most of these utilities duplicate
existing functionality of built-in shell commands, but our goal is to provide the 
cleanest, simplest possible interface to maximize expressivity while minimizing cognitive
load for beginners.

These utilities read lines of space-separated tokens from stdin and write to 
stdout. Several commands have an optional `position` argument (default=0) specifying
which token to use on each line. 

## Usage examples

First, get ahold of a file containing a list of words. A word list is [built in to Unix and Linux](https://en.wikipedia.org/wiki/Words_(Unix). Or [here's a list you can download](https://github.com/dwyl/english-words/blob/master/words_alpha.txt).

### Get the 1000 most common words

```
$ cat words.txt | frequency | order | pluck 1 | head -n 1000
```

### How many words contain two vowels in a row

```
$ cat words.txt | match "aa|ee|ii|oo|uu" | count
```

### What's the shortest word containing all five vowels? 

```
$ cat words.txt | match "a" | match "e" | match "i" | match "o" | match "u" | length | order | head
```

## What are the most common ten-letter words? 

```
$ cat words.txt | length | max 10 | min 10 | frequency 1 | order -r | pluck 2 | head
```

### Filter

- **match [pattern] [position=0]**: Allows lines where the specified word matches
  regular expression `pattern`. Regular expressions often need to be in quotation marks.
- **max [value] [position=0]**: Allows lines where the specified number is no 
  greater than `value`.
- **min [value] [position=0]**: Allows lines where the specified number is no 
  less than `value`.

### Map 

- **length [position=0]** Prepends the length of the specified word to the line.
- **frequency [position=0]** Prepends the frequency of the specified word 
  (approximate number of occurrences per billion words) to the line. 
- **pluck [position=0]** Replaces each line with the specified token.

### Sort

- **order [position=0] [-r --reverse]** Sorts lines according to the specified token. 
  When the specified token is a number, sorts numerically, otherwise lexically. 

### Reduce

- **count** counts the number of lines sent to stdin.
