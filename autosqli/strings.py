# From AutoSQLi

# tampers we shouldn't use because they're too specifics
# TODO: move to a white-list based way of getting tampers to avoid problems
# when updating WhatWaf or things like that, you know.
# TODO: also, I would like to use only tampers that are natively available to
# sqlmap, too avoid priority problems.
# XXX I'll just finish the gross architecture before working on this.
BANNED_TAMPERS = ["base64encode"]
