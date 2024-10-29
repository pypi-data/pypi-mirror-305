# pyfivbvis

<!-- badges: start -->

[![Lifecycle:
experimental](https://img.shields.io/badge/lifecycle-experimental-orange.svg)](https://www.tidyverse.org/lifecycle/#experimental)
![openvolley](https://img.shields.io/badge/openvolley-darkblue.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMTAiIGhlaWdodD0iMjEwIj48cGF0aCBkPSJNOTcuODMzIDE4Ny45OTdjLTQuNTUtLjM5Ni0xMi44MTItMS44ODYtMTMuNTgxLTIuNDQ5LS4yNDItLjE3Ny0xLjY5Mi0uNzUzLTMuMjIyLTEuMjgxLTI4LjY5Ni05Ljg5NS0zNS4xNy00NS45ODctMTMuODY4LTc3LjMyMyAyLjY3Mi0zLjkzIDIuNTc5LTQuMTktMS4zOTQtMy45MDYtMTIuNjQxLjktMjcuMiA2Ljk1Mi0zMy4wNjYgMTMuNzQ1LTUuOTg0IDYuOTI3LTcuMzI3IDE0LjUwNy00LjA1MiAyMi44NjIuNzE2IDEuODI2LS45MTgtLjE3LTEuODktMi4zMS03LjM1Mi0xNi4xNzQtOS4xODEtMzguNTYtNC4zMzctNTMuMDc0LjY5MS0yLjA3IDEuNDE1LTMuODY2IDEuNjEtMy45ODkuMTk0LS4xMjMuNzgyLTEuMDUzIDEuMzA3LTIuMDY2IDMuOTQ1LTcuNjE3IDkuNDU4LTEyLjg2MiAxNy44MzktMTYuOTcgMTIuMTcyLTUuOTY4IDI1LjU3NS01LjgyNCA0MS40My40NDUgNi4zMSAyLjQ5NSA4LjgwMiAzLjgwMSAxNi4wNDcgOC40MTMgNC4zNCAyLjc2MiA0LjIxMiAyLjg3NCAzLjU5NC0zLjE3My0yLjgyNi0yNy42ODEtMTYuOTA3LTQyLjE4NS0zNi4wNjgtMzcuMTUxLTQuMjU0IDEuMTE3IDUuMjQtMy4zMzggMTEuNjYtNS40NzMgMTMuMTgtNC4zOCAzOC45MzctNS43NzIgNDYuMDc0LTEuNDg4IDEuMjQ3LjU0NyAyLjIyOCAxLjA5NSAzLjI3NSAxLjYzIDQuMjkgMi4xMDcgMTEuNzMzIDcuNjk4IDE0LjI2NSAxMS40MjcuNDA3LjYgMS4yNyAxLjg2NiAxLjkxNyAyLjgxNCAxMS4zMDggMTYuNTY1IDguNjIzIDQxLjkxLTYuODM4IDY0LjU1Mi0zLjI0OSA0Ljc1OC0zLjI1OCA0Ljc0MiAyLjQ1IDQuMDE4IDMyLjQ4Mi00LjEyMiA0OC41MTUtMjEuOTM1IDM5LjU3OC00My45NzQtMS4xNC0yLjgwOSAxLjU2NiAxLjA2IDMuNTE4IDUuMDMyIDI5LjY5MyA2MC40MTctMjIuNTggMTA3Ljg1My03OS40OTggNzIuMTQzLTUuMDg0LTMuMTktNS4xMjMtMy4xNTItMy45MDIgMy44ODMgNC43MjEgMjcuMjIgMjUuNzgzIDQzLjU2MiA0NC4wODkgMzQuMjEgMS4zNjItLjY5NiAyLjIxLS43NSAyLjIxLS4xNDMtNi43NiAzLjg1Ny0xNi4wMTggNi41NTMtMjMuMTI2IDguMDkxLTcuNTU1IDEuNTQ3LTE4LjM2NiAyLjE3Mi0yNi4wMiAxLjUwNnoiIGZpbGw9IiNmZmYiLz48ZWxsaXBzZSBjeD0iMTA1Ljk3NSIgY3k9IjEwNC40NDEiIHJ4PSI5NC44NCIgcnk9IjkyLjU0MiIgZmlsbD0ibm9uZSIgc3Ryb2tlPSIjZmZmIiBzdHJva2Utd2lkdGg9IjEwLjc0Ii8+PC9zdmc+)

<!-- badges: end -->

pyfivbvis provides an python client to the FIVB VIS web service system.

Full details - https://openvolley.github.io/pyfivbvis/
## Installation

You can install or update pyfivbvis with:

```
pip install pyfivbvis
pip install pyfivbvis -U
```



## Examples

Fetch list of tournaments:

```python
from pyfivbvis.vis_fetcher import FivbVis as vis
all_tournaments = vis.fetch_beach_tournament_list()
print(all_tournaments[0:2])

[
    {
        "No": "1",
        "Title": "",
        "Type": "9",
        "NoEvent": "",
        "Code": "BEST2010",
        "Gender": "0",
        "Name": "Best Photos of 2010",
        "CountryCode": "99",
        "StartDateQualification": "",
        "StartDateMainDraw": "",
        "EndDateQualification": "",
        "EndDateMainDraw": "",
        "NbTeamsQualification": "64",
        "NbTeamsMainDraw": "32",
        "NbTeamsFromQualification": "8",
    },
    {
        "No": "2",
        "Title": "Beach Tournament Test 00",
        "Type": "35",
        "NoEvent": "343",
        "Code": "BVISTEST",
        "Gender": "1",
        "Name": "Officials training Test event 00",
        "CountryCode": "CH",
        "StartDateQualification": "2024-09-04",
        "StartDateMainDraw": "2024-09-05",
        "EndDateQualification": "2024-09-04",
        "EndDateMainDraw": "2024-09-08",
        "NbTeamsQualification": "16",
        "NbTeamsMainDraw": "16",
        "NbTeamsFromQualification": "4",
    }
]
```

Fetch list of matches from a tournament:

```python
from pyfivbvis.vis_fetcher import FivbVis as vis
tourn_matches = vis.fetch_beach_match_list('503')
# To include refs and round metadata
tourn_matches = vis.fetch_beach_match_list('503', ref_info=True, round_info=True)
print(tourn_matches[0:2])

[
    {
        "NoTournament": "503",
        "NoPlayerA1": "103903",
        "NoPlayerA2": "103904",
        "NoPlayerB1": "117998",
        "NoPlayerB2": "120825",
        "NoTeamA": "771830",
        "NoTeamB": "771808",
        "TeamAName": "Larissa/Juliana",
        "TeamBName": "Ryabova/Ushkova",
        "TeamAFederationCode": "BRA",
        "TeamBFederationCode": "RUS",
        "NoInTournament": "1",
        "LocalDate": "2011-04-19",
        "LocalTime": "10:00:00",
        "Court": "1",
        "MatchPointsA": "2",
        "MatchPointsB": "0",
        "PointsTeamASet1": "21",
        "PointsTeamBSet1": "14",
        "PointsTeamASet2": "21",
        "PointsTeamBSet2": "15",
        "PointsTeamASet3": "",
        "PointsTeamBSet3": "",
        "DurationSet1": "840",
        "DurationSet2": "1020",
        "DurationSet3": "",
        "WinnerRank": "0",
        "LoserRank": "0",
    },
    {
        "NoTournament": "503",
        "NoPlayerA1": "103671",
        "NoPlayerA2": "103670",
        "NoPlayerB1": "122400",
        "NoPlayerB2": "118204",
        "NoTeamA": "771853",
        "NoTeamB": "771844",
        "TeamAName": "Nyström Em./Nyström Er.",
        "TeamBName": "Cicolari/Menegatti",
        "TeamAFederationCode": "FIN",
        "TeamBFederationCode": "ITA",
        "NoInTournament": "2",
        "LocalDate": "2011-04-19",
        "LocalTime": "10:00:00",
        "Court": "3",
        "MatchPointsA": "1",
        "MatchPointsB": "2",
        "PointsTeamASet1": "18",
        "PointsTeamBSet1": "21",
        "PointsTeamASet2": "21",
        "PointsTeamBSet2": "15",
        "PointsTeamASet3": "11",
        "PointsTeamBSet3": "15",
        "DurationSet1": "1200",
        "DurationSet2": "1020",
        "DurationSet3": "780",
        "WinnerRank": "0",
        "LoserRank": "0",
    },
]

```

Fetch list of rankings from a tournament:

```python
from pyfivbvis.vis_fetcher import FivbVis as vis
tourn_ranks = vis.fetch_beach_tournament_ranking('503')
print(tourn_ranks[0:2])

[
    {
        "EarnedPointsPlayer": "300",
        "EarningsPlayer": "850000",
        "EarnedPointsTeam": "600",
        "EarningsTotalTeam": "3000000",
        "Position": "1",
        "Rank": "1",
        "TeamFederationCode": "BRA",
        "TeamName": "Larissa/Juliana",
        "NoTeam": "375507",
        "NoTournament": "502",
    },
    {
        "EarnedPointsPlayer": "270",
        "EarningsPlayer": "600000",
        "EarnedPointsTeam": "540",
        "EarningsTotalTeam": "2100000",
        "Position": "2",
        "Rank": "2",
        "TeamFederationCode": "GER",
        "TeamName": "Goller/Ludwig",
        "NoTeam": "375500",
        "NoTournament": "502",
    },
]


```

