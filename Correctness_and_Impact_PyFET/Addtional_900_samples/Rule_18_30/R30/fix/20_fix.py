class Checker(doctest.OutputChecker):
    """
    Check the docstrings
    """
    obj_pattern = re.compile('at 0x[0-9a-fA-F]+>')
    vanilla = doctest.OutputChecker()
    rndm_markers = {'# random', '# Random', '#random', '#Random', "# may vary",
                    "# uninitialized", "#uninitialized"}
    stopwords = {'plt.', '.hist', '.show', '.ylim', '.subplot(',
                 'set_title', 'imshow', 'plt.show', '.axis(', '.plot(',
                 '.bar(', '.title', '.ylabel', '.xlabel', 'set_ylim', 'set_xlim',
                 '# reformatted', '.set_xlabel(', '.set_ylabel(', '.set_zlabel(',
                 '.set(xlim=', '.set(ylim=', '.set(xlabel=', '.set(ylabel='}
