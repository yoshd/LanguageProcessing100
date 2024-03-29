import knock41
from sentence import Sentence

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        sentence = Sentence(chunks)
        for pair in sentence.make_dependency_pairs():
            src = pair[0]
            dst = pair[1]
            if "名詞" in src.get_included_pos() and "動詞" in dst.get_included_pos():
                print(src.get_phrase() + "\t" + dst.get_phrase())
