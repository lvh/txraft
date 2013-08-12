from twisted.protocols import amp

class AppendEntries(amp.Command):
    """Instructs the recipients to append provided entries to their logs.

    This is the primary replication mechanism. It is also used as a
    heartbeat.

    """
    arguments = [
        ("term", amp.Integer()),
        ("leaderId", amp.String()),
        ("prevLogIndex", amp.Integer()),
        ("prevLogTerm", amp.Integer()),
        ("entries", amp.AmpList([
            ("term", amp.Integer()),
            ("index", amp.Integer()),
            ("command", amp.String())
        ])),
        ("commitIndex", amp.Integer())
    ]
    response = [
        ("term", amp.Integer()),
        ("success", amp.Boolean())
    ]


class RequestVotes(amp.Command):
    """Requests a vote.
    """
    arguments = [
        ("candidateId", amp.String()),
        ("term", amp.Integer()),
        ("lastLogIndex", amp.Integer()),
        ("lastLogTerm", amp.Integer()),
    ]
    response = [
        ("term", amp.Integer()),
        ("voteGranted", amp.Boolean())
    ]
