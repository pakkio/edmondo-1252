# edmondo-1252
testing fork

A very simple score keeper to help in building up small educational games in SecondLife, OpenSim or other virtual worlds,
or for any games.

It works using one only access URL and then specify 

* type
* session
* name
* score

For instance
<URL>/?type=add&session=c8ba58f0-7b66-44c8-a0d8-7231afcf47e9&name=player&score=-1

This adds an entry for player with -1 score or if already existent, set it with a score of -1

type can be

* type=list&session=<session>
To have a sorted list of all the scores sorted desc by score
* type=show&session=<session>
To have a kind of formatted table of the same data as in list
* type=clear&session=<session>
To clear all data for the session

For privacy reasons, no list of current sessions is provided so that the script can be used safely by many educators providing they are using different session ids.
