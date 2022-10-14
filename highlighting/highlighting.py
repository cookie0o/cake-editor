from PyQt5.QtCore import *
from PyQt5.QtGui import *
import configparser
import os

upper_dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..'))


settings = upper_dir+"/settings/config.ini"
config = configparser.ConfigParser()
config.read(settings)
## set button colors
KeywordColorChnage = (config.get('-color-', 'KeywordColorChnage').replace(",", " ").split())
OperatorColorChnage = (config.get('-color-', 'OperatorColorChnage').replace(",", " ").split())
BraceColorChnage = (config.get('-color-', 'BraceColorChnage').replace(",", " ").split())
DefClassColorChnage = (config.get('-color-', 'DefClassColorChnage').replace(",", " ").split())
StringColorChnage = (config.get('-color-', 'StringColorChnage').replace(",", " ").split())
String2ColorChnage = (config.get('-color-', 'String2ColorChnage').replace(",", " ").split())
CommentColorChnage = (config.get('-color-', 'CommentColorChnage').replace(",", " ").split())
SelfColorChnage = (config.get('-color-', 'SelfColorChnage').replace(",", " ").split())
NummbersColorChnage = (config.get('-color-', 'NummbersColorChnage').replace(",", " ").split())
language = (config.get('-settings-', 'language'))




def format(color, style):
    """
    Return a QTextCharFormat with the given attributes.
    """
    _color = QColor()
    if type(color) is not str:
        _color.setRgb(int(color[0]), int(color[1]), int(color[2]))
    else:
        _color.setNamedColor(color)

    _format = QTextCharFormat()
    _format.setForeground(_color)
    if 'bold' in style:
        _format.setFontWeight(QFont.Bold)
    if 'italic' in style:
        _format.setFontItalic(True)

    return _format

# 150, 85, 140
# 147, 112, 219
# 'defclass': format([220, 220, 255], 'bold'),
# Syntax styles that can be shared by all languages

STYLES = {
    'keyword': format(KeywordColorChnage, ""),
    'operator': format(OperatorColorChnage, ""),
    'brace': format(BraceColorChnage, ""),
    'defclass': format(DefClassColorChnage, ""),
    'string': format(StringColorChnage, ""),
    'string2': format(String2ColorChnage, ""),
    'comment': format(CommentColorChnage, ""),
    'self': format(SelfColorChnage, ""),
    'numbers': format(NummbersColorChnage, ""),
}


class PythonHighlighter(QSyntaxHighlighter):

    # keywords
    from highlighting.keywords import keywordsPY, keywordsJ, keywordsLua

    # operators
    operators = [
        '=',
        # Comparison
        '==', '!=', '<', '<=', '>', '>=',
        # Arithmetic
        '\+', '-', '\*', '/', '//', '\%', '\*\*',
        # In-place
        '\+=', '-=', '\*=', '/=', '\%=',
        # Bitwise
        '\^', '\|', '\&', '\~', '>>', '<<',
    ]

    # braces
    braces = [
        '\{', '\}', '\(', '\)', '\[', '\]',
    ]

    def __init__(self, document):
        QSyntaxHighlighter.__init__(self, document)

        # Multi-line strings (expression, flag, style)
        # FIXME: The triple-quotes in these two lines will mess up the
        # syntax highlighting from this point onward
        self.tri_single = (QRegExp("'''"), 1, STYLES['string2'])
        self.tri_double = (QRegExp('"""'), 2, STYLES['string2'])

        rules = []

        # Keyword, operator, and brace rules
        if language == "Python":
            rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                    for w in PythonHighlighter.keywordsPY]
        elif language == "Java":
            rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                    for w in PythonHighlighter.keywordsJ]
        elif language == "Lua":     
            rules += [(r'\b%s\b' % w, 0, STYLES['keyword'])
                    for w in PythonHighlighter.keywordsLua]

        #
        rules += [(r'%s' % o, 0, STYLES['operator'])
                for o in PythonHighlighter.operators]
        rules += [(r'%s' % b, 0, STYLES['brace'])
                for b in PythonHighlighter.braces]

        # All other rules
        rules += [
            # 'self'
            (r'\bself\b', 0, STYLES['self']),

            # Double-quoted string, possibly containing escape sequences
            (r'"[^"\\]*(\\.[^"\\]*)*"', 0, STYLES['string']),
            # Single-quoted string, possibly containing escape sequences
            (r"'[^'\\]*(\\.[^'\\]*)*'", 0, STYLES['string']),

            # 'def' followed by an identifier
            (r'\bdef\b\s*(\w+)', 1, STYLES['defclass']),
            # 'class' followed by an identifier
            (r'\bclass\b\s*(\w+)', 1, STYLES['defclass']),

            # From '#' until a newline
            (r'#[^\n]*', 0, STYLES['comment']),

            # Numeric literals
            (r'\b[+-]?[0-9]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?0[xX][0-9A-Fa-f]+[lL]?\b', 0, STYLES['numbers']),
            (r'\b[+-]?[0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?\b', 0, STYLES['numbers']),
        ]

        # Build a QRegExp for each pattern
        self.rules = [(QRegExp(pat), index, fmt)
                      for (pat, index, fmt) in rules]

    def highlightBlock(self, text):
        """Apply syntax highlighting to the given block of text.
        """
        # Do other syntax formatting
        for expression, nth, format in self.rules:
            index = expression.indexIn(text, 0)

            while index >= 0:
                # We actually want the index of the nth match
                index = expression.pos(nth)
                length = len(expression.cap(nth))
                self.setFormat(index, length, format)
                index = expression.indexIn(text, index + length)

        self.setCurrentBlockState(0)

        # Do multi-line strings
        in_multiline = self.match_multiline(text, *self.tri_single)
        if not in_multiline:
            in_multiline = self.match_multiline(text, *self.tri_double)

    def match_multiline(self, text, delimiter, in_state, style):

        # If inside triple-single quotes, start at 0
        if self.previousBlockState() == in_state:
            start = 0
            add = 0
        # Otherwise, look for the delimiter on this line
        else:
            start = delimiter.indexIn(text)
            # Move past this match
            add = delimiter.matchedLength()

        # As long as there's a delimiter match on this line...
        while start >= 0:
            # Look for the ending delimiter
            end = delimiter.indexIn(text, start + add)
            # Ending delimiter on this line?
            if end >= add:
                length = end - start + add + delimiter.matchedLength()
                self.setCurrentBlockState(0)
            # No; multi-line string
            else:
                self.setCurrentBlockState(in_state)
                length = len(text) - start + add
            # Apply formatting
            self.setFormat(start, length, style)
            # Look for the next match
            start = delimiter.indexIn(text, start + length)

        # Return True if still inside a multi-line string, False otherwise
        if self.currentBlockState() == in_state:
            return True
        else:
            return False