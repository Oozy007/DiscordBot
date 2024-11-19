messageToEveryone = " u need to stop playing League ASAP. Exams are in a few weeks"
messageToHamelsama = " u don't have exams, but we do"

def get_response(input, user):
    loweInput = input.lower()
    LeagueVocab = ["league", "lig", "lol", "league of legends", "aram", "rank", "ranked"]#terms we use to refer to league of legends

    for word in LeagueVocab:
        if word in loweInput:
            if user.name == "hamelsama":#my friend who doesn't have exams coming soon
                return user.mention + messageToHamelsama
            return user.mention + messageToEveryone