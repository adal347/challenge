# Basketball Games Prediction - Challenge

For many years the humanity tried to predict different aspects of the world.
Predict weather, natural disasters, lottery and games is fundamental
for us. We predict future to understand it and react it. For this program we
want to predict, with some characteristics, if we can know the result of a
game that has not yet disputed.

# Table Of Contents

1. [Justification](#justification)
2. [How to Use](#how)
  1. [Install](#install)
  2. [Run](#run)
  3. [Create Test](#create)
3. [References](#references)

# Justification

The reason of why we want to predict basketball games is because is very helpful.
For Technical Director predict basketball games will be useful
to create an intense training or systematic training for the next game,
depending of the result of the prediction.

Also, for obvious reason, predict basketball games is a good help
to win some money in sports betting.

# How to use

To be able to make this predictions, I help in the branch of Artificial Intelligence
that it is Computational Intelligence. This branch is based in when you introduce a
huge data in the computer, it process this data to make the
predictions and obtain the results.

To use this branch, as I said before we need to know all the data that we can use
in the way to predict basketball games. In the references at the end you can see
a bunch of data to explore.

After we see all the data and we know what aspects will help to predict a basketball
game in a successful way. For this program I choose:

* The position in the season.
* The budget of the team in the season.
* Last ten games of the team (If won or lose).
* If the team play as local or not.
* The last five games played with the rival.
* The position of the last season.

To predict basketball games we need an algorithm that use the parameters to obtain
a good results in the evaluations. The function that is used to evaluate this is
a classic algorithm in Artificial Intelligence. The search system with adversary.

Finally the function is:

```shell
 function = summatory( probability(i) * value(i))
```

* Function: The percentage of the team to get the victory.
* i: The characteristics that is evaluated.
* probability of i: the weight of the factor i.
* value of i: the value of each characteristic (i).

The values in the program are:

* Actual Position = 0.25
* Budget = 0.2
* Last ten games = 0.2
* Is Local = 0.15
* Last five games versus the rival = 0.25
* Position of the last season = 0.25

To obtain the probability of each characteristic is more-less the same for each one

```shell

Probability = TeamA(i)/(TeamB(i) + TeamA(i))

```

After calculate all the characteristics we compare the percentage of the teams
and see who will win.

## Install

To get the repository, you need:

```shell
  # Clone the Repository
  git clone https://github.com/adal347/challenge.git
```

## Run

To run the application, you already have some test of the playoffs of the season 2017.
Also you need to have python 3 to run it the run file.

```shell
  # After you clone the repository, you move to the repository
  cd challenge

  # Run the run file, if you don't have permissions you need to do
  chmod 755 run

  # If you have the permissions
  ./run < test/prediction.in
```
After run the run file you can see the prediction of the data that is received.

## Test

The repository already have some test of the playoffs of the season 2017.
In first test, we see games of april 26 and 27 of this season. We see that 5 of 6
games has a success prediction this is a 83% of success.

After in the second test, we see games of may 1 and 2 of the season. We see
that 3 of 4 games are success predicted this is 75% of success.

For the last test, we see a test of one hundred games. We see that of games are
success predicted this is of success.

If you want to test the program you need to create a test like this ones.
You can see this test in Test directory.

# Conclusion

The conclusion is that there are some nice results but it still some values that
we have to count to make a good prediction, another interested values
will be the points, the average height of players
and number of international players, to get better results
and predict in a better way. but also you don’t forget that is
a sport everything can happend in a sport. NBA says "where amazing happens" so.
"This is why we play".

# References

* [NBA Stats](http://stats.nba.com/)
* [Positions](https://es.wikipedia.org/wiki/Playoffs_NBA_2017)
* [Budget](http://www.hispanosnba.com/salarios/equipos/)
