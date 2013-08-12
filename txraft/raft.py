"""
Follower logic.
"""
from twisted.internet import reactor, task
from txraft.commands import RequestVotes


class Server(object):
    """A server, taking part in the Raft protocol.
    """
    def __init__(self):
        self.term = 0
        self.peers = set()
        self.log = None



class Follower(object):
    """Follower behavior.

    """
    def __init__(self, server, _clock=reactor):
        self.timeout = _clock.callLater(10, self.beginElection)


    def timeout(self):
        """Heartbeat timeout, start election round.

        This increments the term, switches to candidate behavior, and
        causes it to start collecting votes.

        """
        self.server.term += 1
        self.server.behavior = behavior = Candidate(self.server)
        behavior.requestVotes()



class Candidate(object):
    """Candidate behavior.

    """
    def __init__(self, server):
        self.server = server
        self.votes += 1


    def requestVotes(self):
        for peer in self.peers:
            d = peer.callRemote(RequestVotes,
                candidateId=None,  # TODO: point to self
                term=self.server.term,
                lastLogIndex=len(self.server.log),
                lastLogTerm=self.server.log[-1].term)
            d.addCallback(self._voteResponseReceived)


    def _voteResponseReceived(self, result):
        """A single vote response was received.
        """
        if self.server.term < result["term"]:
            self.server.term = result["term"]

        if result["voteGranted"]:
            self.votes += 1
