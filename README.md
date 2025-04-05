# [The Kya: Dark Lineages Files website](https://kyadlfiles.github.io)

## Structure of the repository
**/externals** contains submodules 

**/static** contains everything that need to be copied at the root of the website as is (styles, scripts, images etc.).  Copying these files is done by build.py  

**/templates** contains the actual webpages  
- **/templates/_partials/** contains HTML templates that are used to wrap the content of the documents
- Other folders contain Markdown (with custom extensions) documents with the actual text content. The content of the /template folder is copied to the root of the website, with every !index.md being converted and wrapped in an HTML template as index.html 

Every page must be created as a new folder with an !index.md file inside. Apart from subfolders, the !index.md file must be the only content of every folder.

Every !index.md must contain two lines of metadata at the very top
 - **title**, which will be used as the <title> in the HTML, as the title in the header, and will appear in the navigation links at the top of the page
 - **template**, which indicates which file in */templates/_partials* the document will be wrapped in
 
When the build script is run, it will output to **/_site** (which is in .gitignore)
 
## Important 
This website is made possible by the awesome community we built and the efforts of individuals who love to thinker with and study how Kya: DL works  
The content on this website is distributed under the [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0) license](https://creativecommons.org/licenses/by-nc-sa/4.0/)
