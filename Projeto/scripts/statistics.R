# Setup
library(readr)
library(dplyr)
library(ggplot2)

billboard <- read_csv("songs_1970_2018.csv")
lyrics <- read_csv("lyrics.csv")
albuns <- read_csv("albums.csv")
# all_data <- read_csv("combined_data.csv")

# 1. Top 10 music of billboard based on number of weeks
stat1 <- billboard %>% arrange(desc(weeks)) %>% head(10)
write.csv(stat1, "stat1.csv")

# 2. Top 10 artists of billboard based on number of musics they have there
stat2 <- billboard %>% group_by(`artist name`) %>% summarise(nr = n()) %>% arrange(desc(nr)) %>% head(10)
write.csv(stat2, "stat2.csv")

# 3. Average size of lyrics
stat3 <- lyrics %>% summarise(avgLen=mean(nchar(lyrics))) 
write.csv(stat3, "stat3.csv")

# 4. Album with more and less musics in the billboard
stat4 <- inner_join(lyrics, albuns, by="album id") %>% group_by(`album name`) %>% summarise(nr = n()) %>% arrange(desc(nr)) %>% head(10)
write.csv(stat4, "stat4.csv")

stat5 <- inner_join(lyrics, albuns, by="album id") %>% group_by(`album name`) %>% summarise(nr = n()) %>% arrange(nr) %>% head(10)
write.csv(stat5, "stat5.csv")

# 5. Lyrics with the word love and hate

stat6 <- lyrics %>% filter(grepl("love", lyrics, ignore.case = TRUE, fixed = TRUE))
write.csv(stat6, "stat6.csv")

stat7 <- lyrics %>% filter(grepl("hate", lyrics, ignore.case = TRUE, fixed = TRUE)) 
write.csv(stat7, "stat7.csv")

# 6. Plot with the evolution of number of songs through the years
#billboard %>% mutate(year = substr(date, nchar(date)-1, nchar(date))) %>% group_by(year) %>% summarise(nr= n()) 


#temp <- billboard %>% mutate(year = substr(date, nchar(date)-1, nchar(date))) %>% group_by(year) %>% summarise(nr= n())

# I exported temp to file and sorted 

#ordered_data %>%  ggplot(aes(x=year, y=nr, group=1)) +  geom_line() + geom_point() + labs(title="Number of songs on the Billboard 100 through the years", x="Years", y="Number of songs")
