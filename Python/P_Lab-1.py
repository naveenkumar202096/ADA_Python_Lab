#Write a function which return all the unique palindromes from a given string
def uniquePalindromes(string):
    x=string.split()
    k = []  # note how we put it *outside* the loop, so it persists across each iteration without being reset
    for i in x:
        rev= ''.join(reversed(i))
        if i.casefold() == rev.casefold():
            k.append(i.casefold())  
            # the print statement isn't what we want
        # no need for an else statement - the loop will continue anyway
    # now, once all elements have been visited, return the set of unique elements from k
    return set(k)

print (uniquePalindromes("Malayalam"))