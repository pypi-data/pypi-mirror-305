import requests
from bs4 import BeautifulSoup

class FivbVis:

    def fetch_beach_tournament_list():
        """
        Fetch FIVB beach tournament list from VIS.

        Returns
        -------
        list of dicts:
            A list of ALL beach tournaments with fields such as No, Title, Type, etc.
            
        Notes
        ------
        Documentation:
            https://www.fivb.org/VisSDK/VisWebService/BeachTournament.html
        """
        # Create the XML request string
        xml_request = """
            <Requests>
                <Request Type='GetBeachTournamentList' 
                        Fields='No Title Type NoEvent Code Gender Name CountryCode 
                                StartDateQualification StartDateMainDraw 
                                EndDateQualification EndDateMainDraw 
                                NbTeamsQualification NbTeamsMainDraw 
                                NbTeamsFromQualification' />
            </Requests>
        """

        # Set the URL for the request
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"

        # Send the request
        try:
            res = requests.post(url, data=xml_request, headers={'Content-Type': 'text/xml'})
            res.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return []

        # Parse the XML response
        soup = BeautifulSoup(res.content, 'xml')
        tournaments = soup.find_all('BeachTournament')

        # Define the fields of interest
        fields = [
            "No", "Title", "Type", "NoEvent", "Code", 
            "Gender", "Name", "CountryCode", 
            "StartDateQualification", "StartDateMainDraw", 
            "EndDateQualification", "EndDateMainDraw", 
            "NbTeamsQualification", "NbTeamsMainDraw", 
            "NbTeamsFromQualification"
        ]

        # Extract tournament details using a list comprehension
        tourn_list = [
            {field: tournament.get(field) for field in fields}
            for tournament in tournaments
        ]

        return tourn_list

    def fetch_beach_match_list(tournament_no, ref_info=False, round_info=False):
        """
        Fetch FIVB beach match list for a specific tournament.

        Parameters
        ----------
        tournament_no : str
            The ID of the tournament to fetch matches for.
        ref_info : bool, optional
            Include the referees of matches? Defaults to False.
        round_info : bool, optional
            Include the rounds metadata of matches? Defaults to False.

        Returns
        -------
        list of dicts
            A list of matches with fields such as NoInTournament, LocalDate, LocalTime, etc.
            
        Notes
        ------
        Documentation: 
            https://www.fivb.org/VisSDK/VisWebService/GetBeachMatchList.html
        WinnerRank:
            -3 = The team is qualified for the qualification tournament. This value is used for a confederation quota or a federation quota match. The match should not be used for seeding or ranking.
            -1 = The team is qualified for the main draw. This value is used for a qualification tournament match. The match should not be used for seeding or ranking.
            0 = Not ranked. The t3eam continues playing in the tournamnet
            >0 = The team is ranked at the specified rank.


        """
        
        # Base fields for the match list
        base_fields = [
            "NoTournament", "NoPlayerA1", "NoPlayerA2",
            "NoPlayerB1", "NoPlayerB2", "NoTeamA", "NoTeamB",
            "TeamAName", "TeamBName", "TeamAFederationCode", 
            "TeamBFederationCode", 
            "NoInTournament", "LocalDate", "LocalTime",
            "TeamAName", "TeamBName", "Court",
            "MatchPointsA", "MatchPointsB",
            "PointsTeamASet1", "PointsTeamBSet1",
            "PointsTeamASet2", "PointsTeamBSet2",
            "PointsTeamASet3", "PointsTeamBSet3",
            "DurationSet1", "DurationSet2", "DurationSet3",
            "WinnerRank", "LoserRank"
        ]

        # Include referees if specified
        if ref_info:
            base_fields.extend([
                "NoReferee1", "NoReferee2",
                "Referee1FederationCode", "Referee1Name",
                "Referee2FederationCode", "Referee2Name"
            ])

        # Include round info if specified
        if round_info:
            base_fields.extend([
                "NoRound",
                "RoundBracket", "RoundName", 
                "RoundPhase", "RoundCode"
            ])

        # Create the XML request string
        fields_string = ' '.join(base_fields)
        xml_request = f"""
            <Requests>
                <Request Type='GetBeachMatchList' 
                        Fields='{fields_string}'>
                    <Filter NoTournament='{tournament_no}' InMainDraw='true' />
                </Request>
            </Requests>
        """

        # Set the URL for the request
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"

        # Send the request
        try:
            res = requests.post(url, data=xml_request, headers={'Content-Type': 'text/xml'})
            res.raise_for_status()  # Raise an error for bad responses
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return []

        # Parse the XML response
        soup = BeautifulSoup(res.content, 'xml')
        matches = soup.find_all('BeachMatch')

        # Extract match details using a list comprehension
        match_list = [
            {field: match.get(field) for field in base_fields}
            for match in matches
        ]

        return match_list

    def fetch_beach_tournament_ranking(tournament_no):
        """
        Fetch FIVB beach ranking list for a specific tournament.

        Parameters
        ----------
        tournament_no : str
            The ID of the tournament to fetch matches for.

        Returns
        -------
        list of dicts
            A list of matches with fields such as EarnedPointsTeam, EarningsTotalTeam, Position, etc.
            
        Notes
        ------
        Documentation: 
            https://www.fivb.org/VisSDK/VisWebService/#GetBeachTournamentRanking.html

        """
        
        base_fields = [
            "EarnedPointsPlayer", "EarningsPlayer",
            "EarnedPointsTeam", "EarningsTotalTeam", 
            "Position", "Rank", "TeamFederationCode",
            "TeamName", "NoTeam"
        ]

        # Create the XML request string for each phase
        fields_string = ' '.join(base_fields)
        xml_request = f"""
        <Requests>
            <Request Type="GetBeachTournamentRanking" No="{tournament_no}" Fields='{fields_string}' />
        </Requests>
        """

        # Set the URL for the request
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"

        # Send the request
        try:
            # Send the request
            res = requests.post(url, data=xml_request, headers={'Content-Type': 'text/xml'})
            res.raise_for_status()
            
            # Parse the XML response
            soup = BeautifulSoup(res.content, 'xml')
            tournaments = soup.find('BeachTournamentRanking')
            
            if tournaments is None:
                print("No BeachTournamentRanking element found in response")
                tournament_data = []
            else:
                # Filter for only Tag elements and create dictionary
                tournament_data = [
                    {**{field: tournament.get(field) for field in base_fields}, "NoTournament": tournament_no}
                    for tournament in tournaments.find_all()
                    if tournament.name is not None  # This filters out NavigableString objects
                ]
            
            return tournament_data

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            tournament_data = []
        except Exception as e:
            print(f"Error processing data: {e}")
            tournament_data = []

    def fetch_beach_team(team_no):
        """
        Fetch FIVB beach team meta-data a specific tournament.

        Parameters
        ----------
        team_no : str
            The TeamNo of the team to fetch meta-data for. - This number changes across beach tournaments.

        Returns
        -------
        list of dicts
            A list of matches with fields such as EarnedPointsTeam, EarningsTotalTeam, Rank, etc.
            
        Notes
        ------
        Documentation: 
            https://www.fivb.org/VisSDK/VisWebService/GetBeachTeam.html

        """
        
        base_fields = [
            "NoPlayer1", "NoPlayer2", "Name", "Position", "Rank", "TeamFederationCode",
            "EarningsPlayer", "EarnedPointsTeam", "EarnedPointsPlayer",
            "EarningsTeam", "EntryPoints1", "EntryPoints2", "IsInQualification",
            "IsInMainDraw", "MainDrawSeed1", "MainDrawSeed2", "No",
            "NoShirt1", "NoShirt2", "NoTournament", "PositionInMainDraw", 
            "PositionInQualification", "PositionInEntry", "QualificationPoints1", 
            "QualificationPoints2", "TechnicalPoints1", "TechnicalPoints2"
            ]

        # Create the XML request string for each phase
        fields_string = ' '.join(base_fields)
        xml_request = f"""
        <Requests>
            <Request Type="GetBeachTeam" No="{team_no}" Fields='{fields_string}' />
        </Requests>
        """

        # Set the URL for the request
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"

        # Send the request
        try:
            # Send the request
            res = requests.post(url, data=xml_request, headers={'Content-Type': 'text/xml'})
            res.raise_for_status()
            
            # Parse the XML response
            soup = BeautifulSoup(res.content, 'xml')
            teams = soup.find('BeachTeam')
            
            if teams is None:
                print("No BeachTeam element found in response")
                team_data = []
            else:
                # Filter for only Tag elements and create dictionary
                team_data = [
                    {field: teams.get(field) for field in base_fields}
                ]
            
            return team_data

        except requests.RequestException as e:
            print(f"Request failed: {e}")
            team_data = []
        except Exception as e:
            print(f"Error processing data: {e}")
            team_data = []

    def fetch_beach_stats_list(tournament_no):
        """
        Fetch FIVB beach stats list from a specific tournament.

        Parameters
        ----------
        tournament_no : str
            The ID of the tournament to fetch matches for.

        Returns
        -------
        list of dicts
            A list of stats - BlockPoint, SpikeTotal, SpikePoint, SpikeFault, etc.
            
        Notes
        ------
        Documentation: 
            https://www.fivb.org/VisSDK/VisWebService/GetBeachTeam.html

        """
        base_fields = [
            "No", "NoShirt",  "NoItem", "BlockContinue", "BlockFault", "BlockPoint", "BlockTotal", 
            "DigContinue", "DigExcellent", "DigFault", "DigTotal", "ReceptionContinue", "ReceptionExcellent", 
            "ReceptionFault", "ReceptionTotal", "ServeContinue", "ServeFault", "ServePoint", "ServeTotal", 
            "SetContinue", "SetExcellent", "SetFault", "SetTotal", "SpikeContinue", "SpikeFault", 
            "SpikePoint", "SpikeTotal", "AttemptTotal", "PointTotal", "TeamFault", "OpponentError",
        ]

        # Join fields as a space-separated string
        fields_string = ' '.join(base_fields)

        # Construct the XML request
        xml_request = f"""
        <Request Type="GetBeachStatisticList" SumBy="Tournament" Fields="{fields_string}">
            <Filter NoTournaments="{tournament_no}" />
            <Relation Name="Player" Fields="No TeamName NoTeam FederationCode"/>
        </Request>
        """

        # Set the URL for the request
        url = "https://www.fivb.org/vis2009/XmlRequest.asmx"

        # Make the request
        res = requests.post(url, data=xml_request, headers={'Content-Type': 'text/xml'})

        # Parse the XML response
        soup = BeautifulSoup(res.content, 'xml')
        stats_data = []

        # Iterate through each VolleyStatistic element
        for stat in soup.find_all('VolleyStatistic'):
            # Get the base fields
            stat_data = {field: stat.get(field) for field in base_fields}
            stat_data["NoTournament"] = tournament_no

            # Extract player information if present
            player = stat.find('Player')
            if player:
                # Add player details to the stats data
                stat_data.update({
                    "PlayerNo": player.get("No"),
                    "PlayerTeamName": player.get("TeamName"),
                    "PlayerFederationCode": player.get("FederationCode")
                })

            # Append the enriched data to the stats_data list
            stats_data.append(stat_data)
        return stats_data
