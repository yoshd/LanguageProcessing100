import knock41
from sentence import Sentence

if __name__ == "__main__":
    chunks_list = knock41.make_chunks_list("neko.txt.cabocha")

    for chunks in chunks_list:
        sentence = Sentence(chunks)

        lines = {}
        for pair in sentence.make_dependency_pairs():
            src = pair[0]
            dst = pair[1]

            dst_index = dst.dst

            particles = src.get_morphs_by_pos("助詞")
            verbs = dst.get_morphs_by_pos("動詞")

            if len(particles) != 0 and len(verbs) != 0:
                #動詞は最左のみ(問題参照)
                if dst_index not in lines.keys():
                    lines[dst_index] = verbs[0].base + "\t" + " ".join([particle.base for particle in particles])
                else:
                    lines[dst_index] += " " + " ".join([particle.base for particle in particles])

        with open("corpus.txt", "a") as f:
            for line in sorted(lines.items(), key=lambda x: x[0]):
                f.write(line[1] + "\n")