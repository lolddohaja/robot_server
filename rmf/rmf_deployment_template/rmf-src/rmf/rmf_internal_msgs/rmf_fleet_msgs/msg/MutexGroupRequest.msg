# This message is used to attempt to claim a mutex group. It should be sent
# periodically for the entire duration that the claimer needs the mutex because
# mutex groups have a limited-time leasing period that will timeout if a request
# heartbeat is not received in some amount of time.

# Name of the mutex group that is being claimed
string group

# Name of the agent that is trying to claim the mutex group.
uint64 claimant

# Time stamp of when the claim request began. The same time stamp should be used
# for all subsequent heartbeat messages related to this claim. If the claim time
# changes then this claim will be treated a new claim and may be deprioritized.
# Earlier claims have priority over later claims.
builtin_interfaces/Time claim_time

# What kind of request is this?
uint32 mode
# Request to release the mutex group from this claimer
uint32 MODE_RELEASE=0
# Request to lock the mutex group for this claimer
uint32 MODE_LOCK=1
