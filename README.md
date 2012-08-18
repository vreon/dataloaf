# Data Loaf

Data Loaf is a tool that spews out randomly-generated, structured data based on
a set of rules defined in a grammar file. It's what powers
<http://dataloaf.42nex.us>.

The package contains an executable module for CLI usage, a Flask app with a
HATEOAS API, and (someday) a fancy frontend for users to define and save their
own grammars.

The traversal algorithm is nothing fancy, just iterated string replacement. But
it's fun!

## Example of the fun

Let's start with a grammar file:

```
<start>
    1 Data Loaf is <an-adjective> piece of <noun>!

<an-adjective>
    4 an excellent
    4 an enormous
    1 a gigantic
    
<noun>
    2 software
    2 crap
    1 turkey
```

Note that there's nothing special about those angle brackets. You could go on
to define rules for the string `turkey` if you wanted. (Even the letter `e` if
you're feeling adventurous.)

That integer next to each rule is its weight. Like drawing marbles from a bag,
Data Loaf sums up the probabilities for a ruleset and picks one.

Let's run three traversals of that file:

```bash
$ python -m dataloaf --num 3 < example.gmr
Data Loaf is an excellent piece of software!
Data Loaf is an enormous piece of crap!
Data Loaf is an enormous piece of turkey!
```

Useful, no? Now it's your turn -- check out the examples and let your
imagination take you from there! **♪ Data Looooooaf! ♫**

## License

Data Loaf is made available under the terms of the Expat/MIT license (see
LICENSE.)
