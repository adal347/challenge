# challenge

# Table Of Contents

1. [Introduction](#introduction)
2. [Justification](#justification)
3. [How to Use](#how)
  1. [Install](#install)
  2. [Run](#run)
  3. [Create Test](#create)
2. [References](#references)

# Introduction

For many years the humanity tried to predict different aspects of the world.
Predict weather, natural disasters, lotery and games. For this program we
want to predict, with some characteristics, if we can know the result of a
game that has not yet disputed.

# Justification

The reason of why we want to predict basketball games is because is very helpful.
For T.D. predict basketball games will be helpful to create a intese training or
sistematic training for the next game.

Also, for obvious reason, predict basketball games is a good help
to win some money.

# How to use

To be able to make this predictions, I help in the branch of Artificial Intelligence
that it is Computational Intelligence. This branch is based in when you introduce a huge data
in the computer, it process this data to make the predictions and obtain the results.

To use this branch, as I said before we need to know all the data that we can use
in the way to predict basketball games. In the references at the end you can see
a bunch of data to explore.

After we see all the data and we know whar aspects will help to predict a basketball
game in a successful way. For this program I choose:

* The position in the season (In this case is in season 2017)-
* The budget of the season.
* Last Ten games of the team (If won or lose).
* If the team play as Local or not.
* The last five games played with the rival.
* The position of the last season.

To predict basketball games we need a algorithm that use the parameters to obtain
a good results in the evaluations. The function that is used to evaluate this is
an clasic algorithm in Artificial Intelligence. The search system with adversary.

Finally the function is:

```shell
 funtion = sumatory( probabilty(i) * value(i))
```

* Function: The porcentage of the team to get the vicrory.
* i: The characteristics that is evaluated.
* probabilty of i: the weight of the factor i.
* value of i: the value of each characteristic (i).

The values in the program are:

* Actual Position = 0.25
* Budget = 0.2
* Last ten games = 0.2
* Is Local = 0.15
* Last five games versus the rival = 0.25
* Position of the last season = 0.25

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

  # Run the run file, if you don't have permises you need to do
  chmod 755 run

  # If you have the permises
  ./run < test/prediction.in
```
After run the run file you can see the prediction of the data that is recieved.

## Test

The repository already have some test of the playoffs of the season 2017.
In first test, we see games of april 26 and 27 of this season. We see that 5 of 6
games has a success prediction this is a 83% of success.

After in the second test, we see games of may 1 and 2 of the season. We see
that 1 of 2 games are success predicted this is 50% of success.

If you want to test the program you need to create a test like this ones.
You can see this test in Test directory.

# References

* [NBA Stats](http://stats.nba.com/)
* [Positions](https://es.wikipedia.org/wiki/Playoffs_NBA_2017)
* [Budget](http://www.hispanosnba.com/salarios/equipos/)
