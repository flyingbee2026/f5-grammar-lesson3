#!/usr/bin/env python3
"""Build Lesson 3 (Nominalisation) student + teacher docx from Helen's Lesson 2 teacher file as template."""
import sys
import copy
from docx import Document
from docx.oxml.ns import qn

import lesson3_content as C

W = qn('w:')

TPL = "/root/.hermes/cache/documents/doc_97195e5a7359_Lesson 2 - Inversion Part 1 (Teacher's).docx"
OUT_TEACHER = "/opt/f5-grammar-lesson3/out/Lesson 3 - Nominalisation (Teacher's).docx"
OUT_STUDENT = "/opt/f5-grammar-lesson3/out/Lesson 3 - Nominalisation (Student's).docx"

FILL_PATTERN = "DEEBF7"   # light blue
FILL_ANSWERS = "F2F2F2"   # grey
FILL_INSTR = "E4DFEC"     # lavender
TEXT_GREY = "595959"

W_NS = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
def w(tag):
    return f'{{{W_NS}}}{tag}'

def mk(tag):
    from lxml import etree
    return etree.Element(w(tag))

def make_run(text, bold=None, italic=None, color=None, font="Times New Roman", sz="22"):
    r = mk('r')
    if bold is not None or italic is not None or color is not None or font is not None or sz is not None:
        rPr = mk('rPr')
        if font:
            rf = mk('rFonts')
            rf.set(w('ascii'), font); rf.set(w('hAnsi'), font); rf.set(w('cs'), font)
            rPr.append(rf)
        if bold:
            rPr.append(mk('b'))
        if italic:
            rPr.append(mk('i'))
        if sz:
            s = mk('sz'); s.set(w('val'), sz); rPr.append(s)
            s2 = mk('szCs'); s2.set(w('val'), sz); rPr.append(s2)
        if color:
            c = mk('color'); c.set(w('val'), color); rPr.append(c)
        r.append(rPr)
    t = mk('t')
    t.set('{http://www.w3.org/XML/1998/namespace}space', 'preserve')
    t.text = text
    r.append(t)
    return r

def make_para(runs, style=None, border=False, fill=None, line360=True, color=None):
    """runs: list of run dicts {text, bold, italic, color, font, sz}."""
    p = mk('p')
    pPr = mk('pPr')
    if style:
        ps = mk('pStyle'); ps.set(w('val'), style); pPr.append(ps)
    if line360:
        sp = mk('spacing'); sp.set(w('line'), '360'); sp.set(w('lineRule'), 'auto'); pPr.append(sp)
    if border:
        pb = mk('pBdr')
        for side in ('top', 'left', 'bottom', 'right'):
            s = mk(side)
            s.set(w('val'), 'single'); s.set(w('sz'), '4'); s.set(w('space'), '4'); s.set(w('color'), 'auto')
            pb.append(s)
        pPr.append(pb)
    if fill:
        shd = mk('shd')
        shd.set(w('val'), 'clear'); shd.set(w('color'), 'auto'); shd.set(w('fill'), fill)
        pPr.append(shd)
    p.append(pPr)
    for rs in runs:
        p.append(make_run(**rs))
    return p

def make_plain(text, bold=False, **kw):
    return make_para([dict(text=text, bold=bold)], **kw)

def make_heading(text, style_id, sz=None, color=None, bold=True, italic=False):
    runs = [dict(text=text, bold=bold, italic=italic, sz=sz, color=color)]
    return make_para(runs, style=style_id, line360=True)

def make_table(widths, rows, fills=None, label_bold_col=None):
    """rows: list of rows; each row = list of cells; each cell = list of paragraphs; each paragraph = list of run dicts.
    label_bold_col: set of (row_idx, col_idx) whose FIRST run should be bold (label cells)."""
    tbl = mk('tbl')
    tblPr = mk('tblPr')
    ts = mk('tblStyle'); ts.set(w('val'), 'aff2'); tblPr.append(ts)
    tw = mk('tblW'); tw.set(w('w'), '0'); tw.set(w('type'), 'auto'); tblPr.append(tw)
    tl = mk('tblLook'); tl.set(w('val'), '04A0'); tl.set(w('firstRow'), '1'); tl.set(w('lastRow'), '0')
    tl.set(w('firstColumn'), '1'); tl.set(w('lastColumn'), '0'); tl.set(w('noHBand'), '0'); tl.set(w('noVBand'), '1')
    tblPr.append(tl)
    tbl.append(tblPr)
    grid = mk('tblGrid')
    for wd in widths:
        gc = mk('gridCol'); gc.set(w('w'), str(wd)); grid.append(gc)
    tbl.append(grid)
    label_bold_col = label_bold_col or set()
    for ri, row in enumerate(rows):
        tr = mk('tr')
        for ci, cell_paras in enumerate(row):
            # normalise nesting: a cell is a list of paragraphs; a paragraph is a list of run dicts
            if isinstance(cell_paras, dict):
                cell_paras = [[cell_paras]]
            elif cell_paras and isinstance(cell_paras[0], dict):
                cell_paras = [cell_paras]
            tc = mk('tc')
            tcPr = mk('tcPr')
            tcw = mk('tcW'); tcw.set(w('w'), str(widths[ci])); tcw.set(w('type'), 'dxa'); tcPr.append(tcw)
            if fills and fills[ri][ci] is not None:
                shd = mk('shd'); shd.set(w('val'), 'clear'); shd.set(w('color'), 'auto'); shd.set(w('fill'), fills[ri][ci])
                tcPr.append(shd)
            tc.append(tcPr)
            for para_runs in cell_paras:
                if (ri, ci) in label_bold_col and para_runs:
                    first = dict(para_runs[0]); first['bold'] = True
                    p = make_para([first] + para_runs[1:], line360=False)
                else:
                    p = make_para(para_runs, line360=False)
                tc.append(p)
            tr.append(tc)
        tbl.append(tr)
    return tbl

def cell_runs(text):
    return [[dict(text=text)]]

def cell_runs_italic(text):
    return [[dict(text=text, italic=True)]]

def set_row(paras_list):
    return paras_list

# ----------------------------------------------------------------------------
def build(is_teacher):
    doc = Document(TPL)
    body = doc.element.body

    # 1) Fix header paragraphs (index 2 and 3 of body children, before any table)
    children = list(body)
    p3 = children[2]
    # replace runs of P3 with a single run copying old rPr
    old_rpr = None
    for r in p3.findall(w('r')):
        rPr = r.find(w('rPr'))
        if rPr is not None and old_rpr is None:
            old_rpr = copy.deepcopy(rPr)
        p3.remove(r)
    r = mk('r')
    if old_rpr is not None:
        r.append(old_rpr)
    t = mk('t'); t.text = C.HEADER_3; r.append(t)
    p3.append(r)

    p4 = children[3]
    old_rpr4 = None
    for r in p4.findall(w('r')):
        rPr = r.find(w('rPr'))
        if rPr is not None and old_rpr4 is None:
            old_rpr4 = copy.deepcopy(rPr)
        p4.remove(r)
    r = mk('r')
    if old_rpr4 is not None:
        r.append(old_rpr4)
    t = mk('t'); t.text = C.TOPIC_LINE; r.append(t)
    p4.append(r)

    # 2) Drop everything after header P4, keep sectPr
    sectPr = body.find(w('sectPr'))
    for child in list(body):
        if child is p3 or child is p4 or child is children[0] or child is children[1]:
            continue
        body.remove(child)
    if sectPr is not None:
        body.append(sectPr)

    def add(el_):
        body.insert(len(body) - (1 if sectPr is not None else 0), el_)

    # ---- Part 1 ----
    add(make_heading(C.PART1_TITLE, '20'))
    add(make_plain(C.PART1_INTRO))
    add(make_table([9350], [[cell_runs(s)] for s, _, _ in C.QUIZ]))
    if is_teacher:
        add(make_plain(''))
        add(make_plain(C.TEACHER_ANSWERS_LABEL, bold=True))
        rows = [[[[dict(text='Item', bold=True)]], [[dict(text='Correction (fix both errors)', bold=True)]]]]
        for i, (_, corr, note) in enumerate(C.QUIZ, 1):
            rows.append([[[dict(text=str(i))]], [[dict(text=corr + ' ' + note)]]])
        fills = [[FILL_ANSWERS, FILL_ANSWERS]] * len(rows)
        add(make_table([620, 8730], rows, fills=fills))
        add(make_plain(''))
    else:
        add(make_plain(''))

    # ---- Warm-up (words → nouns), right after the proofreading part ----
    add(make_heading(C.WARMUP_TITLE, '31', sz='22'))
    add(make_plain(C.WARMUP_INTRO))
    wrows = [[[[dict(text='Word', bold=True)]], [[dict(text='Noun', bold=True)]]]]
    for i, word in enumerate(C.WARMUP_WORDS):
        if is_teacher:
            wrows.append([[[dict(text=word)]], [[dict(text=C.WARMUP_ANSWERS[i])]]])
        else:
            wrows.append([[[dict(text=word)]], [[dict(text='')]]])
    add(make_table([2605, 6745], wrows))
    add(make_plain(''))

    # ---- Part 2 ---- 
    add(make_heading(C.PART2_TITLE, '20'))
    add(make_plain(C.PART2_INTRO))
    for ex in C.EXAMPLES:
        add(make_heading(ex['title'], '31', sz='22'))
        rows = [
            [[dict(text='Plain:')], [dict(text=ex['plain'])]],
            [[dict(text='More formal:')], [dict(text=ex['formal'])]],
        ]
        fills = [[FILL_PATTERN, FILL_PATTERN]] * 2
        add(make_table([2605, 6745], rows, fills=fills))
        add(make_plain(ex['paragraph'], border=True))

    # ---- Part 2b: Nominalisation as a linking device (round-7) ----
    add(make_heading(C.LINK_TITLE, '31', sz='22'))
    add(make_plain(C.LINK_INTRO))
    for pair in C.LINK_EXAMPLES:
        s2_cell = [[dict(text=r) if isinstance(r, str) else dict(text=r['t'], italic=r['i']) for r in pair['s2']]]
        rows = [
            [[dict(text='Sentence 1:')], [dict(text=pair['s1'])]],
            [[dict(text='Linked sentence:')], s2_cell],
        ]
        add(make_table([2605, 6745], rows, fills=[[FILL_PATTERN, FILL_PATTERN]] * 2))
    add(make_plain(C.LINK_PARAGRAPH, border=True))
    add(make_plain(C.LINK_WATCHOUT, border=True))

    # ---- Part 3 ----
    add(make_plain(''))
    add(make_heading(C.PART3_TITLE, '1'))
    add(make_plain(C.PART3_INTRO))
    for title, simple, prompt, answer in C.SETS:
        add(make_heading(title, '31', sz='22'))
        if is_teacher:
            rows = [
                [cell_runs('Simple sentence:'), cell_runs(simple)],
                [cell_runs('Prompt:'), cell_runs_italic(prompt)],
                [cell_runs('Teacher’s Answer:'), cell_runs(answer)],
            ]
            add(make_table([2605, 6745], rows, label_bold_col={(2, 0)}))
        else:
            rows = [
                [cell_runs('Simple sentence:'), cell_runs(simple)],
                [cell_runs('Prompt:'), cell_runs_italic(prompt)],
                [cell_runs(''), cell_runs('')],
            ]
            add(make_table([2605, 6745], rows))

    # ---- Part 4 ----
    add(make_heading(C.PART4_TITLE, '1'))
    add(make_plain(C.INSTR_LABEL, border=True, fill=FILL_INSTR, bold=True))
    add(make_plain(C.INSTR_1, border=True, fill=FILL_INSTR))
    add(make_plain(C.INSTR_2, border=True, fill=FILL_INSTR))
    add(make_plain(C.INSTR_3, border=True, fill=FILL_INSTR))
    add(make_plain(C.WORD_BANK_LABEL, border=True, fill=FILL_INSTR))
    if is_teacher:
        bank = "   ·   ".join(f"{w} → {n}" for w, n in zip(C.WORD_BANK, C.WORD_BANK_ANSWERS))
        add(make_plain(bank, border=True, fill=FILL_ANSWERS))
        add(make_plain(C.TEACHER_BANK_NOTE, border=True, fill=FILL_ANSWERS))
    else:
        add(make_plain("   ·   ".join(C.WORD_BANK), border=True, fill=FILL_INSTR))
    if is_teacher:
        add(make_plain(''))
        for label, text in C.SAMPLES:
            add(make_para([dict(text=label, bold=True), dict(text=text)], border=True, fill=FILL_ANSWERS))
        add(make_plain(C.TEACHER_BRIDGE_NOTE, border=True, fill=FILL_ANSWERS))
    else:
        for _ in range(7):
            add(make_plain(C.UNDERSCORE_LINE))

    doc.save(OUT_TEACHER if is_teacher else OUT_STUDENT)
    print("saved:", OUT_TEACHER if is_teacher else OUT_STUDENT)

if __name__ == '__main__':
    build(sys.argv[1] == 'teacher')