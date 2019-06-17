library(rvest)

url <- "https://us12.campaign-archive.com/home/?u=feb495b549c951a17eb2162c4&id=dc8f690140"

content <- read_html(url)

urls <- content %>% html_nodes("a") %>% html_attr("href")

urls <- text[startsWith(text,"http://eepurl")]

paste0("'",paste(urls, collapse = "','"),"'")
