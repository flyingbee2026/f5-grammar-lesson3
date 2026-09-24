# Lesson 3 content data — Nominalisation (F5 Grammar), REVISED per Helen's notes. UK spelling.

HEADER_3 = "Grammar – Lesson 3: Nominalisation"
TOPIC_LINE = "Nominalisation"

PART1_TITLE = "Part 1: Proofreading quiz"
PART1_INTRO = ("Each sentence contains TWO errors: one in an inversion structure and one in a relative clause. "
               "Proofread the sentences.")

# (sentence, correction, fix-notes) — every item pairs ONE inversion error with ONE relative-clause error
QUIZ = [
    ("Not only social media connects people far apart, but it also spreads rumours which often goes unchecked.",
     "Not only does social media connect people far apart, but it also spreads rumours which often go unchecked.",
     "(Add do before the subject; goes → go — ‘which’ refers to rumours.)"),
    ("Rarely teenagers verify the truth of what they share online, which make them easy targets of scams.",
     "Rarely do teenagers verify the truth of what they share online, which makes them easy targets of scams.",
     "(Add do before the subject; make → makes — the clause refers to sharing without checking.)"),
    ("Only by setting clear screen-time rules parents can protect their children, who often spends hours gaming late into the night.",
     "Only by setting clear screen-time rules can parents protect their children, who often spend hours gaming late into the night.",
     "(Move can before parents — ‘Only by’ inverts subject and auxiliary; spends → spend — ‘who’ refers to children.)"),
    ("Never the school has considered banning phones in class, which distracts students from every lesson.",
     "Never has the school considered banning phones in class, which distract students from every lesson.",
     "(Move has before the school — ‘Never’ inverts; distracts → distract — ‘which’ refers to phones.)"),
    ("Seldom victims of online scams report the fraud to the police, which make it harder to catch the criminals.",
     "Seldom do victims of online scams report the fraud to the police, which makes it harder to catch the criminals.",
     "(Add do before the subject; make → makes — the clause refers to the whole failure to report.)"),
]

TEACHER_ANSWERS_LABEL = "Teacher’s answers"

PART2_TITLE = "Part 2: Nominalisation in formal writing"
PART2_INTRO = ("Nominalisation names an action or a quality as a noun, so that ‘people use phones’ becomes "
               "‘the use of phones’. Naming ideas in this way packs a sentence into fewer words and gives formal "
               "writing a more academic tone. It is one of the clearest signs of a higher band in DSE Paper 2.")
CONV_LEAD = "Study how each plain sentence is converted. The new version names the action or quality as a noun and sounds more mature, yet the meaning stays the same."
# (plain, formal) pairs — formal version restates the SAME facts, only the construction changes
CONVERSIONS = [
    ("People use their phones all the time, and many young people cannot sleep well.",
     "The constant use of phones affects many young people’s sleep."),
    ("The company will improve its online security system, so customers will feel safer.",
     "The improvement of the company’s online security system will make customers feel safer."),
    ("Young people depend on their phones too much, and their schoolwork suffers.",
     "Young people’s heavy dependence on their phones affects their schoolwork."),
    ("Students who share photos online should be aware of online privacy.",
     "Students who share photos online should show awareness of online privacy."),
    ("The government decided to regulate social media companies, and the public supported this.",
     "The government’s decision to regulate social media companies won public support."),
    ("Tech companies should be responsible for users’ data, but many ignore this duty.",
     "Many tech companies ignore their responsibility for users’ data."),
    ("Because people share news very quickly, rumours spread fast.",
     "The rapid sharing of news makes rumours spread quickly."),
    ("Many people prefer reading news on social media to reading newspapers.",
     "Many people show a clear preference for social media news over newspapers."),
]
PARA_LEAD = "The short paragraphs below use the same idea. Notice how the nominalised phrases fit naturally into the sentences — nothing is forced."
# 3 short paragraphs: proposal / argumentative / cause-and-effect on communication & technology
EXAMPLE_PARAS = [
    "The introduction of a school digital-literacy programme deserves serious consideration. It would give students the skills to manage their screen time and to judge online information for themselves, reducing the risk of cyberbullying and online scams. Parents and teachers alike would welcome such a step.",
    "The importance of digital skills in the modern workplace can hardly be overstated. Students who master online tools at school gain a clear advantage when they graduate, while those who ignore them risk falling further behind. Schools, therefore, should treat digital literacy as a core subject rather than an option.",
    "Owing to the widespread use of smartphones, many students struggle to concentrate for long periods. Revision tasks that once took half an hour now stretch over a whole evening, interrupted by notifications arriving every few minutes. Setting clear screen-time limits at home would benefit both study and sleep.",
]

PART3_TITLE = "Part 3: Practice sets"
PART3_INTRO = ("First, warm up by turning words into nouns. Then rewrite each simple sentence using "
               "nominalisation. The sentences are about technology and communication, so keep the register "
               "formal. The last three sets (4, 5 and 6) are more challenging.")
WARMUP_TITLE = "Warm-up: From words to nouns"
WARMUP_INTRO = "Write the noun form of each word."
WARMUP_WORDS = ["decide", "introduce", "communicate", "regulate", "improve", "develop",
                "aware", "important", "depend", "responsible"]
WARMUP_ANSWERS = ["decision", "introduction", "communication", "regulation", "improvement", "development",
                  "awareness", "importance", "dependence", "responsibility"]

# Each set: title, simple sentence (plain, student-level), prompt, teacher answer (clearly better — level 3)
SETS = [
    ("Example Set 1 (Turn verbs into nouns)",
     "People use social media all the time, so they cannot concentrate on their studies.",
     "Turn the verb ‘use’ into a noun: begin with ‘Students’ constant use of ...’.",
     "Students’ constant use of social media weakens their concentration."),
    ("Example Set 2 (Turn verbs into nouns)",
     "The school decided to introduce a new e-learning platform, and many students welcomed the idea.",
     "Turn ‘decided to introduce’ into a noun phrase that opens the sentence.",
     "The school’s decision to introduce a new e-learning platform was welcomed by many students."),
    ("Example Set 3 (Turn adjectives into nouns)",
     "Parents worry that young people are too dependent on their smartphones.",
     "Turn ‘dependent’ into a noun: begin with ‘Many parents worry about young people’s ...’.",
     "Many parents worry about young people’s strong dependence on their smartphones."),
    ("Example Set 4 (Turn adjectives into nouns)",
     "Students are much more aware of online privacy than they were ten years ago.",
     "Turn ‘aware’ into a noun and rewrite the sentence without the verb ‘are’.",
     "Students’ awareness of online privacy has grown sharply over the past decade."),
    ("Example Set 5 (Turn because / if clauses into noun phrases)",
     "Because technology is developing very quickly, schools have to keep updating their computers and software.",
     "Replace the whole ‘Because ...’ clause with a phrase beginning ‘Owing to the rapid ...’.",
     "Owing to the rapid development of technology, schools must update their computers and software constantly."),
    ("Example Set 6 (Turn because / if clauses into noun phrases)",
     "If the government does not control social media companies more strictly, online scams will just keep growing.",
     "Replace the ‘If ...’ clause with a noun phrase beginning with ‘Without ...’.",
     "Without stricter regulation of social media companies, online scams will continue to grow."),
]

PART4_TITLE = "Part 4: Writing Task"
INSTR_LABEL = "Instructions:"
INSTR_1 = ("1. Your school magazine is running a series called ‘Life in the Digital Age’. Write ONE paragraph "
           "(about 80 words) explaining why online scams have become a common problem for young people, and "
           "suggesting ONE thing schools could do to protect them.")
INSTR_2 = "2. Use TWO noun phrases formed by nominalisation and ONE relative clause."

# label, text — each ~78-83 words, ≥2 nominalisations + exactly 1 relative clause, natural flow
SAMPLES = [
    ("Sample answer 1 (Verbs → nouns) ",
     "Online scams have become a common problem because many young people trust official-looking messages "
     "without a second thought. The spread of fake websites and phishing links is hard to stop, and it catches "
     "even careful users by surprise. Schools, in my view, should teach students the importance of checking every "
     "message before clicking, which is a vital skill in the digital world. A short course on online safety could "
     "easily be added to existing computer lessons, and it would reach every student equally."),
    ("Sample answer 2 (Adjectives → nouns) ",
     "Young people’s awareness of online scams is often low, and their trust in strangers’ messages can be far "
     "too high. The seriousness of the problem becomes clear only after money or personal data has been stolen, "
     "which is usually far too late. Schools should therefore run regular lessons on spotting scams, treating it "
     "as a basic life skill rather than an optional topic. Knowing how to pause and double-check before paying is "
     "the strongest protection available to any student."),
    ("Sample answer 3 (Because / if → nouns) ",
     "Owing to the constant flow of scam messages on social media, young people are targeted almost daily. The "
     "ease of creating fake websites, together with the difficulty of telling them from real ones, explains why "
     "so many victims never notice until it is too late. The responsibility for protection must be shared, which "
     "means schools, platforms and parents all have a part to play. Parents can talk openly about scams at home, "
     "while teachers can make online safety a regular lesson topic."),
]

UNDERSCORE_LINE = "_" * 85