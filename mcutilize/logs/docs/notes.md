### SETUP ####

- to set this up correctly you need to think of some of the keys being unpacked into a function as parameters
- need to set a formatters key like bleow which can be used by handles (essentially what the message may look like)
- handles are the classes and functionality used to lg away
    - below there are tow one called console which is set up to output to the console and one called file to output along with the class
        - logging.StreamHandlers is for in/out streams and logging.FileHandler is for files
    - extra args those classes may take should simply be created as key/value pairs (e.g. filename: log.log)
- loggers is the seciont where you tie all the above together
    - for eample you ahve a logger called root which has thehandlers console and is set to the level of DEBUG
        - the level set here will override the levels eset in the handlers, so if you have debug set in the handelrs 
        but you have error set in to the logger you will only see error logs
    - you can have multiple handlers to do mulitple things like the version_parser handler
- to use a certain logger you will want to first set the config of the logger like below under __main__ and useing 
getLOgger() choose the logger (e.g. either root or file or whatever you may have in the loggers key) 

- levels will show different things in a hierarchic way:
    -   NOTSET will show all
    -   DEBUG will show debug and below
    -   INFO will show info and below (so not debuck, this pattern will hold tru)
    -   WARNING only shows warning and below
    -   ERROR is for error and below
    -   CRITICAL is for critical only 
    
- sources: 
    - https://stackoverflow.com/questions/7507825/where-is-a-complete-example-of-logging-config-dictconfig
    - https://docs.python.org/3/hoto/loggin.html