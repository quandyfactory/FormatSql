FormatSql README

FormatSql takes unformatted SQL and returns (wait for it) formatted SQL. Right now it's pretty rudimentary and not very cutomizable - but I plan to change that over time.

## Author

* Author: Ryan McGreal

* Email: [ryan@quandyfactory.com][1]

* Homepage: [http://quandyfactory.com/projects/7/formatsql][2]

* Repository: [http://github.com/quandyfactory/FormatSql][3]

## Licence

Released under the GNU General Public Licence, Version 2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.html][4]

## This Version

* Version: 0.5

* Release Date: 2009-09-15

## Revision History

### Version: 0.5

* Release Date: 2009-09-15

* Changes:

    * Fixed number of tabs for consistency of alignment.
    * Added convert_tabs_to_spaces() function, which converts tabs to blocks of (default is 8).
    * Added fix_tab_spaces_for_keywords() function, which checks the first word in each line and adds enough spaces to bump it up to the total number of spaces per converted tab (default is 8).

### Version: 0.41

* Release Date: 2009-08-27

* Changes:

    * Added "How to Use" section to README file, including a simple sample code.
    
    
### Version: 0.4

* Release Date: 2009-08-27

* Changes:

    * Replaced way lame replace_word_match function with a lookup against a hashtable
    
### Version: 0.3

* Release Date: 2009-08-27

* Changes:

    * Fixed bug that split CONVERT into CON\n\t\t\tVERT by adding replace_word_match function to replace on exact word
    * Removed stray space after the last tab and before the indented text
    
    
### Version: 0.2

* Release Date: 2009-08-26

* Changes:

    * Added support for inline and block comments
    * Split more sql format operations into individual functions (prepare_inline_comments, set_linebreaks_and_tabs, convert_keywords_to_uppercase)
    
    
### Version: 0.1

* Release Date: 2009-08-20

* Changes:

    * First Commit

## Requirements and Recommendations

* Python 2.5 or newer (not Python 3)

## How to Use

It's really simple. 

1. Save the formatsql.py file someplace where the python PATH will find it.
2. Next, `import formatsql` into your project.
3. Run the formatsql.format_sql(sql) function to get your formatted sql.

### Example code

    """
    This code formats sql using the formatsql.py module.
    """
    
    import formatsql
    sql = "select convert(varchar(10),a.col1,121) as thedate, a.col2 as whatever, b.col3 as fullname, c.col4 as title -- inline comment\nfrom atable a inner join btable b on a.colx = b.colx -- another inline comment\ninner join ctable c on a.coly = c.coly /* this is a block quote */ where a.id < 100 order by a.col1"
    formatted_sql = formatsql.format_sql(sql)
    print formatted_sql

Seriously, that's it.

## Outstanding Issues and Missing Features

### Known Bugs

#### Line Breaks inside Comment Blocks

This function currently eats line breaks inside comment blocks. Not cool.

#### SQL Keywords Without Whitespace

SQL keywords not surrounded by whitespace are not converted to uppercase, e.g.: `convert(varchar(10),dDate,121)` - "convert" and "varchar" are left as lowercase.

#### Function Parameters

If the comma-separated parameters in a function have spaces, it breaks the function into multiple lines, e.g.

    convert(varchar(10), dDate, 121)

becomes:

    convert(varchar(10), 
                    dDate, 
                    121)

#### Parenthesized List Recognition

It only recognizes parenthesized lists of fields (in e.g. an `INSERT` query) if the parentheses are surrounded by whitespace. 
For example, it will correctly format the first part of this query but not the second:

    insert into tblWhatever ( field1, field2, field3 ) values (@field1, @field2, @field3)
    
as:

    INSERT                 
    INTO                   tblWhatever 
                           (
                           field1, 
                           field2, 
                           field3 
                           )
                           
    VALUES                 (@field1, 
                           @field2, 
                           @field3)


### Indenting Code Blocks

It does not indent whole blocks of code, e.g. inside conditionals or `BEGIN ... END` blocks. You need to do that manually.

### Customization

Right now it formats your SQL the way it formats it - and you'll *learn* to *like it*! It would be nice if you could customize the format.

### Syntax Highlighting

More of a 'nice to have' than a requirement, but a boy can dream.

### Support for different SQL dialects

Right now it's optimized for SQL Server, simply because that's the version of SQL I use in which anyone cares about the format.

[1]: mailto:ryan@quandyfactory.com

[2]: http://quandyfactory.com/projects/7/formatsql

[3]: http://github.com/quandyfactory/FormatSql

[4]: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html
