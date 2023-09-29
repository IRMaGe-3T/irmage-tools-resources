
# MkDocs quick tutorial
[MkDocs](https://www.mkdocs.org/) can be used to [documenting your project](https://www.mkdocs.org/getting-started/).
 
MkDocs uses the Markdown language by default. 

### Install MkDocs
```
pip3 install mkdocs
```

### Setup your MkDocs project:
```
cd myprojetcs/
mkdocs new .
```

This commandes create a Mkdocs configuration file (`mkdocs.yml`) and a mindex markdown file (`docs/index.md`).

# Writing yours docs

You can add [Markdowns](https://daringfireball.net/projects/markdown/) files (.md) in the docs folder and [configure page and navigation](https://www.mkdocs.org/user-guide/writing-your-docs/).

All the pages should be added to the `index.md` file and the `nav` (navigation) part of `mkdocs.yml` file should be updated. 

`index.md` file example:
```
# Welcome to your project !

Hello !

## Project layout
    mkdocs.yml
    docs/
        index.md
        users/
            BIDS.md
        developers/
            doc-mkdocs.md
```

`mkdocs.yml` file example: 
```
site_name:Test project
site_url: https://example.com
nav:
    - Home: index.md
    - Users documentation:
      - BIDS: users/BIDS.md
    - Tips for developers:
      - Documentation - MKDocs : developers/doc-mkdocs.md 
theme: readthedocs
```


### Build your project on a development server
```
mkdocs serve
```

It builds all your Markdown files into HTML and create a development server. 
Open up http://127.0.0.1:8000/ in your web browser to see your documentation. 
If your are changing your Markdown files, the dics will be automatically rebuild in your development server.
