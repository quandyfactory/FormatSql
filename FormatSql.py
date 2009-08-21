"""
FormatSql - lets you format SQL using the format_sql() function.
"""

__version__ = '0.1'
__author__ = 'Ryan McGreal ryan@quandyfactory.com'
__copyright__ = 'Copyright 2009 by Ryan McGreal. Licenced under GPL version 2. http://www.gnu.org/licenses/gpl-2.0.html'


def replace_whitespace_with_space(char):
    """
    Takes a character and returns either the character (if it's not a whitespace character) or a single space
    """
    whitespace = '\t\n\x0b\x0c\r '
    if char in whitespace:
        return ' '
    else:
        return char

def convert_whitespaces_to_spaces(instring):
    """
    Takes a string and converts any whitespace characters (spaces, tabs, returns, etc.) to spaces
    """
    return ''.join([replace_whitespace_with_space(s) for s in instring])
   
def remove_multiple_spaces(instring):
    """
    Takes a string and removes any multiple spaces
    """
    while '  ' in instring:
        instring = instring.replace('  ', ' ')
    return instring.strip()

def format_sql(instring):
    """
    Takes an unformatted string of SQL and returns a formatted string:
    * Removes multiple white space
    * Converts SQL keywords to UPPERCASE
    * Sets linebreaks and tabs for SQL statements
    """
    instring = ' ' + instring

    # convert existing tabs and line breaks into spaces
    instring = convert_whitespaces_to_spaces(instring)

    # eliminate multiple spaces
    instring = remove_multiple_spaces(instring)

    #convert string to list of individual words
    MyInWords = instring.split(' ')
    MyOutWords = []

    # list of SQL keywords to treat differently
    keywords = 'absolute action ada add all allocate alter and any are as asc assertion at authorization avg backup begin between bit bit_length both break browse bulk by cascade cascaded case cast catalog char char_length character character_length check checkpoint close clustered coalesce collate collation column commit compute connect connection constraint constraints contains containstable continue convert corresponding count create cross current current_date current_time current_timestamp current_user cursor database date day dbcc deallocate dec decimal declare default deferrable deferred delete deny desc describe descriptor diagnostics disconnect disk distinct distributed domain double drop dummy dump else end end-exec errlvl escape except exception exec execute exists exit external extract false fetch file fillfactor first float for foreign fortran found freetext freetexttable from full function get global go goto grant group having holdlock hour identity identity_insert identitycol if immediate in in include index index indicator initially inner inner input insensitive insert int integer intersect interval into into is isolation join key kill language last leading left level like lineno load local lower match max min minute module month names national natural nchar next no nocheck nonclustered none not null nullif numeric octet_length of off offsets on only open opendatasource openquery openrowset openxml option option or order outer output over overlaps pad partial pascal percent plan position precision prepare preserve primary print prior privileges proc procedure public raiserror read readtext real reconfigure references relative replication restore restrict return revoke right rollback rowcount rowguidcol rows rule save schema scroll second section select session session_user set setuser shutdown size smallint some space sql sqlca sqlcode sqlerror sqlstate sqlwarning statistics substring sum system_user system_user table temporary textsize then time timestamp timezone_hour timezone_minute to top trailing tran transaction translate translation trigger trim true truncate tsequal union unique unknown update updatetext upper usage use user using value values varchar varying view waitfor when whenever where while with work write writetext year zone'.split(' ')

    # convert SQL keywords to uppercase
    for word in MyInWords:
        thisword = word.lower()
        if thisword in keywords:
            MyOutWords.append(thisword.upper())
        else:
            MyOutWords.append(word)
    instring = ' ' + ' '.join(MyOutWords) + ' '

    # fix line breaks and tabs
    instring = instring.replace(' CREATE ', ' \n\nCREATE \t\t\t')
    instring = instring.replace(' ALTER ', ' \n\nALTER \n')
    instring = instring.replace(' PROCEDURE ', '  \nPROCEDURE \t\t')
    instring = instring.replace(' FUNCTION ', '  \nFUNCTION \t\t')
    instring = instring.replace(' EXEC ', ' \n\nEXEC \t\t\t')
    instring = instring.replace(' SELECT ', ' \n\nSELECT \t\t\t')
    instring = instring.replace(' UPDATE ', ' \n\nUPDATE \t\t\t')
    instring = instring.replace(' INSERT ', ' \n\nINSERT \t\t\t')
    instring = instring.replace(' DELETE ', ' \n\nDELETE \t\t\t')
    instring = instring.replace(' INTO ', ' \nINTO \t\t\t')
    instring = instring.replace(' SET ', ' \nSET \t\t\t')
    instring = instring.replace(' INNER JOIN ', ' \nINNER JOIN \t\t')
    instring = instring.replace(' LEFT JOIN ', ' \nLEFT JOIN \t\t')
    instring = instring.replace(' RIGHT JOIN ', ' \nRIGHT JOIN \t\t')
    instring = instring.replace(' WHERE ', ' \nWHERE \t\t\t')
    instring = instring.replace(' HAVING ', ' \nHAVING \t\t\t')
    instring = instring.replace('GROUP BY ', ' \nGROUP BY \t\t')
    instring = instring.replace('ORDER BY ', ' \nORDER BY \t\t')
    instring = instring.replace(' FROM ', '\nFROM \t\t\t')
    instring = instring.replace(' ON ', ' ON \n\t\t\t\t')
    instring = instring.replace(' AND ', ' \n\t\t\tAND ')
    instring = instring.replace(' CASE ', ' \n\t\t\tCASE ')
    instring = instring.replace(' BEGIN ', ' \n\t\t\tBEGIN ')
    instring = instring.replace(' WHEN ', ' \n\t\t\t\tWHEN ')
    instring = instring.replace(' THEN ', ' \n\t\t\t\tTHEN ')
    instring = instring.replace(' ELSE ', ' \n\t\t\t\tELSE ')
    instring = instring.replace(' END ', ' \n\t\t\tEND ')
    instring = instring.replace(' DROP TABLE ', ' \n\nDROP TABLE \t\t')
    instring = instring.replace(' SET ANSI_NULLS ON ', ' \nSET ANSI_NULLS ON ')
    instring = instring.replace(' SET QUOTED_IDENTIFIER ON', ' \nSET QUOTED_IDENTIFIER ON ')
    instring = instring.replace(' GO ', '\nGO\n')
    instring = instring.replace('\tGO ', '\t\nGO\n')
    instring = instring.replace(', ', ', \n\t\t\t\t')
    
    #eliminate multiple spaces
    instring = remove_multiple_spaces(instring)
    return instring.strip()
