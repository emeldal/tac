
"""Filter out stopwords for word cloud"""

import sys
import nltk
try:
    from nltk.corpus import stopwords
except LookupError:
    nltk.download('stopwords')
    from nltk.corpus import stopwords

sw = stopwords.words("french")
sw += ["les", "plus", "cette", "fait", "faire", "être", "deux", "comme", "dont", "tout",
       "ils", "bien", "sans", "peut", "tous", "après", "ainsi", "donc", "cet", "sous",
       "celle", "entre", "encore", "toutes", "pendant", "moins", "dire", "cela", "non",
       "faut", "trois", "aussi", "dit", "avoir", "doit", "contre", "depuis", "autres",
       "van", "het", "autre", "jusqu", "vers", "quelque", "car", "quel", "abord", "parce", 
       "leurs", "chez", "aucun", "alors", "auquel", "tandis", "quand", "devons", "donne", 
       "telles", "toujours", "seulement", "pourra", "cependant", "plusieurs", "elles", 
       "déjà", "très", "lorsque", "trouve", "crois", "toute", "faite", "ans", "celles"
       "celui", "quelques", "laquelle", "faites", "tel", "etc", "devront", "chaque", "agit"
       "mettre", "ceux", "pourront", "avant", "prendre", "aucune", "peu", "fera", "également"
       "celles", "dessus", "devant", "beaucoup"]
sw = set(sw)


def filtering(dpath, year):
    path = f"{dpath}/{year}.txt"
    output = open(f"{dpath}/{year}_keywords.txt", "w", encoding='utf-8')

    with open(path, encoding='utf-8') as f:

        text = f.read()
        words = nltk.wordpunct_tokenize(text)
        kept = [w.lower() for w in words if len(
            w) > 2 and w.isalpha() and w.lower() not in sw]
        kept_string = " ".join(kept)
        output.write(kept_string)
    return f'Output has been written in {output_path}!'


if __name__ == '__main__':
    data_path = sys.argv[1]
    chosen_year = sys.argv[2]

    filtering(data_path, chosen_year)

