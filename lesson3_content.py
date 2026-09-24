# Lesson 3 content data — Nominalisation (F5 Grammar). UK spelling throughout.

HEADER_3 = "Grammar – Lesson 3: Nominalisation"
TOPIC_LINE = "Nominalisation"

PART1_TITLE = "Part 1: Proofreading quiz"
PART1_INTRO = "Each sentence contains TWO errors. Proofread the sentences."

# (sentence, correction, fix-notes)
QUIZ = [
    ("The students which share their notes online usually performs well in group projects.",
     "The students who share their notes online usually perform well in group projects.",
     "(which → who — people; performs → perform.)"),
    ("There are dozens of study apps, all of them is designed to keep users engaged.",
     "There are dozens of study apps, all of which are designed to keep users engaged.",
     "(them → which; is → are.)"),
    ("Many employees check work messages at night, that disturb their sleep.",
     "Many employees check work messages at night, which disturbs their sleep.",
     "(that → which — connective clause; disturb → disturbs — the clause refers to the whole activity of checking messages.)"),
    ("Not only video games provide entertainment, but they also helps players develop problem-solving skills.",
     "Not only do video games provide entertainment, but they also help players develop problem-solving skills.",
     "(Add do before the subject; helps → help.)"),
    ("Rarely teenagers question the accuracy of online news, which make them easy to fool.",
     "Rarely do teenagers question the accuracy of online news, which makes them easy to fool.",
     "(Add do before the subject; make → makes.)"),
    ("The increasing of online scams have made people more cautious about sharing their data.",
     "The increase in online scams has made people more cautious about sharing their data.",
     "(increasing → increase; of → in; have → has — a noun phrase takes a singular verb.)"),
]

TEACHER_ANSWERS_LABEL = "Teacher’s answers"

PART2_TITLE = "Part 2: Three patterns for formal writing"
PART2_INTRO = ("The three patterns in this part all turn actions or qualities into noun phrases — "
               "a technique called nominalisation. Nominalisation packs ideas into fewer words, "
               "and it can lift a formal paragraph towards a higher band.")

# Each pattern: title, (Structure, Use, Example), paragraph (3 sentences, bordered box)
PATTERNS = [
    {
        "title": "Pattern 1: Turn verbs into nouns",
        "rows": [
            ("Structure:", "verb → noun: use → the use of ...; decide → the decision to ...; improve → the improvement of ..."),
            ("Use in formal writing:", "Compresses an action into a noun phrase, so one clause does the work of two. Ideal for opening sentences in proposals and reports."),
            ("Example:", "The school’s decision to introduce e-textbooks has won widespread support."),
        ],
        "paragraph": ("The introduction of a school digital-literacy programme deserves serious consideration. "
                      "It would give students the skills to manage their screen time and to judge online information for themselves, "
                      "reducing the risk of cyberbullying and online scams. Parents and teachers alike would welcome such a step."),
    },
    {
        "title": "Pattern 2: Turn adjectives into nouns",
        "rows": [
            ("Structure:", "adjective → noun: important → importance; aware → awareness; dependent → dependence; responsible → responsibility"),
            ("Use in formal writing:", "Turns a quality into something we can discuss and judge. Excellent for topic sentences in argumentative essays."),
            ("Example:", "Young people’s heavy dependence on smartphones is a growing concern."),
        ],
        "paragraph": ("The importance of digital skills in the modern workplace can hardly be overstated. "
                      "Students who master online tools at school gain a clear advantage when they graduate, "
                      "while those who ignore them risk falling further behind. Schools, therefore, should treat digital literacy as a core subject rather than an option."),
    },
    {
        "title": "Pattern 3: Turn because / if clauses into noun phrases",
        "rows": [
            ("Structure:", "because + a clause → owing to / because of + a noun phrase; if + a clause → without + a noun phrase"),
            ("Use in formal writing:", "Shortens explanations and states a cause or condition in one breath. Ideal for proposals and conclusions."),
            ("Example:", "Owing to the widespread use of smartphones, many students struggle to concentrate for long periods."),
        ],
        "paragraph": ("Owing to the rise of artificial intelligence, teachers can no longer be sure that homework is entirely a student’s own work. "
                      "The ease with which students can copy machine-written answers, together with the difficulty of detecting it, "
                      "forces schools to rethink assessment entirely. The wisest response is not to ban the tools but to teach their responsible use."),
    },
]

ADDITIONAL_TITLE = "Additional pattern (teacher’s note — optional)"
ADDITIONAL_INTRO = ("Introduce this only after the class is secure with the three core patterns. "
                    "Nominalisation should tighten a sentence, not bury it. If the noun phrases pile up and the "
                    "‘of’ sounds multiply, the plain version is usually clearer.")
ADDITIONAL_H4 = "Caution: avoid ‘noun soup’"
ADDITIONAL_ROWS = [
    ("Plain:", "Because students spend hours online, they perform badly in class the next day."),
    ("Over-nominalised:", "Owing to the excessive duration of students’ online activity, the standard of their classroom performance is adversely affected."),
    ("The lesson:", "The plain version wins. Use nominalisation to clarify, never to decorate."),
]
ADDITIONAL_EXT = ("For stronger classes: nominalisation also suits formal reports and minutes — "
                  "‘The committee agreed to ban phones in class’ becomes ‘The committee approved the ban on phones in class.’")

PART3_TITLE = "Part 3: Practice sets"
PART3_INTRO = ("Rewrite each simple sentence using nominalisation. The sentences are all about technology and communication, "
               "so keep the register formal. The even-numbered sets (2, 4 and 6) are more challenging.")

# Each set: title, simple sentence, prompt, teacher answer
SETS = [
    ("Example Set 1 (Turn verbs into nouns)",
     "People use social media so often that it weakens their face-to-face communication.",
     "Turn ‘use’ into a noun and begin with ‘The frequent use of ...’.",
     "The frequent use of social media weakens people’s face-to-face communication."),
    ("Example Set 2 (Turn verbs into nouns)",
     "The government will improve the security of online banking, which will protect customers.",
     "Turn ‘will improve’ into a noun and begin with ‘The improvement of ...’.",
     "The improvement of online banking security will protect customers."),
    ("Example Set 3 (Turn adjectives into nouns)",
     "Many parents worry about how dependent young people are on their smartphones.",
     "Turn ‘dependent’ into a noun: rewrite ‘how dependent young people are’ as ‘young people’s strong dependence ...’.",
     "Many parents worry about young people’s strong dependence on their smartphones."),
    ("Example Set 4 (Turn adjectives into nouns)",
     "Students are more aware of online privacy than they used to be.",
     "Turn ‘aware’ into a noun and rewrite the sentence without the verb ‘are’.",
     "Students’ awareness of online privacy has grown in recent years."),
    ("Example Set 5 (Turn because / if clauses into noun phrases)",
     "Because technology develops quickly, schools must update their resources regularly.",
     "Replace the ‘because’ clause with a phrase beginning ‘Owing to the rapid development of ...’.",
     "Owing to the rapid development of technology, schools must update their resources regularly."),
    ("Example Set 6 (Turn because / if clauses into noun phrases)",
     "If the government does not regulate social media companies, online scams will continue to grow.",
     "Replace the conditional clause with a noun phrase beginning with ‘Without ...’.",
     "Without stricter regulation of social media companies, online scams will continue to grow."),
]

PART4_TITLE = "Part 4: Writing Task"
INSTR_LABEL = "Instructions:"
INSTR_1 = ("1. Your school magazine is running a series called ‘Life in the Digital Age’. Write ONE paragraph "
           "(about 80 words) giving your opinion on whether students should be allowed to use AI tools such as "
           "ChatGPT to help with their schoolwork.")
INSTR_2 = "2. Use TWO noun phrases formed by nominalisation and ONE relative clause."

# label, text — each ~75-85 words, exactly ≥2 nominalisations + exactly 1 relative clause
SAMPLES = [
    ("Sample answer 1 (Verbs → nouns) ",
     "Teachers often blame AI tools for helping students cheat, yet the same tools can support genuine learning. "
     "The introduction of clear school guidelines, together with the use of AI for brainstorming rather than for "
     "writing essays, would keep homework honest while saving time. A simple ban, which students would quickly find "
     "ways around, is unlikely to work, and it may simply drive the practice underground. With clear guidelines in "
     "place, however, AI could become a helpful tutor rather than a hidden ghost-writer."),
    ("Sample answer 2 (Adjectives → nouns) ",
     "Students’ dependence on AI worries many teachers, but the importance of honest effort is just as clear. "
     "A chatbot writing a whole essay teaches nothing, while one explaining a difficult idea can speed up real "
     "learning. The wisest approach, to my mind, is to allow AI with clear limits, which keeps the student’s "
     "responsibility at the centre of every assignment. Chatting with a well-designed tutor bot can also build "
     "confidence, provided the final answer is always the student’s own work."),
    ("Sample answer 3 (Because / if → nouns) ",
     "Owing to the rapid development of artificial intelligence, homework can no longer be treated as proof of a "
     "student’s own thinking. The ease of copying from a chatbot, together with the difficulty of detecting it, has "
     "forced schools to reconsider their assignments. The answer is not to ban the tools but to teach their "
     "responsible use, which will prepare students for a working world full of AI. Adapting assignments to AI’s "
     "strengths and weaknesses is the challenge now facing every school."),
]

UNDERSCORE_LINE = "_" * 85