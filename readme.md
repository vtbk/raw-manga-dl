# raw-manga-dl

Simple tool for downloading manga from websites of various publishers. Meant to be somewhat dynamic to make it easier to add in new services that share similar DRM techniques. Only meant for raw Japanese manga; there are plenty of solutions available on Github for scraping websites that aggregrate English scanlations. 

***Note:*** this is not particularly functional nor is this project organized, so I do not recommend using this. However, it works okay for **my** personal use case. I wouldn't be surprised if it broke if used for yours. I am mostly doing this for fun and as practice. 

## To-do
- Fix sloppy imports and structure project more neatly.. 
- Add more services (https://comic-walker.com, https://web-ace.jp, and so on.)
- Add proper rate limiting.
- Refactor after implementing more DRM solvers, abstract common traits.
- Fix usage of solver - too closely coupled to service implementations, so there's no real need to inject them (especially in a language such as Python)
- Fix argument usage
- Package project for easier distribution 

## Installation

### Clone the repository
```cmd
git clone https://github.com/vtbk/raw-manga-dl && cd raw-manga-dl

```

### Optional

Add raw-manga-dl.py to your PATH

**UNIX example**: 

```bash
chmod +x raw-manga-dl.py
ln -s raw-manga-dl.py /usr/local/bin/raw-manga-dl 
```

**Windows:**

Add the raw-manga-dl folder to your PATH environment variable. File associations seem to be iffy in Windows though; .py files associated with the Python interpreter won't have arguments passed when called directly (i.e. ```x.py``` instead of ```python x.py```). I personally don't know how to fix this.  

### Dependencies
Install the dependencies if missing
```bash
pip install pillow
pip install beautifulsoup4
```


## Usage
Functionality is incredibly limited right now. 

**Example usage**:
> python raw-manga-dl.py --download \<URL\> -o \<type\> \<path\>


**Explanation**:
>--download \<URL\> refers to the _chapter_ URL of the chapter to download
>
>\-o \<type\> specifies the output format. Either "zip" or "folder", defaults to the latter.
>
>\<path\> specifies the storage location; chapter is stored inside of the specified directory => \<path\>/\<chapter\>(.zip) 


