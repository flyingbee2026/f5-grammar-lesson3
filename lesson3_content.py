# Lesson 3 content data — Nominalisation (F5 Grammar), v4 per Helen's notes. UK spelling.

HEADER_3 = "Grammar – Lesson 3: Nominalisation"
TOPIC_LINE = "Nominalisation"

PART1_TITLE = "Part 1: Proofreading quiz"
PART1_INTRO = ("Each sentence contains TWO errors: one in an inversion structure and one in a relative clause. "
               "Proofread the sentences.")

# (sentence, correction, fix-notes) — every item pairs ONE inversion error with ONE relative-clause error
QUIZ = [
    ("Not only online learning saves travelling time, but it also gives students access to courses which is not available in their own schools.",
     "Not only does online learning save travelling time, but it also gives students access to courses which are not available in their own schools.",
     "(Add do before the subject; is → are — ‘which’ refers to courses.)"),
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

WARMUP_TITLE = "Warm-up: From words to nouns"
WARMUP_INTRO = "Write the noun form of each word. The last six words are more challenging."
WARMUP_WORDS = ["decide", "improve", "communicate", "introduce", "regulate", "protect", "explain",
                "solve", "use", "develop", "aware", "important", "depend", "responsible",
                "choose", "know", "lose", "prove", "believe", "strong"]
WARMUP_ANSWERS = ["decision", "improvement", "communication", "introduction", "regulation", "protection",
                  "explanation", "solution", "use", "development", "awareness", "importance",
                  "dependence", "responsibility", "choice", "knowledge", "loss", "proof",
                  "belief", "strength"]

PART2_TITLE = "Part 2: Nominalisation in formal writing"
PART2_INTRO = ("Nominalisation names an action or a quality as a noun, so that ‘people use phones’ becomes "
               "‘the use of phones’. It packs ideas into fewer words and gives formal writing a more academic "
               "tone, and it is one of the clearest signs of a higher band in DSE Paper 2.")

# 4 examples, each: title, plain (wordy student sentence), formal (same facts, nominalised), short paragraph
# that opens with the formal sentence and flows naturally. Plain/formal pairs carry NO new information.
EXAMPLES = [
    {
        "title": "Example 1: Verb → noun",
        "plain": "The school decided to introduce e-books, and students supported this.",
        "formal": "The school’s decision to introduce e-books won students’ support.",
        "paragraph": ("The school’s decision to introduce e-books won students’ support. The introduction of the "
                      "new system also saved paper and lightened schoolbags, and teachers soon noticed a rise in "
                      "reading time. Other schools could follow this example with little extra cost."),
    },
    {
        "title": "Example 2: Adjective → noun",
        "plain": "Students should be aware of online scams.",
        "formal": "Students should show awareness of online scams.",
        "paragraph": ("Students should show awareness of online scams. The danger is real and growing, yet many "
                      "victims discover the fraud only after money has already been lost, which means the damage "
                      "is done. A short lesson on spotting false messages would build this awareness early."),
    },
    {
        "title": "Example 3: Because-clause → noun phrase",
        "plain": "Because people share news very quickly, rumours spread fast.",
        "formal": "Owing to the rapid sharing of news, rumours spread quickly.",
        "paragraph": ("Owing to the rapid sharing of news, rumours spread quickly. A false story can reach "
                      "thousands of people within minutes, and the difficulty of checking every update means "
                      "that some readers forward it before anyone notices. Careful readers, therefore, pause "
                      "and verify before sharing anything."),
    },
    {
        "title": "Example 4: If-clause → noun phrase",
        "plain": "If the school does not update its computers, online lessons will fail.",
        "formal": "Without updated computers, online lessons will fail.",
        "paragraph": ("Without updated computers, online lessons will fail. The school’s plan to renew its "
                      "equipment, however, has already won support from the Parent-Teacher Association, and "
                      "teachers have promised to test the new system before the start of term."),
    },
]

PART3_TITLE = "Part 3: Practice sets"
PART3_INTRO = ("Rewrite each simple sentence using nominalisation. The sentences are about technology and "
               "communication, so keep the register formal. The last three sets (4, 5 and 6) are more "
               "challenging.")

# Each set: title, simple sentence (plain, student-level), prompt, teacher answer (clearly better — level 3)
# Sets 1-3 mirror the four Example moves with DIFFERENT target nouns; sets 4-6 are harder.
SETS = [
    ("Example Set 1 (Verb → noun)",
     "People use social media all the time, so they cannot concentrate on their studies.",
     "Turn the verb ‘use’ into a noun: begin with ‘Students’ constant use of ...’.",
     "Students’ constant use of social media weakens their concentration."),
    ("Example Set 2 (Adjective → noun)",
     "Parents worry that young people are too dependent on their smartphones.",
     "Turn ‘dependent’ into a noun: begin with ‘Many parents worry about young people’s ...’.",
     "Many parents worry about young people’s strong dependence on their smartphones."),
    ("Example Set 3 (Because-clause → noun phrase)",
     "Because online games are so attractive, many teenagers neglect their homework.",
     "Replace the ‘Because ...’ clause with a phrase beginning ‘Owing to the ...’.",
     "Owing to the strong appeal of online games, many teenagers neglect their homework."),
    ("Example Set 4 (Verb → noun)",
     "The government will improve the security of online banking, which will protect customers.",
     "Turn ‘will improve’ into a noun and begin with ‘The improvement of ...’.",
     "The improvement of online banking security will protect customers."),
    ("Example Set 5 (Adjective → noun)",
     "Students are much more aware of online privacy than they were ten years ago.",
     "Turn ‘aware’ into a noun and rewrite the sentence without the verb ‘are’.",
     "Students’ awareness of online privacy has grown sharply over the past decade."),
    ("Example Set 6 (If-clause → noun phrase)",
     "If the government does not control social media companies more strictly, online scams will just keep growing.",
     "Replace the ‘If ...’ clause with a noun phrase beginning with ‘Without ...’.",
     "Without stricter regulation of social media companies, online scams will continue to grow."),
]

PART4_TITLE = "Part 4: Writing Task"
INSTR_LABEL = "Instructions:"
INSTR_1 = ("1. Your school magazine is running a series called ‘Life in the Digital Age’. Write ONE paragraph "
           "(about 80 words) explaining why online scams have become a common problem for young people, and "
           "suggesting ONE thing schools could do to protect them.")
INSTR_2 = ("2. Nominalise ONE of the words in the word bank below and use the noun in your paragraph. "
           "Also add ONE relative clause or ONE inverted pattern "
           "(e.g. Not only … but also …; Never …; Rarely …).")

# Word bank for the writing task: five verbs/adjectives; students turn ONE into a noun (round-6 note).
WORD_BANK_LABEL = "Word bank — turn ONE of these five into a noun, then use it in your paragraph:"
WORD_BANK = ["protect", "aware", "educate", "responsible", "believe"]
WORD_BANK_ANSWERS = ["protection", "awareness", "education", "responsibility", "belief"]
TEACHER_BANK_NOTE = ("Bank answers: protect → protection; aware → awareness; educate → education; "
                     "responsible → responsibility; believe → belief. Note how Sample answer 2 uses "
                     "‘awareness’ and Sample answer 3 uses ‘responsibility’.")

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