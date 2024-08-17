# WikipediaEpisodeScraper
Scrapes the names of all episodes of a TV series from a wikipedia page and outputs them to a text file

Run the python file, scrape_h2_h3_table.py can by compiled using:<br/>
python scrape_h2_h3_table.py<br/>
and input the desired URL of a Wikipedia article of and episode list of a TV series<br/>

It can also be compiled using the main.c file but it is not necessary. This is just a tool I included so I can ensure I can embed the python file in other C projects. <br/>
Run the main.c file using:<br/>
gcc -I/usr/include/python3.12 -lpython3.12 main.c -o mkvrenamer.out && ./mkvrenamer.out<br/>
or:<br/>
clang -I/usr/include/python3.12 -lpython3.12 main.c -o mkvrenamer.out && ./mkvrenamer.out<br/>
or:<br/>
zig cc -I/usr/include/python3.12 -lpython3.12 main.c -o mkvrenamer.out && ./mkvrenamer.out<br/>
NOTE: This is tested in Arch Linux, on Windows it is tested using WSL. <br/>
NOTE: Python 3.12 must be installed as it is what is used in the compile statements. It may work with a different version of python but the above statement must be changed from python 3.12 to 3.x (x being the given version)<br/>
