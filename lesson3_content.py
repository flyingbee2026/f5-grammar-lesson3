# Lesson 3 content data — Nominalisation (F5 Grammar), REVISED per Helen's notes. UK spelling.

HEADER_3 = "Grammar – Lesson 3: Nominalisation"
TOPIC_LINE = "Nominalisation"

PART1_TITLE = "Part 1: Proofreading quiz"
PART1_INTRO = ("Each sentence contains TWO errors: one in an inversion structure and one in a relative clause. "
               "Proofread the sentences.")

# (sentence, correction, fix-notes) — every item pairs ONE inversion error with ONE relative-clause error
QUIZ = [
    ("Not only social media connects people instantly, but it also spreads stories which is often false.",
     "Not only does social media connect people instantly, but it also spreads stories which are often false.",
     "(Add do before the subject; is → are — ‘which’ refers to stories.)"),
    ("Rarely teenagers check the sources of the news they read online, which make them easy to fool.",
     "Rarely do teenagers check the sources of the news they read online, which makes them easy to fool.",
     "(Add do before the subject; make → makes — the clause refers to the whole activity of checking sources.)"),
    ("Only by setting clear screen-time rules parents can help their children, who often spends hours gaming.",
     "Only by setting clear screen-time rules can parents help their children, who often spend hours gaming.",
     "(Move can before parents — ‘Only by’ inverts subject and auxiliary; spends → spend — ‘who’ refers to children.)"),
    ("Never the school has considered banning phones in class, which is used by nearly every student.",
     "Never has the school considered banning phones in class, which are used by nearly every student.",
     "(Move has before the school — ‘Never’ inverts; is → are — ‘which’ refers to phones.)"),
    ("Seldom students will question the news which they read it on social media.",
     "Seldom will students question the news which they read on social media.",
     "(Move will before students — ‘Seldom’ inverts; delete it — ‘which they read’ is complete without a second object.)"),
]

TEACHER_ANSWERS_LABEL = "Teacher’s answers"

PART2_TITLE = "Part 2: Nominalisation in formal writing"
PART2_INTRO = ("Nominalisation names an action or a quality as a noun, so that ‘people use phones’ becomes "
               "‘the use of phones’. Naming ideas in this way packs a sentence into fewer words and gives formal "
               "writing a more academic tone. It is one of the clearest signs of a higher band in DSE Paper 2.")
CONV_LEAD = "Study how each plain sentence is converted. The new version names the action or quality as a noun and sounds more mature, yet the meaning stays the same."
# (plain, formal) pairs — explanation of the move, no structure/function notes
CONVERSIONS = [
    ("People use their phones all day long.",
     "The widespread use of smartphones worries teachers and parents."),
    ("The company will improve its online security system.",
     "The improvement of the company’s online security system will begin next month."),
    ("Young people depend on their phones too much.",
     "Young people’s heavy dependence on their phones shows no sign of weakening."),
    ("Students should be aware of online privacy.",
     "Awareness of online privacy is now taught in many schools."),
    ("The government decided to control social media companies more strictly.",
     "The government’s decision to regulate social media companies has won public support."),
    ("Tech companies should be responsible for users’ data.",
     "Tech companies must accept responsibility for users’ data."),
    ("Because people share news very quickly, rumours spread fast.",
     "The rapid sharing of news allows rumours to spread quickly."),
    ("Many people prefer reading news on social media to reading newspapers.",
     "Young people’s preference for social media news over newspapers has reshaped the whole news industry."),
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
     "Turn the verb ‘use’ into a noun and begin with ‘The constant use of ...’.",
     "The constant use of social media makes it hard for students to concentrate."),
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
           "(about 80 words) giving your opinion on whether young people today are able to tell real news from "
           "fake news, and suggesting ONE thing schools could do to help them.")
INSTR_2 = "2. Use TWO noun phrases formed by nominalisation and ONE relative clause."

# label, text — each ~78-83 words, ≥2 nominalisations + exactly 1 relative clause, natural flow
SAMPLES = [
    ("Sample answer 1 (Verbs → nouns) ",
     "Some adults assume young people are internet experts, but the opposite is usually true. "
     "The spread of fake news on social media is alarmingly fast, and it tests the judgement of even careful "
     "readers. Schools, in my view, should teach students how to check the source of every story, which is a "
     "vital skill in the digital age. Such lessons take only minutes and can be built into normal English "
     "classes without extra cost or equipment."),
    ("Sample answer 2 (Adjectives → nouns) ",
     "Many teenagers rely on short videos for their news, and their awareness of bias is often weak. The "
     "importance of checking information before sharing it becomes clear only after a false story has spread, "
     "which usually means real harm has already been done. Schools should therefore run regular lessons on "
     "media literacy, treating it as a basic life skill rather than an optional topic. Knowing how to pause and "
     "check before sharing is the most useful survival habit in the digital world."),
    ("Sample answer 3 (Because / if → nouns) ",
     "Owing to the constant flow of posts and videos, young people rarely pause to consider whether a story is "
     "true. The ease of forwarding a shocking headline, together with the difficulty of checking it, explains "
     "why fake news spreads so quickly. The responsibility for stopping it must be shared, which means schools, "
     "platforms and parents all have a part to play. Parents, in particular, can show their children how to "
     "compare sources, while teachers can make fact-checking a normal classroom habit."),
]

UNDERSCORE_LINE = "_" * 85