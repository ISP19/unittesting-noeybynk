def unique(list):
    """Return a list containing only the first occurence of each distint
       element in list.  That is, all duplicates are omitted.

    Arguments:
        list: a list of elements (not modified)
    Returns:
        a new list containing only distinct elements from list

    Examples:
    >>> unique([5])
    [5]
    >>> unique(['b','a','a','b','b','b','a','a'])
    ['b', 'a']
    >>> unique([])
    []
    >>> unique(['N','n','o','e','N','y'])
    ['N', 'n', 'o', 'e', 'y']
    >>> unique([1,1,1,1,1])
    [1]
    >>> unique([1,[1,2],3,[1,2]])
    [1, [1, 2], 3]
    """

    list2 = []
    for i in list:
        if i not in list2:
            list2.append(i)
    return list2

if __name__ == "__main__":
    """Run the doctests in all methods."""
    import doctest
    doctest.testmod(verbose=True)

print (unique((1,"2")))