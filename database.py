def extract(query):
    """extract takes in a `query` API function (which returns the first 5 usernames, lexicographically sorted,
    that start with a prefix) and returns the sorted list of all usernames in the database.
    For example, the `query` function in provided in `main` works as follows:

    query("a") #=> ["abracadara", "al", "alice", "alicia", "allen"]
    query("ab") #=> ["abracadara"]
    The following implementation would pass the assertion in `main`, but is not a correct solution since it
    works only for that example `query`:
    def extract(query):
        return query("ab") + query("al") + query("altercation") + query("b") + query("el") + query("ev") + query("m")
    Your goal is to write an `extract` method that is correct for any provided `query`.
    """
    # YOUR CODE HERE
        result = []
    for i in range(97, 122):
        if query(chr(i)):
            result.extend(query(chr(i)))
        else:
            pass
        for j in range(97, 122):
            if query(chr(i) + chr(j)):
                result.extend(query(chr(i) + chr(j)))
            else:
                pass
            for k in range(97, 122):
                if query(chr(i) + chr(j) + chr(k)):
                    result.extend(query(chr(i) + chr(j) + chr(k)))
    result = sorted(list(set(result)))
    return result

def main():
    """Runs your solution -- no need to update (except to maybe try out different databases)."""
    # Sample implementation of the autocomplete API
    database = ["abracadara", "al", "alice", "alicia", "allen", "alter", "altercation", "bob", "element", "ello", "eve",
                "evening", "event", "eventually", "mallory"]
    query = lambda prefix: [d for d in database if d.startswith(prefix)][:5]
    assert extract(query) == database


main()
