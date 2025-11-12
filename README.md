
## Tinkering PDFs

This project is designed for a specific PDF structure and may not work correctly with other formats.


## 🧠 Motivation

All started for the need of having the data of a PDF file from a municipal website with waste days and types of monthly pickup, translated into files to be used afterwards in other ways.


## ⚙️ How It Works

The main package I chose for extracting raw data from the file is "pypdf".
Already at the start trying different libraries none were able to extract the data as tables so I've ended up picking one, and tweked it until it pulled the data the way i wanted.


## 🧩 Formatting

Working on the data formatting to pull some human readable strings took some time and research, all worthy since without the proper format like in a CSV file it was still good for a start.
One more thing which was hard(at least for me), structuring the way it was showed and by looking at the strings 
a lot of unnecessary stuff I had to get rid off, like characters and symbols.
Luckly at the beginning of the strings there were set the days int, so by making a function which picked the start of the day one  and going until the last saved a lot of time.
Pages contain 2 months for each and in raw data month name stays on the top of each one, so by using that function it picks all the days of the month and adds those to a list, by returning two of them.
Everything gets written to files which end up being the 'year_month.txt' in proper folders of years found, this way becomes easier when you need to pick a specific month of the year required for using the data inside of it.

Strings formatted are structured as above:

    [int(day), day_of_the_week_abbreviate, type_of_trash, places_for_other_things(not used atm)]


## 📦 Requirements (beside standard libraries)

-Python 3.12
-pypdf==6.2.0


## 🛠️ Maintenance 

Since the municipal personnel could change the format, a first look before parsing the file could be the best, if no change has been made, a new program can be structured in order to pull data from the website and pushed through the parser automatically.
The program is structured into small modular pieces, most of the functions get imported from a utils folder which contains all of it, this way by any means looks more user-friendly and easier to tweak if someone wants to try with some other pdf patterns files beside for debugging.


## 🧪 Testing

As it should be done, i tried writing tests as well.
Since the program isn't too big all of them fitted inside a single file.
Those can be found in the test folder or run via unittest library using the discovery method.


## 🚀 Execution

Users can try the program by parsing the pdf file as the example above:
    $python main.py -h [path_to_pdf_file]

If user's files has a different pattern from the one I'm providing  as a demo, most likely will need a review to make it fit since not all pdf's have the same structure.


## 💬 Notes

I'm still learning Python (about 4 months in when I made this), so the project might not be perfect.
Any feedback or suggestions are welcome — I'm trying to build and improve as I go!


## 📄 Example

You can test the script using the included `demo.pdf`.
Keep in mind this file isn't the original one so can look a bit off since i had to modify it for a demo.  
Running it should produce a formatted text file similar if not identical to the one in the 'year' as folder mentioned in the file.


### 🧾 Example Output

After running the parser on `demo.pdf`, the output looks like this:

```
'1  Tu  UO      Tonawanda Del-Ton Plaza Astoria Ditmars'
'2  We  C       Brooklyn Flatbush Ave  Brooklyn Flatbush Ave Queens Steinway St Bronx G.Concourse'
```
Single quotes indicate the end of each line and can be useful when there’s no data after the trash type
either to have a better grasp while debugging around spaces.