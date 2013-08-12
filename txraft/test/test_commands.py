from twisted.trial import unittest
from txampext import commandtests
from txraft import commands


class AppendEntriesTests(unittest.TestCase, commandtests.CommandTestMixin):
    """AppendEntries can serialize and deserialize.

    """
    command = commands.AppendEntries
    argumentObjects = {
        "term": 2,
        "leaderId": "leader",
        "prevLogIndex": 3,
        "prevLogTerm": 2,
        "entries": [
            {"term": 2, "index": 4, "command": "x"}
        ],
        "commitIndex": 1
    }
    argumentStrings = {
        "term": "2",
        "leaderId": "leader",
        "prevLogIndex": "3",
        "prevLogTerm": "2",
        "entries": "\x00\x07command\x00\x01x"
                   "\x00\x05index\x00\x014"
                   "\x00\x04term\x00\x012\x00\x00",
        "commitIndex": "1"
    }
    responseObjects = {
        "term": 2,
        "success": True
    }
    responseStrings = {
        "term": "2",
        "success": "True"
    }



class RequestVotesTests(unittest.TestCase, commandtests.CommandTestMixin):
    """RequestVotes can serialize and deserialize.

    """
    command = commands.RequestVotes
    argumentObjects = {
        "candidateId": "candidate",
        "term": 1,
        "lastLogIndex": 1,
        "lastLogTerm": 1,
    }
    argumentStrings = {
        "candidateId": "candidate",
        "term": "1",
        "lastLogIndex": "1",
        "lastLogTerm": "1",
    }
    responseObjects = {
        "term": 1,
        "voteGranted": True
    }
    responseStrings = {
        "term": "1",
        "voteGranted": "True"
    }
