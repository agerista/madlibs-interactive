from random import choice


def madlibs_scripts():
    """Picks a random madlibs script"""

    scripts = {
        "Letter from Camp":
        "Dear RELATIVE, \nI am having a(n) ADJECTIVE time at camp. The counselor is ADJECTIVE and the\
        food is ADJECTIVE. I met PERSON-IN-ROOM and we became ADJECTIVE friends. Unfortunately, (s)he is ADJECTIVE\
        and I VERB(ED) my BODY-PART so we couldn't go VERB(ING) like everyone else. I need more NOUN and a\
        NOUN sharpener, so please ADVERB VERB more when you VERB back. \nYour RELATIVE, \nPERSON-IN-ROOM",

        "Love Letter":
        "Dear TERM-OF-ENDEARMENT,\nWhen I VERB you for the first time, I couldn't ever have VERB(ED) that your\
        almost ADJECTIVE face, which holds a(n) ADJECTIVE and ADJECTIVE smile, was going to VERB me the way\
        it did. It has been a long time, do you remember? However, this ADJECTIVE ADJECTIVE that I VERB for you,\
        and which I dare call love is something very ADJECTIVE and ADJECTIVE. It is renewed every UNIT-OF-TIME\
        as if you could VERB me at every blink of a(n) BODY-PART. I know that I really love you simply because\
        I don't feel EMOTION and don't even get VERB(ED) from our ADJECTIVE relationship. It is in the BODY-FLUID\
        of your kisses and in the exchange of the BODY-FLUID from our bodies that I find the PERSONALITY-TRAIT,\
        the courage needed to confront this world which is full of NOUN and NOUN. It is in the ADJECTIVE tone of\
        your voice, in the suggested rainbow that is formed from the light of the sun hitting the ADJECTIVE of\
        your BODY-PART, or merely in the ADJECTIVE touch of your BODY-PART where I rest my BODY-PART and travel through\
        an ideal space, a space where everything is ADJECTIVE, where everything is ADJECTIVE and ADJECTIVE. A space\
        where everything is love, it is in this route that I travel and it is on you that I VERB, at last.\
        \nA kiss from your\nTERM-OF-ENDEARMENT",

        "Advice":
        "Driving a car can be fun if you follow this ADJECTIVE advice: When approaching a NOUN on the right,\
        always blow your NOUN. Before making a(n) ADJECTIVE turn, always stick your NOUN out of the window.\
        Every 2000 miles, have your NOUN inspected and your NOUN checked. When approaching a school, watch\
        out for ADJECTIVE PLURAL-NOUN. Above all, drive ADVERB The NOUN you save may be your own!"
        }

    madlib = choice(scripts.items())
    return madlib


def get_input_fields(madlib):
    """Get input fields out of script"""

    inputs = {}
    corp = madlib[1]
    corpus = corp.strip().replace(".", "").replace(",", "").split()

    for word in corpus:

        if word == "I" or word == "A":
            continue

        elif word.isupper():

            if inputs.get(word, 0) == 0:
                inputs[word] = 1

            else:
                inputs[word] += 1

    return inputs
