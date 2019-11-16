# NewRelic

## Code Specs
See included CC.md file.

## Requirements
* Python 3.6+

## Build and Run

### Virtualenv
The script will probably run without the virtual environment if you change the python path line, but the test require them.
```
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

### Run
```
$ echo "This is two. This is two. This is one." | word_group_counts
Top 100 results for stdin
---------------------------------
2 - this is two
2 - is two this
2 - two this is
1 - this is one
---------------------------------
```

### Help
```
$ ./word_group_counts
usage: word_group_counts [-h] [-g GROUP_SIZE] [-b BUFFER_SIZE] [-t TOP_COUNT]
                         [-j]
                         [FILE [FILE ...]]

Count word groups

positional arguments:
  FILE                  Input files (default: None)

optional arguments:
  -h, --help            show this help message and exit
  -g GROUP_SIZE, --group-size GROUP_SIZE
                        Group size (default: 3)
  -b BUFFER_SIZE, --buffer-size BUFFER_SIZE
                        Buffer size (default: 10240)
  -t TOP_COUNT, --top-count TOP_COUNT
                        Top counts (default: 100)
  -j, --json-only       Bare JSON results (default: False)
```

### Test
```
$ pytest -vvv
=================================================== test session starts ====================================================
platform darwin -- Python 3.6.8, pytest-5.2.4, py-1.8.0, pluggy-0.13.0 -- /Users/pwong/ownCloud/Code/newrelic/venv/bin/python3.6
cachedir: .pytest_cache
rootdir: /Users/pwong/ownCloud/Code/newrelic
plugins: console-scripts-0.2.0
collected 4 items

test_word_group_counts.py::test_stdin PASSED                                                                         [ 25%]
test_word_group_counts.py::test_stdin_not_enough_words PASSED                                                        [ 50%]
test_word_group_counts.py::test_from_file[inprocess] PASSED                                                          [ 75%]
test_word_group_counts.py::test_from_mulitple_files[inprocess] PASSED                                                [100%]

==================================================== 4 passed in 0.24s =====================================================
```

Suggested sample output.
```
$ ./word_group_counts pg2009.txt
Top 100 results for pg2009.txt
---------------------------------
320 - of the same
126 - the same species
125 - conditions of life
116 - in the same
107 - of natural selection
103 - from each other
98 - species of the
89 - on the other
81 - the other hand
78 - the case of
75 - the theory of
73 - some of the
72 - parts of the
72 - of the world
70 - through natural selection
69 - with respect to
67 - in the case
65 - it may be
65 - the species of
65 - the inhabitants of
64 - of the species
62 - that of the
61 - forms of life
61 - the same genus
60 - individuals of the
58 - as far as
56 - the number of
55 - those of the
55 - part of the
53 - the principle of
52 - the nature of
52 - to each other
51 - on the same
51 - in this case
50 - to the same
50 - nature of the
50 - more or less
50 - at the same
49 - as in the
49 - in regard to
47 - and in the
47 - it has been
47 - a state of
47 - the individuals of
47 - one of the
47 - nearly the same
47 - in which the
46 - inhabitants of the
46 - the amount of
46 - state of nature
46 - each other in
46 - we can understand
45 - are descended from
45 - from a common
44 - might have been
44 - will have been
43 - the conditions of
43 - by natural selection
42 - to have been
42 - animals and plants
42 - and of the
42 - in a state
42 - the same manner
42 - which have been
42 - and on the
42 - to believe that
41 - respect to the
41 - the same time
41 - would have been
41 - we have seen
40 - as well as
40 - there is no
40 - in some degree
40 - the united states
40 - varieties of the
40 - members of the
40 - on the theory
40 - it would be
39 - each other and
39 - of the most
39 - belonging to the
38 - that it is
38 - could be given
38 - it is that
37 - in order to
37 - theory of natural
36 - the present day
36 - the sterility of
36 - of life and
36 - it is not
36 - species belonging to
36 - the process of
35 - the power of
35 - reason to believe
34 - in relation to
33 - at the present
33 - and this is
33 - habits of life
33 - from the same
33 - believe that the
---------------------------------

```
