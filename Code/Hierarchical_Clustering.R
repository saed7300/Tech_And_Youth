library(tm)
library(philentropy)

corpus_link<- 'C:\\Users\\sneaz\\Documents\\Text Mining\\Data\\Corpus\\All'
corpus <- Corpus(DirSource(corpus_link))
(getTransformations()) ## These work with library tm
(ndocs<-length(corpus))

corpus <- tm_map(corpus, removeWords, stopwords("english"))

corpus_doc <- DocumentTermMatrix(corpus,
                                      control = list(
                                        #stopwords = TRUE, ## remove normal stopwords
                                        #wordLengths=c(3, 14), ## get rid of words of len 2 or smaller or larger than 15
                                        #removePunctuation = TRUE,
                                        #removeNumbers = TRUE,
                                        #tolower=TRUE,
                                        #stemming = TRUE,
                                      ))

inspect(corpus_doc)

corpus_term <- TermDocumentMatrix(corpus,
                                          # control = list(
                                          #   stopwords = TRUE, ## remove normal stopwords
                                          #   wordLengths=c(3, 10), ## get rid of words of len 2 or smaller or larger than 15
                                          #   removePunctuation = TRUE,
                                          #   removeNumbers = TRUE,
                                          #   tolower=TRUE,
                                          #   stemming = TRUE,
                                          )

inspect(SmallCorpus_TERM_DM)

corpus_doc_df <- as.data.frame(as.matrix(corpus_doc))


library(dplyr)
library(tidyr)

corpus_doc_df<-corpus_doc_df %>% drop_na()

df <-corpus_doc_df %>% 
  gather(key,value) %>% 
  group_by(key) %>% 
  summarise(Sum=sum(value)) %>% 
  arrange(desc(Sum)) %>% 
  top_n(20,Sum)
top_words = as.list(df$key)


corpus_term_df <- as.data.frame(as.matrix(corpus_term))


corpus_term_df <- cbind(newColName = rownames(corpus_term_df), corpus_term_df)
corpus_term_df_sub <- corpus_term_df[corpus_term_df$newColName %in% top_words,]
corpus_term_df_sub <- corpus_term_df_sub%>%
  select(-c(newColName))


(dist_corpus <- distance(corpus_term_df_sub, method="cosine",use.row.names = TRUE))
dist_corpus<- as.dist(dist_corpus)
hclust_cosine<- hclust(dist_corpus, method="ward.D")
plot(hclust_cosine, cex=.7, hang=-1,main = "Cosine Sim")
rect.hclust(hclust_cosine, k=4)



(dist_corpus2<- dist(corpus_term_df_sub, method = "minkowski", p=2)) #Euclidean
(hclust_cosine_euc <- hclust(dist_corpus2, method = "ward.D" ))
plot(hclust_cosine_euc, cex=1, hang=-1, main = "Minkowski p=2 (Euclidean)")
rect.hclust(hclust_cosine_euc, k=4)







