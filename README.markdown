FormatSql README

FormatSql takes unformatted SQL and returns (wait for it) formatted SQL. Right now it's pretty rudimentary and not very cutomizable - but I plan to change that over time.

## Author

* Author: Ryan McGreal

* Email: [ryan@quandyfactory.com][1]

* Homepage: [http://quandyfactory.com/projects/formatsql][2]

* Repository: [http://github.com/quandyfactory/FormatSql][3]

## Licence

Released under the GNU General Public Licence, Version 2:

[http://www.gnu.org/licenses/old-licenses/gpl-2.0.html][4]

## This Version

* Version: 0.2

* Release Date: 2009-08-26

## Revision History

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

## Things I Wish FormatSql Had

### Customization

Right now it formats your SQL the way it formats it - and you'll *learn* to *like it*! It would be nice if you could customize the format.

### Syntax Highlighting

More of a 'nice to have' than a requirement, but a boy can dream.

### Support for different SQL dialects

Right now it's optimized for SQL Server, simply because that's the version of SQL I use in which anyone cares about the format.

[1]: mailto:ryan@quandyfactory.com

[2]: http://quandyfactory.com/projects/formatsql

[3]: http://github.com/quandyfactory/FormatSql

[4]: http://www.gnu.org/licenses/old-licenses/gpl-2.0.html

