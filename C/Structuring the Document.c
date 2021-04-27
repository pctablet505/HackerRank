
char *copyWord(char *text, int *i) {
    char *word = calloc(1, sizeof(char));
    int len = 1, index = 0;
    while ((text[*i] != '\0') && (text[*i] != '\n') && (text[*i] != '.') && (text[*i] != ' ')) {
        word = realloc(word, ++len);
        word[index] = text[*i];
        *i = *i + 1;
        index++;
    }

    return word;
}

struct document get_document(char *text) {

    struct document doc = {};
    int wordCnt = 0, parCnt = 0, senCnt = 0;
    struct paragraph par = {};
    struct sentence sen = {};
    struct word word = {};
    int i = 0;

    while (text[i] != '\0') {
        char *tmp = copyWord(text, &i);
        wordCnt++;
        word.data = tmp;
        sen.data = realloc(sen.data, wordCnt * sizeof(struct word));
        sen.word_count = wordCnt;
        word.data = tmp;
        memcpy(&(sen.data[wordCnt - 1]), &word, sizeof(struct word));

        if (text[i] == ' ') {
            i++;
        }

        if (text[i] == '.') {
            i++;
            senCnt++;
            par.data = realloc(par.data, senCnt * sizeof(struct sentence));
            par.sentence_count = senCnt;
            memcpy(&(par.data[senCnt - 1]), &sen, sizeof(struct sentence));
            wordCnt = 0;
            sen.data = NULL;
            sen.word_count = 0;
        }

        if (text[i] == '\n') {
            i++;
            parCnt++;
            doc.data = realloc(doc.data, parCnt * sizeof(struct paragraph));
            doc.paragraph_count = parCnt;
            memcpy(&(doc.data[parCnt - 1]), &par, sizeof(struct paragraph));
            senCnt = 0;
            sen.data = NULL;
            sen.word_count = 0;
            par.data = NULL;
            par.sentence_count = 0;
            wordCnt = 0;
        }

    }

    parCnt++;
    doc.data = realloc(doc.data, parCnt * sizeof(struct paragraph));
    doc.paragraph_count = parCnt;
    memcpy(&(doc.data[parCnt - 1]), &par, sizeof(struct paragraph));

    return doc;
}


struct word kth_word_in_mth_sentence_of_nth_paragraph(struct document Doc, int k, int m, int n) {
    return Doc.data[n - 1].data[m - 1].data[k - 1];
}

struct sentence kth_sentence_in_mth_paragraph(struct document Doc, int k, int m) {
    return Doc.data[m - 1].data[k - 1];
}

struct paragraph kth_paragraph(struct document Doc, int k) {
    return Doc.data[k - 1];
}

