from pickle import TRUE


def create_appender(default_value):
    """
    Create an empty list. Return a function which will append its only parameter to this list
    when called and then return a copy of the modified list.
    If no parameter is passed, it will add `default_value` to the list.

    Example:
        appender = create_appender(5)
        appender(1) # [1]
        appender(2) # [1, 2]
        appender() # [1, 2, 5]

        appender2 = create_appender(0)
        appender2(2) # [2]
    """
    temp = []
    while True:
        temp.append(default_value)
        yield temp

    pass


def fibonacci_closure():
    """
    Return a closure (function) that will generate elements of the Fibonacci sequence (starting
    from 1) when called repeatedly.
    Example:
        g = fibonacci_closure()
        g() # 1
        g() # 1
        g() # 2
        g() # 3
        ...
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

    
    pass


def word_extractor(sentence: str):
    """
    Return a generator that will iterate through individual words from the input sentence.
    Words are separated by the following separators: space (' '), dot ('.'), exclamation mark ('!')
    and question mark ('?'). Skip empty words and separators.

    If you encounter the word "stop", ignore the word and stop the generator.

    Example:
        sentence = "Hello world. How are you doing today? I'm doing fine!"
        for word in word_extractor(sentence):
            print(i)
        # "Hello", "world", "How", "are", "you", "doing", "today", ...

        sentence = "Hello world stop this is not extracted anymore."
        for word in word_extractor(sentence):
            print(i)
        # "Hello", "world"
    """
    pass


def transform_file(src: str, dst: str, keyword: str):
    """
    Open file located at `src`, keep only lines that contain the `keyword`, sort them in descending
    order and write them to file located at `dst`.

    If `keyword` is empty, raise an Exception with message "invalid keyword".
    If `src` does not exist, raise an Exception with message "file not found".

    Example:
        transform_file('in.txt', 'out.txt', 'or')

        in.txt:
        barrens
        stormwind
        gondor
        ashenvale
        hogwarts
        yavin
        coruscant

        out.txt:
        stormwind
        gondor
        coruscant
    """
    pass


def tree_walker(tree, order):
    """
    Write a generator that traverses `tree` in the given `order` ('inorder', 'preorder' or 'postorder').
    You should know this from 'Algoritmy II'.
    The tree is represented with nested tuples (left subtree, value, right subtree).
    If there is no subtree, it will be marked as None.
    Example:
        tree = (((None, 8, None), 3, (None, 4, None)), 5, (None, 1, None))
            5
           / \
          3   1
         / \
        8   4
        list(tree_walker(tree, 'inorder')) == [8, 3, 4, 5, 1]
        list(tree_walker(tree, 'preorder')) == [5, 3, 8, 4, 1]
        list(tree_walker(tree, 'postorder')) == [8, 4, 3, 1, 5]
    """
    pass

appender = create_appender(5)
appender(1)