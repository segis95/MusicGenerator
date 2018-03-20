#link <- "http://www.jazclass.aust.com/1books/"
link <- "http://www.thejazzpage.de/"

library(rvest)
library(stringr)

#page <- html("http://www.jazclass.aust.com/1books/lib.htm")
page <- read_html("http://www.thejazzpage.de/midiinfo.html")

files <- page %>%
  html_nodes("a") %>%       # find all links
  html_attr("href") %>%     # get the url
  str_subset(c("\\.mid"))


for (file in files){
  Sys.sleep(0.1)
  l <- paste(link,file,sep = "")
  print(l)
  download(l, substr(file,regexpr('d',file) + 3 ,nchar(file)), mode = "wb")
}